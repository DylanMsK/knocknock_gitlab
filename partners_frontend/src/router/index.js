import Vue from 'vue'
import VueRouter from 'vue-router'

import authPage from '../pages/AuthPage'
import storePage from '../pages/StorePage'
import storeDetailPage from '../pages/StoreDetailPage'
import registerStorePage from '../pages/RegisterStorePage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: authPage, name: 'authPage' },
    { path: '/store', component: storePage, name: 'storePage' },
    { path: '/store/register', component: registerStorePage, name: 'registreStorePage' },
    { path: '/store/storenumber', component: storeDetailPage, name: 'storeDetailPage' }
  ]
})

export default router
