import Vue from 'vue'
import Vuex from 'vuex'

import auth from './modules/auth'
import drawer from './modules/drawer'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    drawer
  }
})
