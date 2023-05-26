<template>
  <div class="cell">
    <div class="content"><Stone :color="color" /></div>
  </div>
</template>

<script lang="ts" setup>
import Stone from "./Stone.vue";

import { PropType } from "vue";
import { StoneColor } from "@/modules/StoneColor";

const props = defineProps({
  color: {
    type: String as PropType<StoneColor>,
    default: "none",
  },
});
</script>

<style scoped>
.cell {
  width: calc(100% / 18);
  aspect-ratio: 1/1;
  background: white;
  padding: 0.5px;
}

.content {
  background-color: #008000;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
