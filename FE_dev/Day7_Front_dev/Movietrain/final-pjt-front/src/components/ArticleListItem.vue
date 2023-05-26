<template>
  <div>
    <!-- <h5>No.{{ post.id }}</h5> -->
    <!-- <h5>작성자: {{post.user}}</h5> -->
    <!-- <p>title: {{ post.title }}</p> -->

    <span>{{ post.id }}.</span>
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: post.id}}" @click.prevent="get">
      {{ post.title }}
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
  created(){
    this.get()
  },

  methods:{
    get() {
      console.log('post:',this.post)}
  }
}
</script>

<style>

</style>
