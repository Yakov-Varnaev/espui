<template>
  <v-row no-gutters>
    <v-col>
      <submit-btn block @click="$emit('submit')" />
    </v-col>
    <v-col>
      <cancel-btn block @click="$emit('cancel')" />
    </v-col>
  </v-row>
</template>
