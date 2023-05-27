<template>
  <v-dialog v-model="ended" width="auto" transition="dialog-top-transition">
    <v-card>
      <v-toolbar color="green" title="ゲーム終了"></v-toolbar>
      <v-card-text>{{ message }}</v-card-text>
      <v-card-actions>
        <v-spacer />
        <v-btn @click="onEndGame">終わる</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts" setup>
import { computed } from "vue";

const props = defineProps({
  status: {
    type: Number,
    required: true,
  },
});

const ended = computed(() => props.status != 0);

const message = computed(() => {
  if (props.status === 1) {
    return "あなたの勝ち!";
  }

  if (props.status === 2) {
    return "コンピュータの勝ち!";
  }

  return "引き分け!";
});

async function onEndGame() {
  location.reload();
}
</script>
