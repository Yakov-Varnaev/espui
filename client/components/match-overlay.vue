<script>
export default {
  methods: {
    closeOverlay(data) {
      this.overlay = false
      if (data) {
        this.$emit('addMatch', data)
      }
    },
  },
  data() {
    return {
      overlay: false,
    }
  }
}
</script>

<template>
  <v-dialog max-width="500" v-model="overlay">
    <template v-slot:activator>
      <v-btn variant='outlined' icon @click="overlay = true">
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </template>

    <template v-slot:default="{ isActive }">
      <match-form @cancel="closeOverlay" @close="closeOverlay" />
    </template>
  </v-dialog>
</template>
