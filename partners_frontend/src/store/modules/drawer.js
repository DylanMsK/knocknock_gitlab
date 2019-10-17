const state = {
  drawerToggle: false,
  headerToggle: true
}

const mutations = {
  drawerOnOff (state) {
    state.drawerToggle = !state.drawerToggle
  },
  headerOnOff (state) {
    state.headerToggle = !state.headerToggle
  },
  headerInit (state) {
    state.headerToggle = true
  }
}

export default {
  namespaced: true,
  state,
  mutations
}
