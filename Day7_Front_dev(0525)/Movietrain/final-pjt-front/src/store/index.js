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
    username : null,
    id : null,

    // 게시글
    posts: [],

    // movies
    movies: [],

    // searched movies
    title : null,
    searchmovies: [],

    // movie detail
    movie : null,
    video : null,

    //community_id
    community_id: null,

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
      router.push({name : 'Home'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    
    SAVE_OTHERS(state, { token, username, id }) {
      state.token = token
      state.username = username
      state.id = id
      localStorage.setItem('username', username)
      localStorage.setItem('id', id)
      router.push({name : 'Home'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    GET_PROFILES(state){
      console.log('state:',state)
      // 스테이트닷뭐시기 하기
    },

    // community post 
    GET_POSTS(state, posts) {
      state.posts = posts
    },

    GET_MOVIES(state, movies) {
      state.movies = movies
    },

    // TMDB search데이터 수집
    GET_SEARCH(state, searchmovies){
      this.state.searchmovies = []
      this.state.searchmovies = searchmovies
      console.log('stae.serar:', this.state.searchmovies)
      // router.push({name : 'SearchView'}) -> 오류
    },

    // LOGOUT 구현
    LOGOUT(state) {
      state.token = ''
      state.username = ''
      router.push({name:"Home"})
      // Remove token and username from localStorage
      localStorage.removeItem('token')
      // localStorage.removeItem('username');
    }
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
          const token = res.data.key
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          axios({
            method: 'get',
            url: `${API_URL}/user/userid/`,  // URL to retrieve user ID based on token (customize as needed)
            headers: {
              Authorization: `Token ${token}`
            }
          })
            .then((response) => {
              console.log('response:', response)
              const username = response.data.username
              const id = response.data.id
              context.commit("SAVE_OTHERS", { token, username, id })
            })
            .catch((error) => {
              console.log(error)
            })
        })
        .catch((err) => {
        console.log(err)
      })
    },

    // 로그인 구현
    login(context, payload) {
      return new Promise((resolve, reject) => {
        const username = payload.username;
        const password = payload.password;
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
          // console.log(token)
          axios({
            method: 'get',
            url: `${API_URL}/user/userid/`,  // URL to retrieve user ID based on token (customize as needed)
            headers: {
              Authorization: `Token ${token}`
            }
          })
          .then((response) => {
            const username = response.data.username;
            const id = response.data.id;
            context.commit("SAVE_OTHERS", { token, username, id });
            resolve(); // 성공적으로 로그인이 처리되었음을 resolve로 알림
          })
          .catch((error) => {
            reject(error); // 오류를 reject로 전달
          });
      });
      }
      )},

    
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
    },

    // 프로필 구현
    getProfile(context){
      const username = localStorage.getItem('username')
      console.log(username)
      axios({
        method: 'get',
        url: `${API_URL}/user/profile/${username}`,
      })
      .then((res)=>{
        console.log('res:',res)
        console.log('context:',context)
      })
      .catch((err) => console.log(err))
    },

    // movie search context
    searchMovie(context){
      // store에서는 $표시 X

      // KOFIS 영화 검색 -> POSTER X
      // console.log(this.state.title)
      // const TITLE = `${this.state.title}`
      // const SEARCH_URL = "https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm="
      // const FULL_REQUEST = SEARCH_URL + TITLE
      // console.log(FULL_REQUEST)

      // TMDB 검색
      const URL = 'https://api.themoviedb.org/3/search/movie'
      const query = `${this.state.title}`
      const includeAdult = false
      const language = 'ko-KR'

      const headers = {
        Authorization : 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM',
        accept: 'application/json'
      }

      const params = {
        query,
        include_adult : includeAdult,
        language,
      }

      axios.get(URL, {params, headers})
      .then((res) =>
        // console.log(res.data.results),
        context.commit('GET_SEARCH', res.data.results)
        
      )
      .catch((error) => {
        // Handle the error
        console.error(error)
      })
    },
  },


  modules: {
  }
})