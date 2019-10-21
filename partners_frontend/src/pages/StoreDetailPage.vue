<template>
  <div class="fill-height">
    <v-col cols="12" class="pb-1 store-title">민수네 국밥가게</v-col>
    <v-col cols="12" class="pt-0 store-rating-layout">
      <v-rating
        class="pr-3"
        v-model="rating"
        readonly
        dense
        background-color="grey lighten-1"
        half-increments
        color="yellow darken-1">
      </v-rating>
      <span class="section-rating-num">3.7</span>
    </v-col>
    <v-col cols="12">
      <v-col cols="12" class="notice px-0 pt-0 pb-2">
        <div>공지사항</div><div class="post-modify-button" @click="postBox()">공지사항 수정하기</div>
      </v-col>
      <postTextBox
        v-show="textBox"
      />
      <v-col class="pa-0 notice-content">
        <div v-show="!textBox">{{ postContent }}</div>
      </v-col>
    </v-col>
    <v-col class="section-none py-1">
    </v-col>
    <v-col cols="12 pa-0 section-menu section-menu-layout">
      <v-col v-bind:style="[infoToggle ? choicedMenu : justMenu]" @click="changeToggle('info')">정보</v-col>
      <v-col v-bind:style="[menuToggle ? choicedMenu : justMenu]" @click="changeToggle('menu')" class="section-menu-center">메뉴</v-col>
      <v-col v-bind:style="[reviewToggle ? choicedMenu : justMenu]" @click="changeToggle('review')">리뷰</v-col>
    </v-col>
    <InfoDetail v-show="infoToggle"/>
    <MenuDetail v-show="menuToggle"/>
    <reviewDetail v-show="reviewToggle"/>
  </div>
</template>

<script>
import InfoDetail from '../components/Detail/infoDetail'
import MenuDetail from '../components/Detail/menuDetail'
import reviewDetail from '../components/Detail/reviewDetail'
import postTextBox from '../components/Detail/postTextBox'

import { mapState } from 'vuex'

export default {
  components: {
    InfoDetail,
    MenuDetail,
    reviewDetail,
    postTextBox
  },
  data () {
    return {
      rating: 3.7,
      infoToggle: true,
      menuToggle: false,
      reviewToggle: false,
      textBox: false,
      choicedMenu: {
        fontWeight: 700,
        fontSize: '18px'
      },
      justMenu: {
        borderBottom: 'solid 1px #dfdfdf',
        fontSize: '16px'
      }
    }
  },
  computed: {
    ...mapState('postText', ['postContent'])
  },
  methods: {
    postBox () {
      this.textBox = !this.textBox
    },
    changeToggle (check) {
      if (check === 'info') {
        this.infoToggle = true
        this.menuToggle = false
        this.reviewToggle = false
      } else if (check === 'menu') {
        this.infoToggle = false
        this.menuToggle = true
        this.reviewToggle = false
      } else {
        this.infoToggle = false
        this.menuToggle = false
        this.reviewToggle = true
      }
    }
  }
}
</script>

<style scoped>
.store-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 40px;
  font-weight: 900;
}
.store-rating-layout {
  display: flex;
  align-items: center;
}
.section-rating-num {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 700;
  font-size: 18px;
}
.section-none {
  background-color: #efefef
}
.post-modify-button {
  color: #0091EA;
  font-weight: 500;
}
.section-menu {
  font-family: 'Noto Sans KR', sans-serif;
}
.section-menu-layout {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
}
.section-menu-layout > div {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.section-menu-center {
  border-left: solid 1px #dfdfdf;
  border-right: solid 1px #dfdfdf;
}
.notice {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  font-weight: 700;
  display: flex;
  justify-content: space-between;
}
.notice-content {
  font-family: 'Noto Sans KR', sans-serif;
}
.textarea-layout {
  width: 100%;
}
</style>
