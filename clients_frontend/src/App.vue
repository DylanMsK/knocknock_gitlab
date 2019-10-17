<template>
  <v-app class="white-bg nanum-gothic-coding">
  <NavigationDrawer />
    <router-view />
  </v-app>
</template>

<script>
import NavigationDrawer from './components/Common/NavigationDrawer'
export default {
  components: {
    NavigationDrawer
  }
}
</script>

<style scoped>
.white-bg {
  background-color: white !important;
}
.nanum-gothic-coding {
  font-family: 'Nanum Gothic Coding', monospace !important;
}
</style>
