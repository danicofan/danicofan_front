import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import App from './App.vue'
import Series from './Series.vue'

const Foo = {template: '<div>foo</div>'}
const Bar = {template: '<div>bar</div>'}

const routes = [
    {path: '/', component: App},
    {path: '/series/:title', component: Series},
    {path: '/bar', component: Bar}
]

const router = new VueRouter({routes: routes})


var app = new Vue({router: router}).$mount('#app')
