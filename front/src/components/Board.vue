<template>
  <div class="d-flex justify-center">
    <div class="grid">
      <div class="d-flex justify-center" v-for="i in rows" :key="i">
        <Cell
          v-for="j in cols"
          :key="j"
          :color="cellAt(j, i)"
          @click="place(j, i)"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { PropType } from "vue";
import { StoneColor } from "@/modules/StoneColor";
import Cell from "./Cell.vue";

const props = defineProps({
  size: {
    type: Number,
    required: true,
  },
  cells: {
    type: Array as PropType<StoneColor[]>,
    required: true,
  },
  cells: {
    type: Array as PropType<StoneColor[]>,
    required: true,
  },
});

const emits = defineEmits<{ (e: "place", x: number, y: number): void }>();

const rows = Array.from({ length: props.size }, (_, i) => i);
const cols = Array.from({ length: props.size }, (_, i) => i);

function cellAt(x: number, y: number): StoneColor {
  return props.cells[x * props.size + y];
}

function place(x: number, y: number) {
  emits("place", x, y);
}
</script>

<style scoped>
.grid {
  background-color: white;
  width: 100%;
  padding: 0.5px;
}
</style>
