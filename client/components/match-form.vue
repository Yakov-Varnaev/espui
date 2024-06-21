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
        tags: [],
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
      return data
    },
    async updateMatch() {
      const data = await $fetch(`http://localhost:8000/api/v1/matches/${this.currentMatch.id}/`, {
        method: 'PUT',
        body: this.currentMatch,
      })
      return data
    },
    async submit() {
      if (this.isEdit) {
        let respData = await this.updateMatch()
        this.$emit('update', respData)
      } else {
        let respData = await this.saveMatch()
        this.$emit('close', respData)
      }
    },
    addVar() {
      this.currentMatch.vars = [{ name: '', type: '', params: [] }, ...this.currentMatch.vars]
    },
    removeVar(idx) {
      this.currentMatch.vars.splice(idx, 1)
    }
  },
  data() {
    let initialMatch = JSON.parse(JSON.stringify(this.match))
    let currentMatch = JSON.parse(JSON.stringify(this.match))

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
      <form-buttons @cancel="$emit('cancel')" @close="$emit('close')" @submit="submit" submitText="Save" />
    </v-card-actions>
  </v-card>
</template>
