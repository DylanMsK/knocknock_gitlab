import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '../pages/MainPage'
import AuthPage from '../pages/AuthPage'
import TermsOfUsePage from '../pages/TermsOfUsePage'
import StoreDetailPage from '../pages/StoreDetailPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPage
    },
    {
      path: '/auth',
      name: 'auth',
      component: AuthPage
    },
    {
      path: '/termsofuse',
      name: 'termsofuse',
      component: TermsOfUsePage
		},
		{
			path: '/store',
			name: 'store-detail',
			component: StoreDetailPage
		}
  ]
})
