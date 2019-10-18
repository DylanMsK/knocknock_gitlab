<template>
  <v-container fill-height>
    <Signin />
    <Signup />
  </v-container>
</template>

<script>
import Signin from '../components/Auth/Signin'
import Signup from '../components/Auth/Signup'
import { mapMutations } from 'vuex'

export default {
  components: {
    Signin,
    Signup
  },
  mounted () {
    this.toggleHeader(false)
  },
  methods: {
    ...mapMutations('toggle', ['toggleHeader'])
  }
}
</script>
