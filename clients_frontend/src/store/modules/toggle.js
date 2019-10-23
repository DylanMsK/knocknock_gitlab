const state = {
  signupShow: false,
	headerShow: true,
	navDrawerShow: false,
  // 백엔드 연결하면 삭제할 것
  tempUserInfoShow: false,
	filterShow: false,
	registerReviewModalShow: false,
}

const mutations = {
  toggleSignup (state, toggle) {
    state.signupShow = toggle
  },
  toggleHeader (state, toggle) {
    state.headerShow = toggle
	},
	toggleNavDrawer (state, toggle) {
		state.navDrawerShow = toggle
	},
  // 백엔드 연결하면 삭제할 것
  toggleUserInfo (state, toggle) {
    state.tempUserInfoShow = toggle
  },
  toggleFilter (state, toggle) {
	  state.filterShow = toggle
	},
	toggleRegisterReviewModal (state, toggle) {
		state.registerReviewModalShow = toggle 
	}
}

export default {
  namespaced: true,
  state,
  mutations
}
