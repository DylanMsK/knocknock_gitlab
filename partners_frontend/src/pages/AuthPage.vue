<template>
  <v-container fill-height>
    <SignIn/>
    <v-dialog v-model="signUpToggle" fullscreen hide-overlay transition="dialog-bottom-transition">
      <SignUp/>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

import SignIn from '../components/Auth/SignIn'
import SignUp from '../components/Auth/SignUp'

export default {
  components: {
    SignIn,
    SignUp
  },
  computed: {
    ...mapState('auth', ['signUpToggle'])
  },
  methods: {
    ...mapMutations('drawer', ['headerOnOff']),
    ...mapMutations('drawer', ['headerInit'])
  },
  created () {
    this.headerInit()
  },
  beforeDestroy: function () {
    this.headerOnOff()
  }
}
</script>

<style scoped>
.Noto-Sans-KR {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
