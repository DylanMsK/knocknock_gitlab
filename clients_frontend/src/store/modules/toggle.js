const state = {
  signupShow: false,
  navDrawerShow: true
}

const mutations = {
  toggleSignup (state, toggle) {
    state.signupShow = toggle
  },
  toggleNavDrawer (state, toggle) {
    state.navDrawerShow = toggle
  }
}

export default {
  namespaced: true,
  state,
  mutations
}
