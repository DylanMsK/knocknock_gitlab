import Vue from 'vue'
import Vuex from 'vuex'
import toggle from './modules/toggle'
import store from './modules/store'
import menu from './modules/menu'
import review from './modules/review'
import profile from './modules/profile'
import auth from './modules/auth'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		toggle,
		store,
		menu,
		review,
		profile,
		auth
	}
})
