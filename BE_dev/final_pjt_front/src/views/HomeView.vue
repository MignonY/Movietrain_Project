<template>
  <div class="home">
    <h1>MOVIE LIST</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'HomeView',
    components: {
    MovieList
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin //로그인 여부
    }
  },

  created() {
    this.getMovies()
  },
  methods: {
    getMovies(){
      if (this.isLogin) {
        this.$store.dispatch('getMovies')
      } else{
        alert('로그인이 필요합니다.')
        this.$router.push({name: 'LogInView'})
      }
    }
  }

}
</script>
