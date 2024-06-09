<script>
export default {
  data() {
    return {
      query: '',
      matches: []
    }
  },
  watch: {
    query(newValue) {
      this.query = newValue
      this.fetchMatches()
    }
  },
  methods: {
    async fetchMatches() {
      let query = {}
      if (this.query) {
        query.query = this.query
      }
      const data = await $fetch(
        'http://localhost:8000/api/v1/matches/', { query }
      )
      this.matches = data
    }
  },
  async mounted() {
    await this.fetchMatches()
  }
}
</script>

<template>
  <div>
    <v-text-field label="Search" v-model="query" />
    <v-list>
      <match-item v-for="match in matches" :match="match" class="mt-3" />
    </v-list>
  </div>
</template>
