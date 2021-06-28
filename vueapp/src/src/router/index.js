import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue')
  },
  {
    path: '/readinglist',
    name: 'ReadingList',
    component: () => import('../components/Account/ReadingList.vue')
  },
  {
    path: '/tvshow/:slug',
    name: 'TvshowDetail',
    props: true,
    component: () => import('../views/Tvshow.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
