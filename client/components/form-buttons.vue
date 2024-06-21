<script>
export default {
  props: {
    submitText: {
      required: false,
      type: String,
      default: "Submit",
    },
    cancelText: {
      required: false,
      type: String,
      default: "Cancel",
    }

  }
}
</script>

<template>
  <v-row no-gutters>
    <v-col>
      <submit-btn block :text="this.submitText" @click="$emit('submit')" />
    </v-col>
    <v-col>
      <cancel-btn block :text="this.cancelText" @click="$emit('cancel')" />
    </v-col>
  </v-row>
</template>
