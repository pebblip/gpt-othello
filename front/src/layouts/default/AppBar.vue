<template>
  <v-app-bar :elevation="8">
    <v-app-bar-title>
      <v-icon icon="mdi-checkbox-blank-circle" />
      Webオセロ
      <v-icon icon="mdi-checkbox-blank-circle-outline" />
    </v-app-bar-title>
    <v-spacer />

    <v-btn icon>
      <v-icon>mdi-checkbox-blank-circle</v-icon>
      {{ blackScore }}
    </v-btn>

    <v-btn icon>
      <v-icon>mdi-checkbox-blank-circle-outline</v-icon>
      {{ whiteScore }}
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts" setup>
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();

const blackScore = computed(() => store.state.stone.black);
const whiteScore = computed(() => store.state.stone.white);
</script>
