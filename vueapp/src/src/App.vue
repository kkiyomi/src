<template>
  <v-app>
    <MainPage></MainPage>
  </v-app>
</template>

<script>
import MainPage from "./views/Main.vue";
import { mapState, mapActions } from "vuex";

export default {
  name: "App",

  components: {
    MainPage,
  },

  data() {
    return {};
  },
  computed: {
    ...mapState(["account"]),
  },
  methods: {
    ...mapActions(["getAccountInfo", "AlreadyLoggedIn", "AccountReadinglist"]),
  },
  async created() {
    if (this.$cookies.isKey("at")) {
      this.AlreadyLoggedIn(this.$cookies.get("at"));
      await this.getAccountInfo();
      await this.AccountReadinglist(this.account.id);
    }
  },
  beforeUpdate() {},
};
</script>

<style>
a {
  text-decoration: none;
}
.red-link:hover {
  color: #ea3c53 !important;
}
</style>
