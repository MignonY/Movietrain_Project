<template>
  <div>
    <h5>No.{{ post.id }}</h5>
    <h5>user: {{post.user}}</h5>
    <p>title: {{ post.title }}</p>

    <router-link :to="{
      name: 'DetailView',
      params: {id: post.id}}" @click.prevent="get">
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
  },

  methods:{
    get() {
      console.log('post:',this.post)}
  }
}
</script>

<style>

</style>
