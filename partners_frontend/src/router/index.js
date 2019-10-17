import Vue from 'vue'
import VueRouter from 'vue-router'

import authPage from '../pages/AuthPage'
import storePage from '../pages/StorePage'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: authPage, name: 'authPage' },
    { path: '/store', component: storePage, name: 'storePage' }
  ]
})

export default router
