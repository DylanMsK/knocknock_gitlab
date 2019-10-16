const state = {
  signUpToggle: false
}

const mutations = {
  onOff (state) {
    state.signUpToggle = !state.signUpToggle
  }
}

export default {
  namespaced: true,
  state,
  mutations
}