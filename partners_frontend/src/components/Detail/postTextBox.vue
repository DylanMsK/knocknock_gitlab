<template>
  <div>
    <div class="post-layout mb-4">
      <div class="pa-5">
        <p class="post-title mb-0">공지사항 수정하기</p>
        <v-textarea
          class="text-area-font"
          v-model="postContent"
        >
        </v-textarea>
        <div class="fill-width btn-layout">
          <v-btn
            color="primary"
            dark
            small
            @click="submit()"
          >작성 완료</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      newPost: ''
    }
  },
  computed: {
    postContent: {
      get () {
        return this.$store.state.postText.postContent
      },
      set (content) {
        this.newPost = content
      }
    }
  },
  methods: {
    ...mapMutations('postText', ['changeTextBox', 'changeContent']),
    submit () {
      this.changeTextBox()
      this.changeContent(this.newPost)
    }
  }
}
</script>

<style scoped>
.post-layout {
  border: solid 1px #c1c1c1;
  border-radius: 3%;

}
.post-title {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 14px;
  font-weight: 700;
}
.btn-layout {
  display: flex;
  justify-content: flex-end;
}
.text-area-font {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
