<template>
  <div>
    <div v-if="account">
      <v-card class="mx-auto" width="700" outlined v-if="serie_set">
        <v-card-title v-if="account.readinglist === null">
          <v-btn class="ml-4" @click="AddList"> activate Reading List </v-btn>
        </v-card-title>
        <v-card-title v-else>
          Reading List
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
          v-if="account.readinglist !== null"
          dense
          :headers="headers"
          :items="serie_set"
          :search="search"
          v-model="selected"
          :sort-by.sync="sortBy"
          :sort-desc.sync="sortDesc"
          item-key="id"
          show-select
          class="elevation-1"
        >
          <template #item.tvshow_title="{ item }">
            <router-link
              class="red-link"
              :to="{
                name: 'TvshowPage',
                params: { slug: item.tvshow_slug },
              }"
              >{{ item.tvshow_title }}
            </router-link>
          </template>
          <template #item.tvshow_release_number="{ item }">
            <a
              :href="item.tvshow_release_link"
              class="red-link"
              target="_blank"
            >
              {{ item.tvshow_release_number }}
            </a>
          </template>
          <template #item.tvshow_latest_number="{ item }">
            <a :href="item.tvshow_latest_link" class="red-link" target="_blank">
              {{ item.tvshow_latest_number }}
            </a>
          </template>
          <template #item.tvshow_latest_date_added="{ item }">
            <TableColumn
              :date_added="item.tvshow_latest_date_added"
            ></TableColumn>
          </template>
          <template slot="footer">
            <!-- <v-btn
              style="position: absolute; left: 10px; bottom: 10px"
              elevation="2"
              color="error"
              v-if="selected.length !== 0"
              @click="RemoveSerieFromReadingList"
              text
            >
              Remove
            </v-btn> -->
            <RemoveSerieDialog
              v-if="selected.length !== 0"
              :selected="selected"
              @RemoveFromReadingList="updateSelected"
            ></RemoveSerieDialog>
          </template>
        </v-data-table>
      </v-card>
    </div>
    <div v-else>log in first</div>
  </div>
</template>

<script>
import TableColumn from "../TVShow/TableColumn.vue";
import RemoveSerieDialog from "../Account/RemoveSerieDialog.vue";

import { mapState, mapActions } from "vuex";
export default {
  name: "ReadingList",

  components: {
    RemoveSerieDialog,
    TableColumn,
  },

  data() {
    return {
      dialog: false,
      selectedRelease: 2,
      selected: [],
      sortBy: "tvshow_latest_date_added",
      sortDesc: true,
      search: "",
      headers: [
        { text: "Series", value: "tvshow_title" },
        { text: "Date", value: "tvshow_latest_date_added", width: "100" },
        { text: "My Status", value: "tvshow_release_number", width: "110" },
        { text: "Latest Release", value: "tvshow_latest_number", width: "140" },
      ],
    };
  },
  computed: {
    ...mapState(["serie_set", "account"]),
  },
  methods: {
    ...mapActions([
      "AccountReadinglist",
      "getAccountInfo",
      "AddReadinglist",
      "DeleteSerieFromReadingList",
    ]),
    updateSelected(variable) {
      this.selected = variable;
    },

    async RemoveSerieFromReadingList() {
      for (var i = 0; i <= this.selected.length - 1; i++) {
        await this.DeleteSerieFromReadingList(this.selected[i].id);
      }
      this.selected = [];
      await this.AccountReadinglist(this.account.id);
    },
    async AddList() {
      await this.AddReadinglist();
      await this.getAccountInfo();
      await this.AccountReadinglist(this.account.id);
    },
  },
  watch: {
    async account(account) {
      if (account) {
        await this.AccountReadinglist(this.account.id);
      }
    },
  },
};
</script>
