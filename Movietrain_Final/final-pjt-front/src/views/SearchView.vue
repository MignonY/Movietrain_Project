<template>
  <div>
    <h1>Movie Search List</h1>
    <MoviSearchList/>
  </div>
</template>

<script>
import MoviSearchList from '@/components/MoviSearchList.vue'

export default {
  name: 'SearchView',
  components:{
    MoviSearchList
  },

}
</script>

<style>

</style>