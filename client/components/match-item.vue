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
    async deleteMatch() {
      console.log('deleting')
      await $fetch(`http://localhost:8000/api/v1/matches/${this.match.id}/`, {
        method: 'delete'
      })
      this.$emit('delete', this.match.id)
    }
  }
}
</script>

<template>
  <v-card variant="outlined">
    <v-card-title class="d-flex align-center">
      {{ match.trigger }}
      <v-btn class="ml-auto" icon flat @click="deleteOverlay = true" size="xs">
        <v-icon>mdi-pencil</v-icon>
      </v-btn>

      <v-dialog v-model="deleteOverlay">
        <template v-slot:activator>
          <v-btn icon flat @click="deleteOverlay = true">
            <v-icon>mdi-trash-can</v-icon>
          </v-btn>
        </template>

        <template v-slot:default>
          <v-card>
            <v-card-text>
              <div>
                Do you really want to delete match with trigger {{ match.trigger }}?
              </div>
              <v-row no-gutters>
                <v-col>
                  <submit-btn block @click="deleteMatch" />
                </v-col>
                <v-col>
                  <cancel-btn block @click="deleteOverlay = false" />
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </template>

      </v-dialog>
    </v-card-title>
    <v-card-text>
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
