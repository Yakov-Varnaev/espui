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
    addMatch(match) {
      console.log(match)
      this.matches.splice(0, 0, match)
    },
    deleteMatch(matchId) {
      this.matches = this.matches.filter((m) => m.id !== matchId);
    },
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
    <div class="d-flex align-center justify-center">
      <v-text-field label="Search" v-model="query" variant="outlined" class="mr-2 mt-5 pa-0" />
      <match-overlay @addMatch="addMatch" />
    </div>
    <v-divider />
    <v-list>
      <match-item v-for="match in matches" :match="match" class="mt-3" @delete="deleteMatch" />
    </v-list>
  </div>
</template>
