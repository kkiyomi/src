<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          href="#"
          text
          v-bind="attrs"
          v-on="on"
        >
          <span v-if="account">{{ account.username }}</span>
          <span v-else>Account</span>
          <v-icon class="ml-1">mdi-home</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in isloggedin"
          :key="index"
          @click="Logout(item.title)"
          :to="item.page"
        >
          <v-list-item-title @click="Logout(item.title)">{{ item.title }}

          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'newDropdown',

  data () {
    return {
      loggedin_user: [
        { page: '/profile', title: 'Profile' },
        { page: '/readinglist', title: 'Reading List' },
        { page: '/logout', title: 'Logout' },
      ],
      notloggedin_user: [
        { page: '/login', title: 'Login' },
        { page: '/register', title: 'Register' },
      ],
    }
  },
  computed: {
    ...mapState(['account']),
    isloggedin () {
      if (this.$store.state.token) {
        return this.loggedin_user
      } else {
        return this.notloggedin_user
      }
    }
  },
  methods: {
    ...mapActions(['AccountLogout']),
    Logout (title) {
      if (title === 'Logout') {
        this.AccountLogout()
      }
    }
  },
}
</script>
