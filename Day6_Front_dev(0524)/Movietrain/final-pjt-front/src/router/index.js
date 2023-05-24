import Vue from 'vue'
import VueRouter from 'vue-router'

// 컴포넌트를 가져옵니다.
import DefaultLayout from '@/layout/DefaultLayout'
import EmptyLayout from '@/layout/EmptyLayout'
import MovieDetailView from '@/views/MovieDetailView' // MovieDetailView 컴포넌트를 가져옵니다.

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        {
          path: '/',
          name: 'Home',
          component: () => import('@/views/HomeView')
        },
        {
          path: '/profile',
          name: 'Profile',
          component: () => import('@/views/ProfileView')
        },
        {
          path: '/article',
          name: 'Article',
          component: () => import('@/views/ArticleView')
        },
        // MovieDetailView로 라우팅
        {
          path: '/movies/:id',
          name: 'MovieDetailView',
          component: MovieDetailView
        }
      ]
    },
    {
      path: '/',
      name: 'EmptyLayout',
      component: EmptyLayout,
      children: [
        {
          path: '/login',
          name: 'Login',
          component: () => import('@/views/LoginView')
        },
        {
          path: '/signup',
          name: 'Signup',
          component: () => import('@/views/SignupView')
        },
      ]
    }
  ]
})

export default router
