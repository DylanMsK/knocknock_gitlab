<template>
  <div>
    <div class="comment-layout mb-4">
      <div class="pa-5">
        <p class="comment-title mb-0">댓글 작성하기</p>
        <v-textarea>
        </v-textarea>
        <div class="fill-width btn-layout">
          <v-btn
            color="primary"
            dark
          >작성 완료</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.comment-arrow {
  display: flex;
  justify-content: center;
}
.comment-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.comment-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  font-weight: 700;
}
.btn-layout {
  display: flex;
  justify-content: flex-end;
}
</style>