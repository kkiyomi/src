<template>
  <div id="newnavbar" data-app>
    <v-app-bar app dark>
      <div class="d-flex align-center mr-2 ml-16">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>
      <v-btn active-class="no-active" class="mx-1 ml-4" text to="/">
        <span>Home</span>
      </v-btn>

      <v-btn
        active-class="no-active"
        class="mx-1"
        text
        v-if="account"
        :to="{ name: 'ReadingList' }"
      >
        <span class="mr-1">Reading List</span>
      </v-btn>

      <v-spacer></v-spacer>

      <newDropdown class="mr-16"></newDropdown>
    </v-app-bar>
  </div>
</template>

<script>
import newDropdown from "./DropDown2.vue";
import { mapState } from "vuex";

export default {
  name: "newnavbar",

  components: {
    newDropdown,
  },
  data() {
    return {};
  },
  computed: {
    ...mapState(["account"]),
  },
};
</script>

<style>
.v-btn--active.no-active::before {
  opacity: 0 !important;
}
</style>
