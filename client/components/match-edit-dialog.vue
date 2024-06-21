<script>
export default {
  props: {
    match: {
      required: true,
      type: Object,
    }
  },
  methods: {
    closeOverlay() {
      this.overlay = false
    },
    updateMatch(data) {
      console.log('update dia')
      this.closeOverlay()
      this.$emit('update', data)
    }
  },
  data() {
    return {
      overlay: false,
    }
  }
}
</script>

<template>
  <v-dialog v-model="overlay">
    <template v-slot:activator>
      <v-btn icon flat @click="overlay = true">
        <v-icon>mdi-pencil</v-icon>
      </v-btn>
    </template>

    <template v-slot:default>
      <match-form @cancel="closeOverlay" @update="updateMatch" :isEdit="true" :match="match" />
    </template>
  </v-dialog>
</template>
