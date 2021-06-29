<template>
  <div>
    <newnavbar></newnavbar>
    <v-main>
      <v-container>
        <v-snackbar v-model="alert.state" :timeout="alert.timeout" top>
          {{ this.alert.message }}

          <template v-slot:action="{ attrs }">
            <v-btn color="pink" text v-bind="attrs" @click="resetAlert()">
              Close
            </v-btn>
          </template>
        </v-snackbar>
        <v-row class="text-center">
          <v-col>
            <router-link class="red-link" :to="{ name: 'Home' }"
              >Home</router-link
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
import { mapState } from "vuex";

export default {
  name: "MainPage",

  components: {
    newnavbar,
  },

  data() {
    return {};
  },
  computed: {
    ...mapState(["alert"]),
  },
  methods: {
    resetAlert() {
      this.alert.state = false;
      this.alert.message = null;
    },
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
