<template>
  <Board :size="size" :cells="cells" @place="onPlace" />
</template>

<script lang="ts" setup>
import createClient from "openapi-fetch";
import { ref } from "vue";
import { onMounted } from "vue";
import { paths } from "@/generated/schema";
import Board from "@/components/Board.vue";
import { StoneColor } from "@/modules/StoneColor";

const cells = ref<StoneColor[]>([]);
const size = ref<number>(8);

const { get, post } = createClient<paths>({
  baseUrl: "http://localhost:8889/api",
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

onMounted(async () => {
  const { data, error } = await get("/start", {});
  size.value = data.size;
  cells.value = toArray(data!.rows);
});

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

async function onPlace(x: number, y: number) {
  console.log("place", x, y);

  const { data, error } = await post("/user/place", {
    params: {
      query: { x: x, y: y },
    },
    body: toDimension(),
  });
  cells.value = toArray(data!.rows);

  await demandAiToPlace();
}

async function demandAiToPlace() {
  const { data, error } = await post("/ai/place", {
    body: toDimension(),
  });
  cells.value = toArray(data!.rows);
}
</script>
