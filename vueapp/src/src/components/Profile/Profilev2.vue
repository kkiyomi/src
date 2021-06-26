<template>
  <v-card
    class="mx-auto"
    max-width="900"
    max-height="400"
  >
  <v-row no-gutters>
    <v-col cols="4">
      <v-img
        class="white--text mx-auto"
        src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
      >
      </v-img>
    </v-col>
    <v-col cols="8">
      <v-card-title>
        {{ account.username }}
      </v-card-title>
      <v-container style="margin-left: 5%;">
        <v-row no-gutters v-for="(item, i) in accountData" :key="i">
          <v-col cols="3">{{ item.name }}</v-col>
          <v-col>{{ item.value }}</v-col>
        </v-row>
      </v-container>
    </v-col>
  </v-row>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Profilev2',

  data () {
    return {
    }
  },
  computed: {
    ...mapState(['account']),
    dateFormated () {
      return this.account.date_joined.split('T')[0]
    },
    accountData () {
      return [
        { name: 'User ID', icon: 'account', value: this.account.id },
        { name: 'User level', icon: 'clock-time-four-outline', value: 'Member' },
        { name: 'Date Joined', icon: 'calendar-month-outline', value: this.dateFormated },
        { name: 'Last online', icon: 'clock-time-four-outline', value: 'dd' },
        { name: 'Group(s)', icon: 'account-multiple', value: 'dd' },
        { name: 'Biography', icon: '', value: 'dd' }
      ]
    },
  },
  methods: {
    ...mapActions(['getAccountInfo']),
  },
}

</script>
