<template>
  <div>
    <h1>
      movie search List Item
    </h1>
    <MoviSearchListItem
    v-for="movie in searchmovies" :key="movie.id" :movie="movie"
    />

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

<style>

</style>
