<template>
  <div v-if="releases && this.tvshow != null">
    <v-card class="mx-auto" width="700" outlined v-if="tvshow.slug === slug">
      <v-card-title>
        Releases
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        dense
        :headers="headers"
        :items="releases"
        :search="search"
        sort-by="date_added"
        sort-desc
        single-select
        v-model="Oselected"
        item-key="id"
        show-select
        class="elevation-1"
      >
        <template #item.date_added="{ item }">
          <TableColumn :date_added="item.date_added"></TableColumn>
        </template>
        <template #item.group="{ item }"> gggup {{ item.id }} </template>
        <template #item.number="{ item }">
          <a :href="item.link" target="_blank">{{ item.number }}</a>
        </template>
        <template slot="footer" v-if="Oselected.length !== 0">
          <v-btn
            style="position: absolute; left: 10px; bottom: 10px"
            elevation="2"
            color="primary"
            @click="addSerie"
            v-if="currentSerie == null"
            text
          >
            Follow
          </v-btn>
          <v-btn
            style="position: absolute; left: 10px; bottom: 10px"
            elevation="2"
            color="error"
            @click="RemoveSerieFromReadingList"
            v-else
            text
          >
            remove
          </v-btn>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
import TableColumn from "./TableColumn";
import { mapState, mapActions, mapGetters } from "vuex";

export default {
  name: "TvshowReleaseTable",
  props: ["id", "slug"],

  components: {
    TableColumn,
  },
  data() {
    return {
      isloaded: false,
      Oselected: [],
      search: "",
      headers: [
        {
          text: "Date",
          align: "start",
          width: "150",
          value: "date_added",
        },
        { text: "Group", value: "group" },
        { text: "Release", value: "number", width: "100" },
      ],
    };
  },
  computed: {
    ...mapGetters(["getNumberfromId", "currentSerie"]),
    ...mapState(["releases", "tvshow", "account", "alert"]),
  },
  methods: {
    ...mapActions([
      "getReleaseList",
      "UpdateSerie",
      "AddSerieToReadingList",
      "DeleteSerieFromReadingList",
      "AccountReadinglist",
    ]),
    async addSerie() {
      if (this.currentSerie == null && this.Oselected.length !== 0) {
        await this.AddSerieToReadingList({
          current_release_id: this.Oselected[0].id,
          tvshow: this.tvshow.id,
          readinglist: this.account.id,
        });
        await this.AccountReadinglist(this.account.id);

        this.alert.message = "Entry sucessfully added...";
        this.openAlert();
      }
    },
    async RemoveSerieFromReadingList() {
      await this.DeleteSerieFromReadingList(this.currentSerie.id);
      await this.AccountReadinglist(this.account.id);
      this.Oselected = [];

      this.alert.message = "Entry sucessfully removed...";
      this.openAlert();
    },
    openAlert() {
      this.alert.state = true;
    },
  },
  async created() {
    // console.log(this.slug, this.id);
    // await this.getReleaseList(this.id);
  },
  watch: {
    async tvshow(tvshow) {
      if (tvshow != null) {
        await this.getReleaseList(this.tvshow.id);
      }
    },
    getNumberfromId: function (newSelected, oldSelected) {
      if (
        newSelected !== this.Oselected &&
        newSelected[0] != null &&
        oldSelected !== newSelected
      ) {
        this.Oselected = this.getNumberfromId;
      }
    },
    Oselected: function (newSelected, oldSelected) {
      if (
        oldSelected != null &&
        oldSelected[0] != null &&
        newSelected[0] !== oldSelected[0] &&
        this.currentSerie != null
      ) {
        this.UpdateSerie({
          id: this.currentSerie.id,
          selected: newSelected[0].id,
        });
      }
    },
  },
};
</script>
