<template>
  <div class="fill-height">
    <v-col cols="12" class="store-title store-title-layout">영업장 관리</v-col>
    <v-col cols="12" class="section-top">
      <v-col cols="4" class="pa-0"><v-img class="img" src="../assets/image/test.jpg"></v-img></v-col>
      <v-col cols="8" class="pa-0 section-font">
        <div class="section-title">
          <h3>민수네 국밥가게</h3>
          <v-icon>fas fa-utensils</v-icon>
        </div>
      </v-col>
    </v-col>

    <!-- 이 부분부터 for문으로 처리 -->
    <v-col cols="12" class="section">
      <v-col cols="4" class="pa-0"><v-img class="img" src="../assets/image/test2.jpg"></v-img></v-col>
      <v-col cols="8" class="pa-0 section-font">
        <div class="section-title">
          <h3>동훈의 디카페인</h3>
          <v-icon>fas fa-coffee</v-icon>
        </div>
      </v-col>
    </v-col>
    <!-- 여기까지 for문으로 처리 -->

    <v-col cols="12" class="section-bottom">
      <v-col cols="12" class="section-bottom-inner section-bottom-text">
        <v-icon class="icon-color">fas fa-plus</v-icon>
        <h3>영업장을 추가하세요.</h3>
      </v-col>
    </v-col>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.store-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.store-title-layout {
  margin-bottom: 2rem;
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
.icon-color {
  color: #c1c1c1;
}
.section-bottom-text > h3 {
  padding-left: 15px;
}
.img {
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
</style>
