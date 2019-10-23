import api from '@/services/api'

const state = {
  err: null
}

const mutations = {
  setError (state, payload) {
    state.err = payload
  },
  initError (state) {
    state.err = null
  }
}

const actions = {
  async signUp ({ commit }, payload) {
    await api.signUp(payload).catch(err => {
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
