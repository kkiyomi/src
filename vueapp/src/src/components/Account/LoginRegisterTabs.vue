<template>
  <v-dialog v-model="dialog" max-width="350px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn text v-bind="attrs" v-on="on"> Login/Register </v-btn>
    </template>
    <v-card>
      <v-container class="">
        <v-card>
          <v-tabs v-model="tabs" centered>
            <v-tab> Login </v-tab>
            <v-tab> Register </v-tab>
          </v-tabs>

          <v-tabs-items v-model="tabs">
            <v-tab-item>
              <login-form />
            </v-tab-item>
            <v-tab-item>
              <register-form />
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </v-container>
    </v-card>
  </v-dialog>
</template>


<script>
import LoginForm from "../Account/LoginForm.vue";
import RegisterForm from "../Account/RegisterForm.vue";
import { mapState, mapActions } from "vuex";

export default {
  name: "LoginRegisterTabs",

  components: {
    LoginForm,
    RegisterForm,
  },

  data() {
    return {
      dialog: false,
      tabs: null,
    };
  },
  computed: {
    ...mapState(["token"]),
  },
  methods: {
    async Login() {
      await this.AccountLogin(this.info);
      await this.getAccountInfo();
      await this.AccountReadinglist(this.account.id);
    },
  },
  watch: {
    token(loggedin) {
      if (loggedin) {
        this.dialog = false;
      }
    },
  },
};
</script>