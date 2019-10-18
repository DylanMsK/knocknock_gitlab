  <template>
    <v-col>
      <p class="menu-title">메뉴</p>
      <div class="menu-detail-category">
        <v-col cols="12" class="menu-detail pb-2">
          <v-col cols="4" class="menu-tag">돼지국밥</v-col>
          <v-col cols="8">7,500원</v-col>
        </v-col>
        <v-col cols="12" class="menu-detail pb-2">
          <v-col cols="4" class="menu-tag">순대국밥</v-col>
          <v-col cols="8">7,500원</v-col>
        </v-col>
        <v-col cols="12" class="menu-detail pb-2">
          <v-col cols="4" class="menu-tag">섞어국밥</v-col>
          <v-col cols="8">7,500원</v-col>
        </v-col>
        <v-col cols="12" class="menu-detail pb-2">
          <v-col cols="4" class="menu-tag">얼큰국밥</v-col>
          <v-col cols="8">8,500원</v-col>
        </v-col>
      </div>
    </v-col>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.menu-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
}
.menu-detail-category {
  font-family: 'Noto Sans KR', sans-serif;
  margin-bottom: 16px;
}
.menu-tag {
  color: black;
}
.menu-detail {
  display: flex;
  padding: 0px;
  color: #a9a9a9;
}
.menu-detail > div {
  padding: 0px;
}
</style>
