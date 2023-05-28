<template>
  <div class="cell">
    <div
      class="content d-flex justify-center align-center"
      :class="gptSuggested ? 'bg-blue' : ''"
    >
      <Stone :color="color" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import Stone from "./Stone.vue";
import { PropType, computed } from "vue";
import { StoneColor } from "@/modules/StoneColor";
import { useStore } from "vuex";

const props = defineProps({
  color: {
    type: String as PropType<StoneColor>,
    default: "none",
  },
  x: {
    type: Number,
    required: true,
  },
  y: {
    type: Number,
    required: true,
  },
});

const store = useStore();
const gptSuggestedPoint = computed(() => store.state.gptSuggestedPoint);

console.log("suggested", gptSuggestedPoint);

const gptSuggested = computed(
  () =>
    gptSuggestedPoint.value &&
    gptSuggestedPoint.value[0] == props.x &&
    gptSuggestedPoint.value[1] == props.y
);

console.log("xxx", gptSuggested);
</script>

<style scoped>
.cell {
  aspect-ratio: 1/1;
  background: white;
  padding: 0.5px;
}

.content {
  background-color: #008000;
  height: 100%;
  width: 100%;
}
</style>
