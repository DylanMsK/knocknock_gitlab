<template>
  <v-container fill-height>
    <Signin />
    <Signup
      @turnToggle="snackBar=true"
      @turnToggleError="signUpErrorSnackBar=true"
    />
    <v-snackbar
      class="Noto-Sans-KR"
      color="#0091EA"
      :timeout="1500"
      v-model="snackBar"
      top
    >
      회원가입이 완료되었습니다!!
      <v-btn
        @click="snackBar=false"
        text
      >
        닫기
      </v-btn>
    </v-snackbar>
    <v-snackbar
      class="Noto-Sans-KR"
      color="#D32F2F"
      :timeout="1500"
      v-model="signUpErrorSnackBar"
      top
    >
      이미 존재하는 이메일입니다.
    </v-snackbar>
  </v-container>
</template>

<script>
import Signin from '../components/Auth/Signin'
import Signup from '../components/Auth/Signup'
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      snackBar: false,
      signUpErrorSnackBar: false
    }
  },
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
