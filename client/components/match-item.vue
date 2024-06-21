<script>
export default {
  props: {
    match: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      deleteOverlay: false
    }
  },
  methods: {
    getColor() {
      return '#' + (Math.random() * 0xFFFFFF << 0).toString(16).padStart(6, '0');
    },
    deleteMatch(matchID) {
      this.$emit("delete", matchID)
    },
    updateMatch(match) {
      this.$emit("update", match)
    }
  }
}
</script>

<template>
  <v-card variant="outlined">
    <v-card-title class="d-flex align-center">
      {{ match.trigger }}
      <v-spacer />
      <match-edit-dialog :match="match" @update="updateMatch" />
      <match-delete-dialog :match="match" @delete="deleteMatch" />
    </v-card-title>
    <v-card-text>
      <div>
        <v-chip v-for="tag in match.tags" :key="tag" :color="getColor()" class="text-caption">
          {{ tag }}
        </v-chip>
      </div>
      <div>
        {{ match.replace }}
      </div>
      <div v-if="match.vars && match.vars.length" class="mt-2">
        <v-chip v-for="v in match.vars" class="mr-2">
          {{ v.name }}
        </v-chip>
      </div>
    </v-card-text>
  </v-card>
</template>
