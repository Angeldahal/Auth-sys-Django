import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Login_Page from '@/views/Login_Page.vue'

const routes: Array<RouteRecordRaw> = [
  {path: '/login', component: Login_Page},
  {path: '/', component: () => import('@/views/Home_Page.vue')},
  {path: '/register', component: () => import('@/views/Register_Page.vue')},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
