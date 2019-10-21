<template>
  <div>
    <div class="review-comment-layout">
      <v-col cols="1" class=""></v-col>
      <v-col cols="11" class="partners pa-0">사장님 댓글</v-col>
    </div>
    <div class="review-comment-layout">
      <v-col cols="1" class="pa-0">
        <v-icon class="icon-transform" small>fas fa-reply</v-icon>
      </v-col>
      <v-col cols="11" class="pa-0 partners-comment">
        잘 드셨다고하니 제가 다 든든~하네요. 감사합니다.
      </v-col>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.partners {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.partners-comment {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 16px;
  font-weight: 500;
}
.icon-transform {
  transform: rotate(-180deg)
}
.review-comment-layout {
  display: flex;
}
</style>