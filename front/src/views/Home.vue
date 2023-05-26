<template>
  <v-container>
    <Board :size="size" :cells="cells" @place="onPlace" />

    <v-progress-linear
      v-if="loading"
      indeterminate
      rounded
      height="20"
      color="light-gray"
      striped
    ></v-progress-linear>
  </v-container>
</template>

<script lang="ts" setup>
import createClient from "openapi-fetch";
import { ref } from "vue";
import { onMounted } from "vue";
import { paths } from "@/generated/schema";
import Board from "@/components/Board.vue";
import { StoneColor } from "@/modules/StoneColor";
import { useStore } from "vuex";
import { computed } from "vue";

const cells = ref<StoneColor[]>([]);
const size = ref<number>(8);

const { get, post } = createClient<paths>({
  baseUrl: "http://localhost:8889/api",
});

const store = useStore();

const loading = computed(() => store.state.loading);

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
    const { data, error } = await post("/user-place", {
      params: {
        query: { x: x, y: y },
      },
      body: toDimension(),
    });
    cells.value = toArray(data!.rows);
    const blackScore = data!.score[0];
    const whiteScore = data!.score[1];
    store.commit("updateStone", { black: blackScore, white: whiteScore });
  } finally {
    store.commit("updateLoading", { loading: false });
  }

  await demandAiToPlace();
}

async function demandAiToPlace() {
  store.commit("updateLoading", { loading: true });
  try {
    console.log("ai1");
    const { data, error } = await post("/ai-place", {
      body: toDimension(),
    });
    console.log("ai2");
    cells.value = toArray(data!.rows);
    const blackScore = data!.score[0];
    const whiteScore = data!.score[1];
    store.commit("updateStone", { black: blackScore, white: whiteScore });
  } finally {
    store.commit("updateLoading", { loading: false });
  }
}
</script>
