<template>
  <v-col>
    <div class="event-title">
      <v-icon class="mb-4 pr-3" color="#FBC02D">fas fa-star</v-icon><p>이벤트</p>
    </div>
    <v-expansion-panels
      accordion
    >
      <v-expansion-panel
        v-for="(item,i) in arr"
        :key="i"
      >
        <v-expansion-panel-header class="list-header">{{ item }}</v-expansion-panel-header>
        <v-expansion-panel-content
          class="list-header"
        >
          <p>{{ arr_content[i] }}</p>
          <div class="event-buttons">
            <v-btn class="mr-4" color="#0091EA" dark small @click="openCloseTextBox">수정하기</v-btn>
            <v-btn small color="#D32F2F" dark>삭제하기</v-btn>
          </div>
          <eventTextBox
            v-show="textBoxToggle"
          />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-pagination
      class="pt-5"
      v-model="page"
      :length="6"
      circle
    ></v-pagination>
  </v-col>
</template>

<script>
import eventTextBox from './eventTextBox'

export default {
  components : {
    eventTextBox
  },
  data () {
    return {
      arr: ['하루만 떨이 행사!','b','c','d','e', 'f', 'g'],
      arr_content: ['떨이떨이떨이 !', 'B', 'C', 'D', 'E', 'F', 'G'],
      page: 1,
      textBoxToggle: false
    }
  },
  methods: {
    openCloseTextBox () {
      this.textBoxToggle = !this.textBoxToggle
    }
  }
}
</script>

<style scoped>
.event-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
  display: flex;
}
.list-header {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
}
.event-buttons {
  display: flex;
  justify-content: flex-end;
}
</style>
