import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  async created () {
    if ('user' in localStorage) {
      await store.dispatch('auth/userAuth')
    } else {
      router.push('/')
    }
  },
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
