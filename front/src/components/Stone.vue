<template>
  <div
    class="rounded-circle d-inline-block"
    :class="stoneColor"
    style="height: 90%; width: 90%"
  />
</template>

<script lang="ts" setup>
import { PropType, computed } from "vue";
import { StoneColor } from "@/modules/StoneColor";

const props = defineProps({
  color: {
    type: String as PropType<StoneColor>,
    default: "none",
  },
});

const stoneColor = computed(() => {
  if (props.color == "black") {
    return "bg-black";
  }
  if (props.color == "white") {
    return "bg-white";
  }

  return "";
});
</script>
