import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import App from './App.vue'
import Series from './Series.vue'

const routes = [
    {path: '/', component: App},
    {path: '/series/:title', component: Series},
    {path: '*', redirect: '/'}
]

const router = new VueRouter({routes: routes})


var app = new Vue({router: router}).$mount('#app')
