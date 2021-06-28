<template>
  <v-card v-if="token === null">
    <v-container class="">
      <v-row class="my-n3 pa-0 pb-n4">
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              label="Username"
              v-model="info.username"
              :rules="usernameRules"
              prepend-icon="mdi-account"
              type="text"
              required
              clearable
            ></v-text-field>
            <v-text-field
              label="Email"
              v-model="info.email"
              :rules="emailRules"
              prepend-icon="mdi-email"
              type="text"
              required
              clearable
            ></v-text-field>
            <v-text-field
              id="password"
              label="Password"
              v-model="info.password"
              prepend-icon="mdi-lock"
              type="password"
              required
              clearable
            ></v-text-field>
            <v-text-field
              id="password"
              label="Repeat Password"
              v-model="info.password2"
              prepend-icon="mdi-lock"
              type="password"
              required
              clearable
            ></v-text-field>
          </v-form>
        </v-card-text>
      </v-row>
    </v-container>

    <v-card-actions class="py-4">
      <v-btn
        class="mr-4"
        color="primary blue darken-1"
        elevation="2"
        block
        @click="Register"
      >
        Register
      </v-btn>
    </v-card-actions>
  </v-card>
</template>


<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "RegisterForm",

  data() {
    return {
      valid: true,
      info: {
        username: "",
        email: "",
        password: "",
        password2: "",
      },
    };
  },
  computed: {
    ...mapState(["token", "account"]),
    usernameRules() {
      return [
        (value) => !!value || "Username is required",
        (value) =>
          value.length >= 4 || "Username must be more than 4 characters",
      ];
    },
    emailRules() {
      return [
        (value) => !!value || "Email is required",
        (value) => /.+@.+/.test(value) || "E-mail must be valid",
      ];
    },
  },
  methods: {
    ...mapActions([
      "AccountRegister",
      "AddReadinglist",
      "getAccountInfo",
      "AccountReadinglist",
    ]),
    async Register() {
      await this.AccountRegister(this.info);
      await this.AddReadinglist();
      await this.getAccountInfo();
      await this.AccountReadinglist(this.account.id);
    },
    ResetForm() {
      this.$refs.form.reset();
    },
  },
};
</script>
