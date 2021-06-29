<template>
  <div class="text-center">
    <login-register-tabs v-if="!account"> </login-register-tabs>

    <!-- <v-avatar v-else class="mr-4" color="teal" size="30">
      <v-icon dark> mdi-account-circle </v-icon>
    </v-avatar> -->

    <v-menu v-else bottom min-width="200px" rounded offset-y>
      <template v-slot:activator="{ on }">
        <v-btn icon x-large v-on="on">
          <v-avatar color="brown" size="30">
            <v-icon dark> mdi-account-circle </v-icon>
          </v-avatar>
        </v-btn>
      </template>
      <v-card>
        <v-list-item-content class="justify-center">
          <div class="mx-auto text-center">
            <h3>{{ account.username }}</h3>
            <p class="text-caption mt-1">
              {{ account.email }}
            </p>
            <!-- <v-divider class="my-3"></v-divider>
            <v-btn depressed rounded text> Edit Account </v-btn> -->
            <v-divider class="my-3"></v-divider>
            <v-btn depressed rounded text @click="AccountLogout()">
              Logout
            </v-btn>
          </div>
        </v-list-item-content>
      </v-card>
    </v-menu>
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
  },
};
</script>
