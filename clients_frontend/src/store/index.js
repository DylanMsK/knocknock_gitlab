import Vue from 'vue'
import Vuex from 'vuex'
import toggle from './modules/toggle'
import storeInfo from './modules/storeInfo'
import menu from './modules/menu'
import review from './modules/review'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
	toggle,
	storeInfo,
	menu,
	review
  }
})
