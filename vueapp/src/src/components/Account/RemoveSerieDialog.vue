<template>
  <div>
    <v-btn
      style="position: absolute; left: 10px; bottom: 10px"
      elevation="2"
      color="error"
      @click="dialog = true"
      text
    >
      Remove
    </v-btn>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="text-wrap">
          Are you sure you want to remove the selected from your list?
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click="RemoveSerieFromReadingList()">
            YES
          </v-btn>

          <v-btn text @click="dialog = false"> Cancel </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  name: "RemoveSerieDialog",
  props: ["selected"],

  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    ...mapState(["account"]),
    toDelete() {
      return this.selected;
    },
  },
  methods: {
    ...mapActions([
      "AccountReadinglist",
      "SerieDelete",
      "DeleteSerieFromReadingList",
    ]),
    async RemoveSerieFromReadingList() {
      for (var i = 0; i <= this.toDelete.length - 1; i++) {
        await this.DeleteSerieFromReadingList(this.toDelete[i].id);
      }
      this.$emit("RemoveFromReadingList", []);
      await this.AccountReadinglist(this.account.id);
      this.dialog = false;
    },
  },
};
</script>
