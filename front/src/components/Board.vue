<template>
  <v-container>
    <div class="d-flex justify-center">
      <div class="grid">
        <div
          class="d-flex justify-center"
          v-for="i in [1, 2, 3, 4, 5, 6, 7, 8]"
          :key="i"
          style="width: 100%"
        >
          <Cell v-for="j in [1, 2, 3, 4, 5, 5, 6, 7, 8]" :key="j" />
        </div>
      </div>
    </div>
  </v-container>
</template>

<script lang="ts" setup>
import { isUserWhitespacable } from "@babel/types";
import Cell from "./Cell.vue";

const props = defineProps({
  size: {
    type: Number,
    default: 8,
  },
});

enum Status {
  Black,
  White,
  Empty,
}

type Point = {
  x: number;
  y: number;
  status: Status;
};
</script>

<style scoped>
.grid {
  background-color: white;
  width: 100%;
  padding: 0.5px;
}
</style>
