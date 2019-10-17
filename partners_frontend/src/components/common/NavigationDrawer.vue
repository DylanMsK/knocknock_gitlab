<template>
  <v-navigation-drawer
    width="100%"
    v-model="drawerToggle"
    absolute
  >
    <div class="flex menu-header">
      <v-col cols="10">
        <p class="menu-title mb-0">메뉴</p>
      </v-col>
      <v-col cols="2" @click="drawerOnOff()">
        <p class="menu-text">닫기</p>
      </v-col>
    </div>
    <div class="flex">
      <v-col class="center block-one" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-store</v-icon></div>
        <div class="pa-1 menu-text">영업장</div>
      </v-col>
      <v-col class="center block-two" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-user-alt</v-icon></div>
        <div class="pa-1 menu-text">프로필</div>
      </v-col>
      <v-col class="center block-three" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-comments</v-icon></div>
        <div class="pa-1 menu-text">리뷰 관리</div>
      </v-col>
    </div>
    <!-- <div class="flex">
      <v-col class="center block-four" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-store</v-icon></div>
        <div class="pa-1 menu-text">영업장</div>
      </v-col>
      <v-col class="center block-five" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-user-alt</v-icon></div>
        <div class="pa-1 menu-text">프로필</div>
      </v-col>
      <v-col class="center block-six" cols="4">
        <div class="pa-3"><v-icon class="icon">fas fa-phone-alt</v-icon></div>
        <div class="pa-1 menu-text">1:1 문의</div>
      </v-col>
    </div> -->
    <v-col class="footer menu-font fill-width">
      <p class="center mb-2">연중무휴 고객센터 <span class="pl-4 menu-text">010-5191-0337</span></p>
      <p class="center mb-0 footer-text">Copyright Hey & Nerd in Gang-Nam, All Rights Reserved.</p>
    </v-col>
  </v-navigation-drawer>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      items: [
        { title: '영업장 관리', icon: 'fas fa-store' },
        { title: 'Account', icon: 'fas fa-lock' },
        { title: 'Admin', icon: 'fas fa-lock' }
      ]
    }
  },
  computed: {
    drawerToggle: {
      get() {
        return this.$store.state.drawer.drawerToggle
      },
      set() {
        return
      }
    }
  },
  methods: {
    ...mapMutations('drawer', ['drawerOnOff'])
  }
}
</script>

<style scoped>
.menu-font {
  font-family: 'Noto Sans KR', sans-serif;
  color: #7b7b7b;
}
.menu-text {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
  color: black;
}
.center {
  display: flex;
  justify-content: center !important;
}
.center > div {
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
  font-size: 7px;
}
</style>
