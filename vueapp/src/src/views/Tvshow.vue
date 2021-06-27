<template>
  <v-app>
    <v-main>
      <TvshowReleaseTable :id="id"></TvshowReleaseTable>
      <br />
      <br />
      <TvshowDetail :id="id"></TvshowDetail>
    </v-main>
  </v-app>
</template>

<script>
import TvshowDetail from "../components/TVShow/TvshowDetail.vue";
import TvshowReleaseTable from "../components/TVShow/TvshowReleaseTable.vue";
import { mapState, mapActions } from "vuex";

export default {
  name: "Tvshow",
  props: ["id"],
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
