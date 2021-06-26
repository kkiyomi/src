<template>
  <div v-if="tvshow != null">
    <v-card
      class="mx-auto"
      width="700"
      outlined
      v-if="tvshow.slug === slug"
    >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4"><h1>{{ tvshow.title }}</h1></div>
          <br>
          <v-card-text class="text-left">
            <p>Year : {{ tvshow.year }}</p>
            <p>{{ tvshow.description }}</p>
          </v-card-text>
        </v-list-item-content>

        <v-img
          :alt="tvshow.title"
          contain
          class="my-4"
          align-self="center"
          max-width="200"
          :src="tvshow.image"
          transition="scale-transition"
          width="40"
        />
      </v-list-item>
    </v-card>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'TvshowDetail',
  props: ['slug'],

  data () {
    return {
    }
  },
  methods: {
    ...mapActions(['getTVShowDetail']),
  },
  computed: {
    ...mapState(['tvshow']),
  },
  created () {
    this.getTVShowDetail(this.slug)
  },
}
</script>
