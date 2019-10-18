<template>
  <v-col>
    <div class="info-head">
      <p class="info-title pr-4">가게 소개</p>
      <p class="info-modify">수정하기</p>
    </div>
    <p class="info-description">
      민수네 국밥가게는 돼지국밥, 순대국밥, 콩나물국밥 등 다양한 국밥을 판매하며, 한 숟가락 드실 시 든든~하고, 뜨뜻하게 하루를 보낼 수 있습니다. 만약, 조커가 국밥을 먹을 수 있었다면, 몸도 마음도 따뜻해져서 최악의 악당으로 되지 않았을겁니다.
    </p>
    <p class="info-title">사업자 정보</p>
    <div class="info-detail-category">
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">대표자명</v-col>
        <v-col cols="8">강민수</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">상호명</v-col>
        <v-col cols="8">민수네 국밥가게</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">사업자 주소</v-col>
        <v-col cols="8">서울특별시 강남구 역삼동 테헤란로38길 40-8</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">사업자 번호</v-col>
        <v-col cols="8">609-04-76324</v-col>
      </v-col>
    </div>
    <div class="info-head">
      <p class="info-title pr-4">영업 시간</p>
      <p class="info-modify">수정하기</p>
    </div>
    <div class="week-time">
      <p class="pb-2"><span class="info-tag">월요일 - </span>08:00 ~ 24:00</p>
      <p class="pb-2"><span class="info-tag">화요일 - </span>08:00 ~ 24:00</p>
      <p class="pb-2"><span class="info-tag">수요일 - </span>10:00 ~ 22:00</p>
      <p class="pb-2"><span class="info-tag">목요일 - </span>08:00 ~ 24:00</p>
      <p class="pb-2"><span class="info-tag">금요일 - </span>08:00 ~ 24:00</p>
      <p class="pb-2"><span class="info-tag">토요일 - </span>10:00 ~ 22:00</p>
      <p class="pb-2"><span class="sunday-time-text">일요일 - </span>10:00 ~ 22:00</p>
      <div class="break-time-text pb-2">
        <div class="icon-width">
          <v-icon class="icon-scale pr-2">fas fa-bed</v-icon>
        </div>
        <div>쉬는 시간 - 14:00 ~ 16:00</div>
      </div>
      <div class="last-order-text pb-2">
        <div class="icon-width">
          <v-icon class="icon-scale pr-2">fas fa-clipboard-list</v-icon>
        </div>
        <div>마지막 주문 - 마감 1시간 전</div>
      </div>
    </div>
    <div class="info-head">
      <p class="info-title pr-4">매장 정보</p>
      <p class="info-modify">수정하기</p>
    </div>

    <div class="info-detail-category">
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">연락처</v-col>
        <v-col cols="8">010-5191-0337</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">주차</v-col>
        <v-col cols="8" class="impossible-text">불가</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">배달</v-col>
        <v-col cols="8" class="impossible-text">불가</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">포장</v-col>
        <v-col cols="8" class="impossible-text">불가</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">예약</v-col>
        <v-col cols="8" class="possible-text">가능</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">단체석</v-col>
        <v-col cols="8">12인 이상</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">가격대</v-col>
        <v-col cols="8">10,000원 ~ 25,000원</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">네이버 리뷰 수</v-col>
        <v-col cols="8">7,302개</v-col>
      </v-col>
      <v-col cols="12" class="info-detail pb-2">
        <v-col cols="4" class="info-tag">조회수</v-col>
        <v-col cols="8">25,234회</v-col>
      </v-col>
    </div>
  </v-col>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.info-head {
  display: flex;
  align-items: flex-end;
}
.info-modify {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  color: #0091EA;
}
.info-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.info-description {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  color: #a9a9a9;
}
.week-time {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  color: #a9a9a9;
  margin-bottom: 16px;
}
.week-time > p {
  margin-bottom: 0px;
}
.sunday-time-text {
  color: #D50000;
}
.break-time-text {
  color: #00BFA5;
  display: flex;
}
.last-order-text {
  color: #00BFA5;
  display: flex;
}
.icon-scale {
  transform: scale(0.8)
}
.icon-width {
  display: flex;
  justify-content: center;
  width: 40px;
}
.info-detail-category {
  font-family: 'Noto Sans KR', sans-serif;
  margin-bottom: 16px;
}
.info-detail {
  display: flex;
  padding: 0px;
  color: #a9a9a9;
}
.info-detail > div {
  padding: 0px;
}
.info-tag  {
  color: black;
}
.possible-text {
  color:#0091EA;
}
.impossible-text {
  color:#D50000
}
</style>
