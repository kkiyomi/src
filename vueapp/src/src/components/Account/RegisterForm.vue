<template>
  <v-app id="inspire">
    <v-main>
      <v-container>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="6">
            <v-card v-if="token === null">
              <v-card-text>
                <v-form>
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
                  ></v-text-field>

                  <v-text-field
                    id="password"
                    label="Repeat Password"
                    v-model="info.password2"
                    prepend-icon="mdi-lock"
                    type="password"
                    required
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="Register" class="mr-4">Register</v-btn>
                <v-btn class="mr-4">clear</v-btn>
              </v-card-actions>
            </v-card>
            <div v-else>
              <br />
              <h1>already logged in</h1>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "registerForm",

  data() {
    return {
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
  },
};
</script>
