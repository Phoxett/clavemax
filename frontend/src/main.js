import { createApp } from 'vue'
import App from './App.vue'

import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'


const app = createApp(App)

import './assets/main.css'


import 'primevue/resources/themes/arya-green/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'


app.use(PrimeVue)
app.use(ToastService)


app.mount('#app')
