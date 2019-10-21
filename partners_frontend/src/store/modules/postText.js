const state = {
  postContent: '아프리카 돼지 열병 사태로 당분간 영업을 하지 않습니다. 혹시나 국밥이 마려우신 분은 성진네 국밥가게를 가주시기 바랍니다.'
}

const mutations = {
  changeContent (state, content) {
    state.postContent = content
  }
}

export default {
  namespaced: true,
  state,
  mutations
}