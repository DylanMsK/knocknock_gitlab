import Vue from 'vue'
import VueRouter from 'vue-router'

import authPage from '../pages/AuthPage'
import mainPage from '../pages/MainPage'
Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: authPage, name: 'authPage' },
    { path: '/main', component: mainPage, name: 'mainPage' }
  ]
})

export default router
