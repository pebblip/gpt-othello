<template>
  <v-app>
    <default-bar />

    <default-view />

    <v-footer app class="bg-black d-flex flex-column">
      <div class="d-flex w-100 justify-center align-center">
        <span>&copy; 2023 <strong>Higurin</strong></span>
        <v-btn
          class="mx-4"
          variant="plain"
          icon="mdi-github"
          href="https://github.com/pebblip/gpt-othello"
          target="_blank"
        />
      </div>
    </v-footer>
  </v-app>
</template>

<script lang="ts" setup>
import DefaultBar from "./AppBar.vue";
import DefaultView from "./View.vue";
</script>
