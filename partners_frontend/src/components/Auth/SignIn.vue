<template>
  <v-row>
    <v-col cols="12">
      <p class="login-font mb-0">낰낰</p>
    </v-col>
    <v-col cols="12">
      <v-text-field
        class="Noto-Sans-KR"
        label="이메일"
        outlined
        rounded
        clearable
      ></v-text-field>
      <v-text-field
        class="Noto-Sans-KR"
        label="비밀번호"
        type="password"
        outlined
        rounded
        clearable
      ></v-text-field>
    </v-col>
    <v-col class="center pt-0" cols="12">
      <v-btn class="Noto-Sans-KR" x-large color="primary">로그인 하기</v-btn>
    </v-col>
    <v-col class="Noto-Sans-KR center bottom-position fill-width">
      낰낰의 계정이 없으신가요?<a class="bold-signup-font px-3">회원가입</a>
    </v-col>
  </v-row>
</template>

<script>
export default {
  
}
</script>

<style>
.login-font {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 72px;
  font-weight: 900;
}
.Noto-Sans-KR {
  font-family: 'Noto Sans KR', sans-serif;
}
.center {
  display: flex;
  justify-content: center;
}
.bottom-position {
  position: absolute;
  bottom: 12px;
}
.bold-signup-font {
  font-weight: 600;
}
</style>
