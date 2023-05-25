<template>
  <div class="card article-list">
    <div class="card-header">
      <h3>Post List</h3>
    </div>
    <div class="card-body">
      <ArticleListItem 
        v-for="post in posts" :key="post.id" :post="post"
      />
    </div>
  </div>
</template>


<script>
import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  computed: {
    posts() {
      return this.$store.state.posts
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
  width: 50%; 
  margin: 0 auto; 
}
</style>
