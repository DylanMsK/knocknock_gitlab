<template>
  <v-app class="white-bg">
    <v-container class="nanum-gothic-coding">
      <router-view />
    </v-container>
  </v-app>
</template>

<style scoped>
.white-bg {
  background-color: white !important;
}
.nanum-gothic-coding {
  font-family: 'Nanum Gothic Coding', monospace !important;
}
</style>
