<template>
  <board :size="size" :cells="cells" />
</template>

<script lang="ts" setup>
import HelloWorld from "@/components/HelloWorld.vue";
import Board from "@/components/Board.vue";
import { StoneColor } from "@/modules/StoneColor";

const size = 8;
const cells: StoneColor[] = Array.from({ length: 8 * 8 }, (_, i) => "black");
</script>
