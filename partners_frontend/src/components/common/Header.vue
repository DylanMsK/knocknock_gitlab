<template>
  <div>
    <v-app-bar>
      <v-app-bar-nav-icon
        @click="drawerOnOff()"
      ></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <div class="user-text">유저이름</div>
    </v-app-bar>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapState('drawer', ['drawerToggle'])
  },
  methods: {
    ...mapMutations('drawer', ['drawerOnOff'])
  }
}
</script>

<style scoped>
.user-text {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 500;
}
</style>
