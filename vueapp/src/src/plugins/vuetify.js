import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import '@mdi/font/css/materialdesignicons.css'

Vue.use(Vuetify)
export default new Vuetify({
  theme: {
    dark: true
  },
  icons: {
    iconfont: 'mdi'
  }
})
