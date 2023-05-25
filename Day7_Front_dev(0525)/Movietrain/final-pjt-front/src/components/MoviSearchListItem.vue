<template>
  <div>
    <p>{{movie.id}}</p>
    <p>{{movie.title}}</p>
    
    <hr>
  </div>
</template>

<script>
export default {
  name : 'MoviSearchListItem',
  props: {
    movie: Object,
  },
}
</script>

<style>

</style>