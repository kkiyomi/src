<template>
  <div class="home" v-if="tvshows_paginated">
    <v-container fluid>
      <v-row justify="center" align="center">
        <template v-for="(show, idx) in tvshows_paginated.results">
          <v-col :key="idx" md="auto">
            <v-card class="mx-auto" max-width="200">
              <router-link
                :to="{
                  name: 'TvshowDetail',
                  params: { slug: show.slug, id: show.id },
                }"
              >
                <v-img
                  class="white--text align-end"
                  max-width="200"
                  max-height="250"
                  :src="show.image"
                  transition="scale-transition"
                  :alt="show.title"
                >
                </v-img>
              </router-link>
              <v-card-title class="justify-center">
                <router-link
                  class="red-link"
                  :to="{
                    name: 'TvshowDetail',
                    params: { slug: show.slug, id: show.id },
                  }"
                >
                  {{ show.title }}
                </router-link>
              </v-card-title>
            </v-card>
          </v-col>
          <v-responsive
            v-if="idx === 2"
            :key="`width-${idx}`"
            width="100%"
          ></v-responsive>
        </template>
      </v-row>
    </v-container>
    <template>
      <div class="text-center">
        <v-pagination
          v-model="page"
          :length="tvshows_paginated.length"
          @input="PageChange"
          :total-visible="10"
        ></v-pagination>
      </div>
    </template>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "Home",

  data() {
    return {
      page: 1,
    };
  },
  computed: {
    ...mapState(["tvshows", "tvshows_paginated"]),
  },
  methods: {
    ...mapActions(["getTVShowList", "getTVShowPagination"]),
    PageChange(page) {
      this.getTVShowPagination(page);
    },
  },
  mounted() {
    // this.getTVShowList()
    this.getTVShowPagination(1);
  },
  updated() {},
};
</script>
