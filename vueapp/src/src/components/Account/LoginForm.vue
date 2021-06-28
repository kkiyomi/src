<template>
  <v-card class="">
    <v-container>
      <v-row class="grey darken-4 my-n3 pa-0 pb-n4">
        <v-card-text>
          <v-form>
            <v-text-field
              label="Username"
              v-model="info.username"
              :rules="usernameRules"
              prepend-icon="mdi-account"
              type="text"
              required
            ></v-text-field>

            <v-text-field
              id="password"
              label="Password"
              v-model="info.password"
              prepend-icon="mdi-lock"
              type="password"
              required
            ></v-text-field>

            <v-checkbox
              class="mb-n4"
              v-model="checkbox"
              label="Remember Me"
            ></v-checkbox>
          </v-form>
        </v-card-text>
      </v-row>
    </v-container>

    <v-card-actions class="py-4">
      <v-btn
        block
        elevation="2"
        class="mr-4"
        color="primary blue darken-1"
        @click="Login"
      >
        Login
      </v-btn>
    </v-card-actions>

    <v-card-actions class="pb-4 justify-center">
      <a href="" class="text-subtitle-2"> Forgot your password? </a>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "LoginForm",

  data() {
    return {
      checkbox: false,
      info: {
        username: "",
        password: "",
        cookies_setting: {
          expires: 7,
        },
      },
      usernameRules: [
        (v) => !!v || "Username is required",
        (v) => v.length >= 4 || "Username must be more than 4 characters",
      ],
    };
  },
  computed: {
    ...mapState(["account", "token", "globalKey"]),
  },
  methods: {
    ...mapActions(["AccountLogin", "getAccountInfo", "AccountReadinglist"]),
    async Login() {
      if (this.checkbox) {
        this.info.cookies_setting.expires = "1Y";
      }
      await this.AccountLogin(this.info);
      await this.getAccountInfo();
      await this.AccountReadinglist(this.account.id);
    },
  },
};
</script>