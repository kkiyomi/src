<template>
  <div>
    <newnavbar></newnavbar>
    <v-main>
      <v-container>
        <v-row class="text-center">
          <v-col>
            <router-link class="red-link" :to="{ name: 'Home' }"
              >Home</router-link
            >
            |
            <router-link class="red-link" :to="{ name: 'About' }"
              >About</router-link
            >
            |
            <router-link class="red-link" :to="{ name: 'Login' }"
              >Login</router-link
            >
            |
            <router-link class="red-link" :to="{ name: 'Register' }"
              >Register</router-link
            >
            |
            <router-link class="red-link" :to="{ name: 'ReadingList' }"
              >Readinglist</router-link
            >
            |
            <router-link class="red-link" :to="{ name: 'Profile' }"
              >Profile</router-link
            >
            |
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <router-view></router-view>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>

<script>
import newnavbar from "../components/NavBar/NewNavbar.vue";
import { mapState, mapActions } from "vuex";

export default {
  name: "MainPage",

  components: {
    newnavbar,
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
