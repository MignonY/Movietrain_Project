<template>
  <div class="movielist">
    <h1>
      <span class="title-decoration">TOP 20</span> MOVIES
    </h1>
    <div class="row">
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie" class="col-xxl-2 col-md-3 col-sm-6 mb-4">

      </MovieListItem>
    </div>
  </div>
</template>

<script>

import MovieListItem from '@/components/MovieListItem'

export default {
  name: 'MovieList',
  components:{
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  },
  created(){
    this.getMovies()
    // console.log(this.movies)
  }

};
</script>

<style scoped>
h1{
  margin-top:1rem;
  margin-bottom:2rem;
  color:white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) ;
}
.title-decoration {
  font-weight: bold;
  font-size: 1.2em;
  color: red;
}

.movielist {
  margin-left: auto;
  margin-right: auto;
  margin-top: 5rem;
  width: 80%;
  color:black;
}

.row {
  display: flex;
  flex-wrap: wrap;
}


.card-link {
  text-decoration: none;
  color: inherit;
}
</style>