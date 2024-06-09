<script>
export default {
  props: {
    isEdit: {
      type: Boolean,
      required: false,
      default: false,
    },
    match: {
      type: Object,
      required: false,
      default: () => ({
        trigger: '',
        replace: '',
        vars: []
      })
    }
  },
  methods: {
    async saveMatch() {
      const data = await $fetch('http://localhost:8000/api/v1/matches/', {
        method: 'POST',
        body: this.currentMatch
      })
    },
    async submit() {
      if (this.isEdit) {
      } else {
        await this.saveMatch()
      }
      this.$emit('close', this.currentMatch)
    },
    addVar() {
      this.currentMatch.vars = [{ name: '', type: '', params: [] }, ...this.currentMatch.vars]
    },
    removeVar(idx) {
      this.currentMatch.vars.splice(idx, 1)
    }
  },
  data() {
    let initialMatch = { ...this.match }
    let currentMatch = { ...this.match }
    return {
      initialMatch, currentMatch,
    }
  }
}
</script>

<template>
  <v-card>
    <v-card-text>
      <v-text-field label="trigger" v-model="currentMatch.trigger" variant='outlined' />
      <v-textarea label="replace" v-model="currentMatch.replace" variant='outlined' />

      <div class="d-flex align-center justify-space-between">
        <span>Variables</span>
        <v-btn class="ml-auto" icon flat size="xs" @click="addVar"><v-icon>mdi-plus-circle-outline</v-icon></v-btn>
      </div>

      <v-divider class="mt-2" />

      <div class="d-flex mt-2 align-center" v-for="(v, idx) in currentMatch.vars.entries()" :key="idx">
        <v-text-field label="name" v-model="currentMatch.vars[idx].name" variant='outlined' density='compact'
          class="mr-2 mt-4" />
        <v-text-field label="type" v-model="currentMatch.vars[idx].type" variant='outlined' density='compact'
          class="mr-2 mt-4" />
        <v-btn icon flat size="xs" class="ma-0" @click="removeVar(idx)"><v-icon>mdi-close</v-icon></v-btn>
      </div>

    </v-card-text>
    <v-card-actions>
      <form-buttons @cancel="$emit('cancel')" @submit="submit" />
    </v-card-actions>
  </v-card>
</template>
