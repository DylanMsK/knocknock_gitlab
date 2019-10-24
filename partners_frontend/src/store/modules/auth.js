import api from '@/services/authApi'

const state = {
  signUpToggle: false,
  error: null,
  signOutToggle: false
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
  },
  signOutCheck (state) {
    state.signOutToggle = true
  },
  initSignOut (state) {
    state.signOutToggle = false
  }
}

const actions = {
  async userSignIn ({ commit }, payload) {
    await api.userSignIn(payload).then(resp => {
      localStorage.setItem('user', JSON.stringify(resp.data.user))
    }).catch(error => {
      commit('setError', error.message)
    })
  },
  async userSignUp ({ commit }, payload) {
    await api.userSignUp(payload).catch(err => {
      commit('setError', err.message)
    })
  },
  async userSignOut ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.userSignOut(token).then(() => {
      localStorage.removeItem('user')
      commit('signOutCheck')
    }).catch(error => {
      console.log(error.message)
    })
  },
  async userAuth ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.userAuth(token).catch(error => {
      commit('setError', error.message)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
