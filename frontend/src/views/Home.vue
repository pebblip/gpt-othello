<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <v-sheet>
          <v-list class="bg-black">
            <v-list-item>
              <v-btn
                block
                @click="onPass"
                :disabled="canPlace"
                :class="!canPlace ? 'bg-orange' : ''"
                >パス</v-btn
              >
            </v-list-item>
            <v-list-item>
              <v-btn block @click="tryAgain">最初からやり直す</v-btn>
            </v-list-item>
            <v-list-item>
              <v-btn block @click="onGptAsk">ChatGPTに教えてもらう</v-btn>
            </v-list-item>

            <v-divider class="my-4" thickness="4"></v-divider>

            <v-list-item link color="grey-lighten-4">
              <v-list-item-title>
                <v-sheet
                  :height="250"
                  style="white-space: pre-wrap"
                  class="pa-2"
                >
                  {{ message }}
                </v-sheet>
              </v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-progress-linear
                v-if="loading"
                indeterminate
                color="yellow-darken-2"
                height="10"
              ></v-progress-linear>
            </v-list-item>
          </v-list>
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet>
          <v-list style="height: 80vmin" class="bg-black">
            <Board :size="size" :cells="cells" @place="onPlace" />
          </v-list>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import createClient from "openapi-fetch";
import { ref } from "vue";
import { onMounted } from "vue";
import { paths } from "@/generated/schema";
import { StoneColor } from "@/modules/StoneColor";
import { useStore } from "vuex";
import { computed, watch } from "vue";
import Board from "@/components/Board.vue";

const cells = ref<StoneColor[]>([]);
const size = ref<number>(8);
const status = ref<number>(0);
const canPlace = ref<boolean>(true);
const store = useStore();
const loading = computed(() => store.state.loading);
const message = ref<string>("");

watch(status, () => {
  if (status.value === 1) {
    message.value = "あなたの勝ち!";
  } else if (status.value === 2) {
    message.value = "コンピュータの勝ち!";
  } else {
    message.value = "引き分け!";
  }
});

const { get, post } = createClient<paths>({
  baseUrl: import.meta.env.VITE_BASE_API_URL,
});

function toArray(rows: number[][]): StoneColor[] {
  let cells: StoneColor[] = [];
  rows.forEach((row: number[]) => {
    row.forEach((col: number) => {
      let stoneColor: StoneColor = "none";
      if (col === -1) {
        stoneColor = "black";
      }

      if (col === 1) {
        stoneColor = "white";
      }

      cells.push(stoneColor);
    });
  });
  return cells;
}

function toDimension(): number[][] {
  const rows = [];
  for (var i = 0; i < size.value; i++) {
    const cols = [];
    for (var j = 0; j < size.value; j++) {
      const point = i * size.value + j;
      const cell = cells.value[point];
      let value = 0;
      if (cell === "black") {
        value = -1;
      }

      if (cell === "white") {
        value = 1;
      }

      cols.push(value);
    }
    rows.push(cols);
  }
  return rows;
}

onMounted(async () => {
  store.commit("updateLoading", { loading: true });
  try {
    const { data, error } = await get("/start", {});
    size.value = data!.size;
    cells.value = toArray(data!.rows);
    const blackScore = data!.score[0];
    const whiteScore = data!.score[1];

    store.commit("updateStone", { black: blackScore, white: whiteScore });
    store.commit("updateGptSuggestedPoint", { gptSuggestedPoint: undefined });
  } finally {
    store.commit("updateLoading", { loading: false });
  }
});

async function onPlace(x: number, y: number) {
  if (loading.value) {
    return;
  }
  store.commit("updateLoading", { loading: true });
  try {
    const { data, error } = await post("/user/place", {
      params: {
        query: { x: x, y: y },
      },
      body: toDimension(),
    });
    cells.value = toArray(data!.rows);
    canPlace.value = data!.valids.length > 0;
    status.value = data!.status;
    const blackScore = data!.score[0];
    const whiteScore = data!.score[1];

    store.commit("updateStone", { black: blackScore, white: whiteScore });
    store.commit("updateGptSuggestedPoint", { gptSuggestedPoint: undefined });

    await demandAiToPlace();
  } finally {
    store.commit("updateLoading", { loading: false });
  }
}

async function onPass() {
  if (canPlace.value) {
    alert("パスできません");
    return;
  }
  store.commit("updateLoading", { loading: true });
  try {
    const { data, error } = await post("/user/pass", {
      body: toDimension(),
    });
    cells.value = toArray(data!.rows);
    const blackScore = data!.score[0];
    const whiteScore = data!.score[1];
    canPlace.value = data!.valids.length > 0;
    status.value = data!.status;

    store.commit("updateStone", { black: blackScore, white: whiteScore });
    store.commit("updateGptSuggestedPoint", { gptSuggestedPoint: undefined });
  } finally {
    store.commit("updateLoading", { loading: false });
  }
}

async function demandAiToPlace() {
  store.commit("updateLoading", { loading: true });
  try {
    const { data, error } = await post("/ai/place", {
      body: toDimension(),
    });
    cells.value = toArray(data!.rows);
    const blackScore = data!.score[0];
    const whiteScore = data!.score[1];
    canPlace.value = data!.valids.length > 0;
    status.value = data!.status;

    store.commit("updateStone", { black: blackScore, white: whiteScore });
    store.commit("updateGptSuggestedPoint", { gptSuggestedPoint: undefined });
  } finally {
    store.commit("updateLoading", { loading: false });
  }
}

async function onGptAsk() {
  store.commit("updateLoading", { loading: true });
  try {
    const { data, error } = await post("/gpt/ask", {
      body: toDimension(),
    });
    const answer = data!.answer;
    const position = data!.position;
    message.value = answer;
    store.commit("updateGptSuggestedPoint", { gptSuggestedPoint: position });
  } finally {
    store.commit("updateLoading", { loading: false });
  }
}

function tryAgain() {
  location.reload();
}
</script>
