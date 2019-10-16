import Vue from 'vue'
import VueRouter from 'vue-router'

import AuthPage from '../pages/Auth'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: AuthPage, name: 'Auth' }
  ]
})

export default router
