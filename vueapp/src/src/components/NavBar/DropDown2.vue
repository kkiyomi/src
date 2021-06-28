<template>
  <div class="text-center">
    <login-register-tabs v-if="!token"> </login-register-tabs>
    <v-btn text @click="AccountLogout()"> Logout </v-btn>
  </div>
</template>

<script>
import LoginRegisterTabs from "../Account/LoginRegisterTabs.vue";

import { mapState, mapActions } from "vuex";

export default {
  name: "newDropdown",

  components: {
    LoginRegisterTabs,
  },
  data() {
    return {};
  },
  computed: {
    ...mapState(["account", "token"]),
  },
  methods: {
    ...mapActions(["AccountLogout"]),
    Logout(title) {
      if (title === "Logout") {
        this.AccountLogout();
      }
    },
  },
};
</script>
