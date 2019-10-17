const state = {
  signupShow: false
}

const mutations = {
  toggleSignup (state, toggle) {
    state.signupShow = toggle
  }
}

export default {
  namespaced: true,
  state,
  mutations
}
