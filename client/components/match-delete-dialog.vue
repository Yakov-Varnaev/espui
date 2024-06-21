<script>
export default {
  props: {
    match: {
      required: true,
      type: Object,
    }
  },
  methods: {
    async deleteMatch() {
      try {
        const data = await $fetch(
          `http://localhost:8000/api/v1/matches/${this.match.id}/`,
          {
            method: 'delete',
            body: this.currentMatch
          }
        )
        this.$emit("delete", data)
      } catch (e) {
        console.log(e)
      }
      this.overlay = false
    }
  },
  data() {
    return {
      overlay: false
    }
  }
}
</script>

<template>
  <v-dialog v-model="overlay" cols="4">
    <template v-slot:activator>
      <v-btn icon flat @click="overlay = true">
        <v-icon>mdi-trash-can</v-icon>
      </v-btn>
    </template>

    <template v-slot:default>
      <v-card>
        <v-card-text>
          <div>
            Do you really want to delete match with trigger
            <span class="font-weight-black">{{ match.trigger }}</span>?
          </div>
          <form-buttons submitText="Delete" @submit="deleteMatch" @cancel="overlay = false" />
        </v-card-text>
      </v-card>
    </template>
  </v-dialog>
</template>
