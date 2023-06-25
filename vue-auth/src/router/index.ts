import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {path: '/login', component: () => import('@/views/Login/Login_Page.vue')},
  {path: '/', component: () => import('@/views/Home_Page.vue')},
  {path: '/register', component: () => import('@/views/Register_Page.vue')},
  {path: '/forgot-password', component: () => import('@/views/Forgot_Password_Page.vue')},
  {path: '/reset/:token', component: () => import('@/views/Reset_Page.vue')},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
