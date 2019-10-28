<template>
  <div class="fill-height">
    <v-col cols="12" class="store-title">영업장 관리</v-col>
    <v-col class="info-text pt-0">사진을 눌러서 <span class="open-text">영업 중 </span>/<span class="close-text"> 영업 마감</span>을 관리하세요.</v-col>
    <v-col v-for="store in allStores.data" :key="store.id" cols="12" class="section-top">
      <v-col cols="4" class="pa-0">
        <v-img v-if="store.thumbnail" :style="[openCloseToggle ? openImg : closeImg]" :src="store.thumbnail" @click="openClose()"></v-img>
        <v-img v-else :style="[openCloseToggle ? openImg : closeImg]" src="../assets/image/noneThumbnail.png" @click="openClose()"></v-img>
      </v-col>
      <v-col cols="8" class="pa-0 section-font" @click="goToDetail(store.id)">
        <div class="section-title section-title-layout pb-2">
          <h3>{{ store.name }}</h3>
          <v-icon class="icon-size">fas fa-utensils</v-icon>
        </div>
        <div class="section-detail-layout pb-1">
          <v-icon class="pr-2" color="yellow darken-1" small>fas fa-star</v-icon>
          <span class="section-detail-rating pr-1">3.7</span><span class="section-detail-rating-count">(+10)</span>
        </div>
        <div class="section-detail-layout">
          <span class="section-detail-new-comment pr-1">새로 등록된 댓글</span><span class="section-detail-new-comment-count pl-1">5</span>
        </div>
        <div v-show="!openCloseToggle">
          <span class="section-close-text pr-2">영업 마감</span><v-icon class="icon-size">fas fa-door-closed</v-icon>
        </div>
        <div v-show="openCloseToggle">
          <span class="section-open-text pr-2">영업 중</span><v-icon class="icon-size">fas fa-door-open</v-icon>
        </div>
      </v-col>
    </v-col>

    <!-- 이 부분부터 for문으로 처리 -->
    <v-col cols="12" class="section">
      <v-col cols="4" class="pa-0"><v-img v-bind:style="[openCloseToggle ? openImg : closeImg]" src="../assets/image/test2.jpg"></v-img></v-col>
      <v-col cols="8" class="pa-0 section-font">
        <div class="section-title section-title-layout pb-2">
          <h3>동훈의 디카페인</h3>
          <v-icon class="icon-size">fas fa-coffee</v-icon>
        </div>
        <div class="section-detail-layout pb-1">
          <v-icon class="pr-2" color="yellow darken-1" small>fas fa-star</v-icon>
          <span class="section-detail-rating pr-1">4.2</span><span class="section-detail-rating-count">(+20)</span>
        </div>
        <div class="section-detail-layout">
          <span class="section-detail-new-comment pr-1">새로 등록된 댓글</span><span class="section-detail-new-comment-count-none pl-1">0</span>
        </div>
        <div>
          <div v-show="!openCloseToggle">
            <span class="section-close-text pr-2">영업 마감</span><v-icon class="icon-size">fas fa-door-closed</v-icon>
          </div>
          <div v-show="openCloseToggle">
            <span class="section-open-text pr-2">영업 중</span><v-icon class="icon-size">fas fa-door-open</v-icon>
          </div>
        </div>
      </v-col>
    </v-col>
    <!-- 여기까지 for문으로 처리 -->

    <v-col cols="12" class="section-bottom">
      <v-col cols="12" class="section-bottom-inner section-bottom-text" @click="goToRegister()">
        <v-icon class="icon-color">fas fa-plus</v-icon>
        <h3>영업장을 추가하세요.</h3>
      </v-col>
    </v-col>
  </div>
</template>

<script>
import router from '../router'
import { mapState, mapActions } from 'vuex'

export default {
  data () {
    return {
      openCloseToggle: false,
      closeImg: {
        borderRadius: '50%',
        height: '100px',
        width: '100px',
        filter: 'brightness(50%)'
      },
      openImg: {
        borderRadius: '50%',
        height: '100px',
        width: '100px'
      }
    }
  },
  async created () {
    await this.getAllStores()
  },
  computed: {
    ...mapState('store', ['allStores'])
  },
  methods: {
    ...mapActions('store', ['getAllStores']),
    goToDetail (id) {
      router.push('/store/' + id)
    },
    goToRegister () {
      router.push('/store/register')
    },
    openClose () {
      this.openCloseToggle = !this.openCloseToggle
    }
  }
}
</script>

<style scoped>
.store-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.section-title-layout {
  display: flex;
  align-items: center;
}
.section-top {
  border-top: solid 1px #dfdfdf;
  border-bottom: solid 1px #dfdfdf;
  height: 10rem;
  display: flex;
  align-items: center;
}
.section {
  border-bottom: solid 1px #dfdfdf;
  height: 10rem;
  display: flex;
  align-items: center;
}
.section-bottom {
  height: 10rem;
  display: flex;
  align-items: center;
}
.section-bottom-inner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  border: dashed 2px #c1c1c1;
  border-radius: 3%;
}
.section-font {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
}
.section-font > h3 {
  font-weight: 900;
}
.section-title {
  display: flex;
}
.section-title > h3 {
  padding-right: 15px;
}
.section-bottom-text {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
  color: #c1c1c1;
}
.section-detail-layout {
  display: flex;
  align-items: center;
}
.icon-color {
  color: #c1c1c1;
}
.icon-size {
  transform: scale(0.9)
}
.section-bottom-text > h3 {
  padding-left: 15px;
}
.section-detail-rating {
  font-size: 13px;
}
.section-detail-rating-count {
  font-size: 13px;
  color: #c1c1c1;
  font-weight: 500;
}
.section-detail-new-comment {
  font-size: 13px;
  font-weight: 500;
}
.section-detail-new-comment-count {
  font-size: 13px;
  color: #D50000;
  font-weight: 500;
}
.section-detail-new-comment-count-none {
  font-size: 13px;
  color: #c1c1c1;
  font-weight: 500;
}
.info-text {
  font-family: 'Noto Sans KR', sans-serif;
}
.open-text {
  font-weight: 500;
  color: #0091EA;
}
.close-text {
  font-weight: 500;
  color: #D50000;
}
.section-open-text {
  font-weight: 500;
  color: #0091EA;
  font-size: 13px;
}
.section-close-text {
  font-weight: 500;
  color: #D50000;
  font-size: 13px;
}
</style>
