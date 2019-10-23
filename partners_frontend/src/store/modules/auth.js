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
  async userSignIn ({ commit }, payload) {
    await api.userSignIn(payload).then(resp => {
      localStorage.setItem('user', JSON.stringify(resp.data.user))
    }).catch(err => {
      commit('setError', err.message)
    })
  },
  async userSignUp ({ commit }, payload) {
    await api.userSignUp(payload).catch(err => {
      commit('setError', err.message)
    })
  },
  async userSignOut ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.userSignOut(token)
  },
  async userAuth ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.userAuth(token)
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
