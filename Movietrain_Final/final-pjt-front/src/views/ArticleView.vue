<template>
<div class="articleview bg-image">
  <div class="header-section">
    <h1 class="MAINTEXT">Community Page</h1>
  </div>
  <div class="content-section flex-start">
    <router-link :to="{ name: 'Create' }" class="btn btn-success my-5">글쓰기</router-link>
    <ArticleList></ArticleList>
    <hr>
  </div>
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
.articleview {
  height: auto;  /* Here */
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;  /* And here */
}

.header-section {
  height: 30vh;
  /* background-image: url(../assets/Artbg1.png); */
  background-position: center bottom;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.content-section {
  background-color: rgba(255, 255, 255, 0.7);
  height: auto;  /* Here */
  width: 100%;
  height:100vh;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
}

.bg-image {
  background-image: linear-gradient(90deg, rgba(149, 255, 207, 0.3), rgba(255, 146, 215, 0.3)), url(../assets/Artbg1.png);
  background-position: center bottom;
  background-size: cover;
  background-repeat: no-repeat;
}
.MAINTEXT{
  font-size: 3.5rem;
  font-weight: 800;
  color:white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) ;
}
</style>