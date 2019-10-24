import api from '@/services/api'

const state = {
  err: null,
  condition: true // 로그인
}

const mutations = {
  setError (state, payload) {
    state.err = payload
  },
  initError (state) {
    state.err = null
  },
  logInCondition (state) {
    state.condition = true // 로그인
  },
  logOutCondition (state) {
    state.condition = false // 로그아웃
  }
}

const actions = {
  async signUp ({ commit }, payload) {
    await api.signUp(payload).catch(err => {
      commit('setError', err.message)
    })
  },
  async signIn ({ commit }, payload) {
    await api.signIn(payload).then(resp => {
      localStorage.setItem('user', JSON.stringify(resp.data.user))
    }).catch(err => {
      commit('setError', err.message)
    })
  },
  async signOut ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.signOut(token).then(() => {
      localStorage.removeItem('user')
      commit('setError')
    }).catch(err => {
      console.log(err.message)
    })
  },
  async userAuth ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.userAuth(token).catch(err => {
      commit('setError', err)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
