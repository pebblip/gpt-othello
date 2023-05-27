/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

// Plugins
import { registerPlugins } from "@/plugins";

import { createStore } from "vuex";

const store = createStore({
  state() {
    return {
      stone: {
        black: 0,
        white: 0,
      },
      loading: false,
      gptSuggestedPoint: undefined,
    };
  },
  mutations: {
    updateStone(state, payload) {
      state.stone.black = payload.black;
      state.stone.white = payload.white;
    },

    updateLoading(state, payload) {
      state.loading = payload.loading;
    },

    updateGptSuggestedPoint(state, payload) {
      state.gptSuggestedPoint = payload.gptSuggestedPoint;
    },
  },
});

const app = createApp(App);

registerPlugins(app);
app.use(store);

app.mount("#app");
