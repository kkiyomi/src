<template>
  <span>
    {{ result }}
  </span>
</template>

<script>
export default {
  name: 'TableColumn',
  props: ['date_added'],

  data () {
    return {
    }
  },
  computed: {
    result () {
      return this.date_added.split('T')[0]
    },
  },
  methods: {
  }
}
</script>
