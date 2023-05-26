<template>
  <div>
    <h1>movie detail view</h1>
    <div v-if="movie">
      <h2>{{movie.title}}</h2>
      <p>{{video}}</p>
      <p>{{movie.overview}}</p>
      <p>{{movie.poster_path}}</p>
      <ul> 
        <li v-for=" genre in movie.genres" :key="genre.id" :genre="name">
          {{genre.name}}</li>
      </ul>
      <p>{{movie.vote_average}}</p>
      <p>{{movie.vote_count}}</p>
      <p>{{movie.release_date}}</p>
      <p></p>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// import {route} from 'vue-router'
export default {
  data() {
    return {
      movie : null,
      video: null,
    }
  },
  created() {
    this.detailmovies()
    this.videodetail()
  },
    // const movieId = `${this.$route.params.id}`
   methods:{
        detailmovies() {
      const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM'
          }
        };
  
      const URL = 'https://api.themoviedb.org/3/movie/'
      const movieId = `${this.$route.params.id}`
      const language= 'ko-KR'
      const full = URL + movieId + '?language=' + language
      // console.log(full)
      fetch( full, options)
      // fetch(
      //   'https://api.themoviedb.org/3/movie/27505?language=ko-KR', options)
        .then(response => response.json())
        .then(response => {
        console.log(response)
        this.movie = response
        // this.$store.state.movie = response
        // this.$store.state.movie = response
        }
        )
        .catch(err => console.error(err));
      },

    videodetail(){
      const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM'
        }
      }
  
      const URL = 'https://api.themoviedb.org/3/movie/'
      const movieId = `${this.$route.params.id}`
      const language= 'ko-KR'
  
      const FULL = URL + movieId + '/videos?language=' + language 
    fetch(FULL, options)
    .then(res => res.json())
    .then(res => {
      const youtube = 'https://www.youtube.com/watch?v='

      this.video = youtube + res.results[0].key
      // this.$store.state.video = this.video
    }
    )
    .catch(err => console.error(err));
    },


    // detailmovies(){
    //   this.$store.dispatch('detailmovies')
    //   this.$store.videodetail('detailview')
    // }
  },
}
</script>

<style>

</style>
