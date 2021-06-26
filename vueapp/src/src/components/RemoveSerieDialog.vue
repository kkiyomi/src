<template>
  <div>
    <v-btn
      style="position: absolute; left: 10px; bottom: 10px"
      elevation="2"
      color="error"
      v-if="selectedRL.length !== 0"
      @click="remove"
      text
    >
      Remove
    </v-btn>
    <v-dialog v-model="dialog" max-width="550">
      <v-card>
        <v-card-title class="headline">
          Are you sure you want to remove the selected from your list?
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text @click="dialog = false"> YES </v-btn>

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
  props: ["selectedRL"],

  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    ...mapState(["serie_set", "globalKey"]),
  },
  methods: {
    ...mapActions(["AccountReadinglist", "SerieDelete"]),
    remove() {
      this.dialog = !this.dialog;
      for (var i = 0; i <= this.selectedRL.length - 1; i++) {
        const isLargeNumber = (element) =>
          element && element.id === this.selectedRL[i].id;
        this.SerieDelete(this.selectedRL[i].id);
        const ind = this.serie_set.findIndex(isLargeNumber);
        delete this.serie_set[ind];
      }
      this.selectedRL = [];
    },
  },
};
</script>
