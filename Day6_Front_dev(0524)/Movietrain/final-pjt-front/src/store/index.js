import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    // 로그인
    token: null,

    // username
    userId : null,

    // 게시글
    posts: [],

    // movies
    movies: [],
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    // 토큰 방식 로그인 
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'Homeview'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    
    SAVE_OTHERS(state, { token, userId }) {
      state.token = token
      state.userId = userId
      router.push({name : 'Homeview'}) // store/index.js $router 접근 불가 -> import를 해야함
    },


    // community post 
    GET_POSTS(state, posts) {
      state.posts = posts
    },

    GET_MOVIES(state, movies) {
      state.movies = movies
      console.log(movies)
    },
  },
  actions: {
    // 회원 가입 구현
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    // 로그인 구현
    login(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, 
          password
        }
      })
      .then((res)=> {
        const token = res.data.key
        console.log(token)
        axios({
          method: 'get',
          url: `${API_URL}/user/userid/`,  // URL to retrieve user ID based on token (customize as needed)
          headers: {
            Authorization: `Token ${token}`
          }
        })
          .then((response) => {
            const userId = response.data.userId
            context.commit("SAVE_OTHERS", { token, userId })
          })
          .catch((error) => {
            console.log(error)
          })
      })
      // .then((res)=> {
      //   context.commit("SAVE_TOKEN", res.data.key)
      // })
      .catch((err)=> console.log(err))
    },
    
    // posts 구현
    getPosts(context){
      axios({
        method: 'get',
        url: `${API_URL}/community/`,
        })
        .then((res)=>
          context.commit('GET_POSTS', res.data)
        )
        .catch((err)=> console.log(err))
    },

    // movies 구현
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
      })
      .then((res)=>
      context.commit('GET_MOVIES', res.data))
      .catch((err)=> console.log(err))
    }

  },
  modules: {
  }
})