<template>
<div class="articleview">
  <h1>Community Page</h1>
  <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
  <ArticleList></ArticleList>
  <hr>
</div>
</template>

<script>

import ArticleList from '@/components/ArticleList.vue'

export default {
  name:'ArticleView',
  components:{
    ArticleList
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  created() {
    this.getPosts()
  },
  methods: {
    getPosts() {
      if (this.isLogin) {
        this.$store.dispatch('getPosts')
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({ name: 'Login' })
      }


      // 로그인이 되어 있으면 getArticles action 실행
      // 로그인 X라면 login 페이지로 이동

    }
  }
}
</script>

<style scoped>
.articleview{
  background-color: white;
  opacity:65%;
  height: 100vh; /* 전체 화면 크기를 채우기 위해 추가 */
  width: 100vw; /* 전체 화면 크기를 채우기 위해 추가 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>