import Vue from 'vue'
import Vuex from 'vuex'
import toggle from './modules/toggle'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    toggle
  }
})
