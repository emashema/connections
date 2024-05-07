import Vue from 'vue'
import App from './App.vue'

// Bootstrap and BootstrapVue
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)

// Custom CSS
import style from './assets/scss/main.scss'
Vue.use(style)

// Custom toast prototype
Vue.prototype.$toast = function(message) {
  this.$bvToast.toast(message, {
    toaster: 'b-toaster-top-center',
    toastClass: 'custom-toast',
    autoHideDelay: 1000,
    noCloseButton: true,
    solid: true
  })
}

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
