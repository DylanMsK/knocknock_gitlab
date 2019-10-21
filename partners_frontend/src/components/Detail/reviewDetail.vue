<template>
  <v-col>
    <div class="review-detail-category">
      <p class="review-id mb-0">
        <span>이**님</span>
        <span class="pl-2 review-date">2019-10-21</span>
        <span class="review-button" @click="textBox()">
          <v-icon class="ml-2" color="#0091EA " small>far fa-comment</v-icon>
          <span class="ml-1 review-content-button">댓글달기</span>
        </span>
      </p>
      <p class="review-layout-flex mb-2">
        <span class="review-menu pr-2">돼지국밥</span>
        <v-rating
          small
          v-model="rating"
          readonly
          dense
          background-color="grey lighten-1"
          half-increments
          color="yellow darken-1">
        </v-rating>
      </p>
      <p class="review-content">술 먹고 다음 날 아침에 민수네 국밥 한 그릇 먹으면 하루를 든든~하게 시작 할 수 있습니다.</p>
      <reviewTextBox
        v-show="textBoxToggle"
      />
      <reviewComment/>
    </div>
  </v-col>
</template>

<script>
import reviewComment from './reviewComment'
import reviewTextBox from './reviewTextBox'

export default {
  components: {
    reviewComment,
    reviewTextBox
  },
  data () {
    return {
      rating: 3.7,
      textBoxToggle: false
    }
  },
  methods: {
    textBox () {
      this.textBoxToggle = !this.textBoxToggle
    }
  }
}
</script>

<style scoped>
.review-id {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.review-detail-category {
  font-family: 'Noto Sans KR', sans-serif;
  margin-bottom: 16px;
}
.review-date {
  font-size: 14px;
  font-weight: 500;
  color: #afafaf
}
.review-layout-flex {
  display: flex;
  align-items: flex-end;
}
.review-menu {
  font-size: 14px;
  font-weight: 500;
  color: #00BFA5;
}
.review-content-button {
  font-size: 14px;
  font-weight: 500;
}
.review-button {
  color: #0091EA;
}
</style>
