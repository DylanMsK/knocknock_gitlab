const state = {
  signupShow: false,
  navDrawerShow: true,
  // 백엔드 연결하면 삭제할 것
  tempUserInfoShow: false
}

const mutations = {
  toggleSignup (state, toggle) {
    state.signupShow = toggle
  },
  toggleNavDrawer (state, toggle) {
    state.navDrawerShow = toggle
  },
  // 백엔드 연결하면 삭제할 것
  toggleUserInfo (state, toggle) {
    state.tempUserInfoShow = toggle
  }
}

export default {
  namespaced: true,
  state,
  mutations
}
