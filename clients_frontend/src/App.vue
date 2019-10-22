<template>
  <v-app class="white-bg">
  	<Header />
		<NavigationDrawer />
    <router-view class="mt-13" />
  </v-app>
</template>

<script>
import Header from './components/Common/Header'
import NavigationDrawer from './components/Common/NavigationDrawer'

export default {
  components: {
		Header,
		NavigationDrawer
  }
}
</script>

<style scoped>
.white-bg {
  background-color: white !important;
}
.mt-13 {
  margin-top: 56px;
}
</style>
