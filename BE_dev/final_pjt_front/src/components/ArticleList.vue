<template>
  <div class="article-list">
    <h3>Post List</h3>
    <ArticleListItem 
    v-for="post in posts" :key="post.id" :post="post"
    />
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
}
</style>
