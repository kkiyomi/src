<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <Profilev2></Profilev2>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import Profilev2 from "../components/Profile/Profilev2.vue";

export default {
  name: "Profile",

  components: {
    Profilev2,
  },

  data() {
    return {};
  },
  computed: {},
  methods: {},
};
</script>
