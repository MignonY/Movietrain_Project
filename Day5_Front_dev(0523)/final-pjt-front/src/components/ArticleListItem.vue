<template>
  <div>
    <h5>{{ post.id }}</h5>
    <p>{{ post.title }}</p>
    <router-link :to="{
      name: 'DetailView',
      params: {id: post.id }}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    post: Object,
  }
}
</script>

<style>

</style>
