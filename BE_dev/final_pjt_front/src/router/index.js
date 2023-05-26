import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleView from '../views/PostView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import ProfileView from '../views/ProfileView.vue'
import SearchView from '../views/SearchView.vue'
import MovieDetail from '../views/MovieDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/Post',
    name: 'PostView',
    component: ArticleView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '/post/detail',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/profile/:id',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/MovieDetail',
    name: 'MovieDetail',
    component: MovieDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
