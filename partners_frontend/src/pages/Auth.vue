<template>
  <v-container fill-height>
    <SignIn/>
  </v-container>
</template>

<script>
import SignIn from '../components/Auth/SignIn'
import SignUp from '../components/Auth/SignUp'

export default {
  components: {
    SignIn,
    SignUp
  }
}
</script>

<style scoped>
.Noto-Sans-KR {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
