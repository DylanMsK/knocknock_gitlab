import api from '@/services/api'

const state = {
  allStores: [],
  oneStore: null,
  error: null
}

const mutations = {
  regiAllStores (state, data) {
    state.allStores = data
  },
  regiOneStore (state, data) {
    state.oneStore = data
  },
  setError (state, data) {
    state.error = data
  },
  initError (state) {
    state.error = null
  }
}

const actions = {
  async getAllStores ({ commit }, payload) {
    await api.getAllStore(payload).then(resp => {
      commit('regiAllStores', resp)
    }).catch(error => {
      commit('setError', error)
    })
  },
  async getOneStore ({ commit }, payload) {
    await api.getOneStore(payload).then(resp => {
      commit('regiOneStres', resp)
    }).catch(error => {
      commit('setError', error)
    })
  },
  async enrollStore ({ commit }, payload) {
    await api.enrollStore(payload).catch(error => {
      commit('setError', error)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
