import Vue from 'vue'
import App from './App'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
//import 'material-design-icons-iconfont/dist/material-design-icons.min.css'

Vue.use(Vuetify)
Vue.config.productionTip = false

new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
