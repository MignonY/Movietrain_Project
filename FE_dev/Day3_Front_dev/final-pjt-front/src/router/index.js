import Vue from 'vue'
import VueRouter from 'vue-router'

//mainView import
import DefaultLayout from '@/layout/DefaultLayout'
import EmptyLayout from '@/layout/EmptyLayout'

Vue.use(VueRouter)



const router = new VueRouter({
  mode: 'history',
  routes : [
    {
      path:'/',
      name:'DefaultLayout',
      component: DefaultLayout,
      children:[
        {
          path: '/',
          name: 'Home',
          component: ()=>import('@/views/HomeView')
        },
        // {
        //   path: '/login',
        //   name: 'Login',
        //   component: ()=>import('@/views/ProfileView')
        //   // route level code-splitting
        //   // this generates a separate chunk (about.[hash].js) for this route
        //   // which is lazy-loaded when the route is visited.
        //   // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
        // },
        {
          path: '/profile',
          name: 'Profile',
          component:()=>import('@/views/ProfileView')
        }
      ]
      
    },
    {
      path:'/',
      name:'EmptyLayout',
      component:EmptyLayout,
      children:[
        {
          path: '/login',
          name: 'Login',
          component: ()=>import('@/views/LoginView')
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          // component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
        },
      ]
      
    }
   
    
    //nested routing - 로그인시 노출 
    // {
    //   path: '/user/:id',
    //   name: 'Profile',
    //   component: ProfileView,
    //   children: [
    //     {
    //       path: 'evaluates',
    //       component: UserEvaluates
    //     },
    //     {
    //       path: 'posts',
    //       component: UserPosts
    //     },
    //     {
    //       path: 'histagram',
    //       component: UserHistagram
    //     }
    //   ]
    // },
   
  ]
  // base: process.env.BASE_URL,
  // routes
})

export default router
