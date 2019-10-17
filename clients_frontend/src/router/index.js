import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '../pages/MainPage'
import AuthPage from '../pages/AuthPage'

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
    }
  ]
})
