<template>
  <div class="fill-height">
    <v-col cols="12" class="pb-1 store-title">민수네 국밥가게</v-col>
    <v-col cols="12" class="pt-0 store-rating-layout">
      <v-rating
        class="pr-3"
        v-model="rating"
        dense
        background-color="grey lighten-1"
        half-increments
        color="yellow darken-1">
      </v-rating>
      <span class="section-rating-num">3.7</span>
    </v-col>
    <v-col cols="12 section-notice section-notice-layout">
      <v-col cols="3" class="notice pa-0"><div>공지사항</div></v-col>
      <v-col cols="9" class="notice-content pa-0">
        <textarea class="textarea-layout" disabled>아프리카 돼지 열병 사태로 영업을 하지 않습니다.</textarea>
      </v-col>
    </v-col>
    <v-col class="section-none py-1">
    </v-col>
    <v-col cols="12 section-menu section-menu-layout">
      <v-col>정보</v-col>
      <v-col class="section-menu-center">메뉴</v-col>
      <v-col>설정</v-col>
    </v-col>
  </div>
</template>

<script>
export default {
  data () {
    return {
      rating: 3.7,
      infoToggle: false,
      menuToggle: false,
      settingToggle: false
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
.section-notice {
  height: 4rem;
}
.section-notice-layout {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
  display: flex;
  justify-content: center;
  align-items: center;
}
.section-none {
  background-color: #efefef
}
.section-menu {
  font-family: 'Noto Sans KR', sans-serif;
}
.section-menu-layout {
  border-bottom: solid 1px #dfdfdf;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
}
.section-menu-layout > div {
  display: flex;
  justify-content: center;
}
.section-menu-center {
  border-left: solid 1px #dfdfdf;
  border-right: solid 1px #dfdfdf;
}
.notice {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  font-weight: 700;
}
.notice-content {
  font-family: 'Noto Sans KR', sans-serif;
}
.textarea-layout {
  width: 100%;
}
</style>
