<template>
  <v-app id="inspire">
    <v-main>
      <v-container>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="6">
            <v-card :key="globalKey">
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
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="Login" class="mr-4">Login</v-btn>
                <v-btn class="mr-4">clear</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>
<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "loginForm",

  data() {
    return {
      info: {
        username: "",
        password: "",
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
      await this.AccountLogin(this.info);
      await this.getAccountInfo();
      await this.AccountReadinglist(this.account.id);
      this.$router.push("/");
    },
  },
};
</script>
