<template>
  <v-col>
    <div class="post-title">
      <p><v-icon class="mb-1 pr-3" color="#D32F2F">fas fa-exclamation</v-icon>공지사항</p>
      <p class="new-post" @click="newPost()">새 글 등록하기</p>
    </div>
    <newTextBox v-show="newPostBoxToggle"/>
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
          <div class="post-buttons">
            <v-btn class="mr-4" color="#0091EA" dark small @click="openCloseTextBox">수정하기</v-btn>
            <v-btn small color="#D32F2F" dark>삭제하기</v-btn>
          </div>
          <postTextBox
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
import postTextBox from './postTextBox'
import newTextBox from './newTextBox'

export default {
  components: {
    postTextBox,
    newTextBox
  },
  data () {
    return {
      arr: ['휴가', 'b', 'c', 'd', 'e', 'f', 'g'],
      arr_content: ['아프리카 열병 사태로 영업을 하지 않습니다.', 'B', 'C', 'D', 'E', 'F', 'G'],
      page: 1,
      textBoxToggle: false,
      newPostBoxToggle: false
    }
  },
  methods: {
    openCloseTextBox () {
      this.textBoxToggle = !this.textBoxToggle
    },
    newPost () {
      this.newPostBoxToggle = !this.newPostBoxToggle
    }
  }
}
</script>

<style scoped>
.post-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
  font-weight: 900;
  display: flex;
  justify-content: space-between;
}
.list-header {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
}
.post-buttons {
  display: flex;
  justify-content: flex-end;
}
.new-post {
  color: #0091EA;
  font-size: 16px;
  font-weight: 500;
}
</style>
