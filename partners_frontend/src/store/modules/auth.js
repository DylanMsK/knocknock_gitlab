import api from '@/services/api'

const state = {
  signUpToggle: false,
  error: null
}

const mutations = {
  onOff (state) {
    state.signUpToggle = !state.signUpToggle
  },
  setError (state, payload) {
    state.error = payload
  },
  initError (state) {
    state.error = null
  }
}

const actions = {
  async userSignUp ({ commit }, payload) {
    await api.userSignUp(payload).then(resp => {
      console.log(resp)
    }).catch(err => {
      commit('setError', err.message)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
