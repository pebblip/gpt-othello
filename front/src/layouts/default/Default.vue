<template>
  <v-app>
    <default-bar />

    <default-view />

    <v-footer :elevation="8">
      <v-row justify="center" no-gutters>
        <v-col class="text-center mt-4" cols="12"> &copy; 2023 Higurin </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script lang="ts" setup>
import DefaultBar from "./AppBar.vue";
import DefaultView from "./View.vue";
</script>
