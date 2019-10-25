import api from '@/services/storeApi'

const state = {
  allStores: [],
  oneStore: [],
  error: null,
  storeInfo: {}
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
  },
  setInfo (state) {
    state.storeInfo = {
      storeName: state.oneStore.data.name,
      description: state.oneStore.data.description,
      price_avg: state.oneStore.data.price_avg.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","),
      review_cnt: state.oneStore.data.review_cnt.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
    }
  }
}

const actions = {
  async getAllStores ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getAllStores(token).then(resp => {
      commit('regiAllStores', resp)
    }).catch(error => {
      commit('setError', error)
    })
  },
  async getOneStore ({ commit }, payload) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getOneStore(payload, token).then(resp => {
      commit('regiOneStore', resp)
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
