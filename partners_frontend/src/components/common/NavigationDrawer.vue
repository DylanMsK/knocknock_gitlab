<template>
  <v-navigation-drawer
    class="top-index"
    width="100%"
    :value="drawerToggle"
    absolute
  >
    <div class="flex menu-header">
      <v-col cols="10">
        <p class="menu-title mb-0">메뉴</p>
      </v-col>
      <v-col cols="2">
        <p class="menu-text" @click="drawerOnOff()">닫기</p>
      </v-col>
    </div>
    <div class="flex">
      <v-col class="menu-inner block-one" cols="4" @click="goToStore()">
        <div class="pa-3"><v-icon class="icon">fas fa-store</v-icon></div>
        <div class="pa-1 menu-text">영업장</div>
      </v-col>
      <v-col class="menu-inner block-two" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-comments</v-icon></div>
        <div class="pa-1 menu-text">리뷰 관리</div>
      </v-col>
      <v-col class="menu-inner block-three" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-user-alt</v-icon></div>
        <div class="pa-1 menu-text">프로필</div>
      </v-col>
    </div>
    <div class="flex">
      <v-col class="menu-inner block-four" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-wrench</v-icon></div>
        <div class="pa-1 menu-text">공사 중</div>
      </v-col>
      <v-col class="menu-inner block-five" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-wrench</v-icon></div>
        <div class="pa-1 menu-text">공사 중</div>
      </v-col>
      <v-col class="menu-inner block-six" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-wrench</v-icon></div>
        <div class="pa-1 menu-text">공사 중</div>
      </v-col>
    </div>
    <v-col class="footer footer-text fill-width">
      <p class="center mb-2">연중무휴 고객센터 <span class="pl-4 menu-text">010-5191-0337</span></p>
      <p class="center mb-0 footer-info">Copyright Hey & Nerd in Gang-Nam, All Rights Reserved.</p>
    </v-col>
  </v-navigation-drawer>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
import router from '../../router'

export default {
  computed: {
    ...mapState('drawer', ['drawerToggle'])
  },
  methods: {
    ...mapMutations('drawer', ['drawerOnOff']),
    goToStore () {
      this.drawerOnOff()
      router.push('/store').catch(err => {
        console.log('이미 같은 페이지입니다.')
      })
    }
  }
}
</script>

<style scoped>
.top-index {
  z-index: 2;
}
.menu-text {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
  color: black;
}
.menu-inner > div {
  display: flex;
  justify-content: center;
}
.center {
  display: flex;
  justify-content: center;
}
.icon {
  color: black;
}
.menu-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.menu-header {
  margin-bottom: 5rem;
}
.flex {
  display: flex;
}
.block-one {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
  border-right: solid 1px #dfdfdf;
}
.block-two {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
}
.block-three {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
  border-left: solid 1px #dfdfdf;
}
.block-four {
  border-bottom: solid 1px #dfdfdf;
  border-right: solid 1px #dfdfdf;
}
.block-five {
  border-bottom: solid 1px #dfdfdf;
}
.block-six {
  border-bottom: solid 1px #dfdfdf;
  border-left: solid 1px #dfdfdf;
}
.footer {
  position: absolute;
  bottom: 12px;
}
.footer-text {
  font-family: 'Noto Sans KR', sans-serif;
  color: #7b7b7b;
}
.footer-info {
  font-size: 7px;
}
</style>
