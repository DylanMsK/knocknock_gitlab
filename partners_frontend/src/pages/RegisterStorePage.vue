<template>
  <v-col>
    <div cols="12" class="register-head mb-4">영업장 등록</div>
    <div>
      <p class="register-title">상호 명</p>
      <v-text-field
        class="text-area-font"
      >
      </v-text-field>
    </div>
    상호, 성명, 사업장 주소, 등록번호, 캡처
  </v-col>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.register-head {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 60px;
  font-weight: 900;
}
.register-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.text-area-font {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>