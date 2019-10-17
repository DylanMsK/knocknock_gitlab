<template>
  <v-container fill-height>
    <Signin />
    <Signup />
  </v-container>
</template>

<script>
import Signin from '../components/Auth/Signin'
import Signup from '../components/Auth/Signup'

export default {
  components: {
    Signin,
    Signup
  }
}
</script>
