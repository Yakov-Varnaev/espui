<script>
export default {
  props: {
    match: {
      type: Object,
      required: true,
    }
  },
}
</script>

<template>
  <v-card variant="outlined">
    <v-card-title>{{ match.trigger }}</v-card-title>
    <v-card-text>
      <div>
        {{ match.replace }}
      </div>
      <div>
      </div>
    </v-card-text>
    <v-card-actions v-if="match.vars">
      <v-chip v-for="v in match.vars" class="mr-2">
        {{ v.name }}
      </v-chip>
    </v-card-actions>
  </v-card>
</template>
