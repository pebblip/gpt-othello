<template>
  <div class="bg-black h-100">
    <div
      class="d-flex justify-center"
      v-for="i in rows"
      :key="i"
      style="height: calc(100% / 8)"
    >
      <Cell
        v-for="j in cols"
        :key="j"
        :color="cellAt(j, i)"
        :x="j"
        :y="i"
        @click="place(j, i)"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { PropType, computed } from "vue";
import { StoneColor } from "@/modules/StoneColor";
import { useStore } from "vuex";
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
