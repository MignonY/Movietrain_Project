<template>
  <div class="container mx-auto mt-5" style="width: 60%;">
    <h1>Search Results</h1>
    <div class="d-flex justify-content-center flex-wrap">

      <MoviSearchListItem
      v-for="movie in searchmovies" :key="movie.id" :movie="movie"
      class="col-3 p-3"
      />

    </div>
  </div>
</template>


<script>
import MoviSearchListItem from '@/components/MoviSearchListItem.vue'

export default {
  name : 'MoviSearchList',
  components: {
    MoviSearchListItem
  },
  computed: {
  searchmovies(){
    return this.$store.state.searchmovies
  }
  }
}
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