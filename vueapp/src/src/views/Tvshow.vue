<template>
  <v-app>
    <v-main>
      <TvshowReleaseTable :slug="slug"></TvshowReleaseTable>
      <br />
      <br />
      <TvshowDetail :slug="slug"></TvshowDetail>
    </v-main>
  </v-app>
</template>

<script>
import TvshowDetail from "../components/TVShow/TvshowDetail.vue";
import TvshowReleaseTable from "../components/TVShow/TvshowReleaseTable.vue";
import { mapState, mapActions } from "vuex";

export default {
  name: "Tvshow",
  props: ["slug"],
  components: {
    TvshowDetail,
    TvshowReleaseTable,
  },

  data() {
    return {};
  },
  computed: {
    ...mapState(["serie_set"]),
  },
  methods: {
    ...mapActions(["getReleaseList"]),
  },
};
</script>
