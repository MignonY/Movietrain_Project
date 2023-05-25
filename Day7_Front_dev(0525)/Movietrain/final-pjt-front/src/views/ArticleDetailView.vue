<template>

<div class="articleview bg-image">
  <div class="header-section">
    <h1 class="MAINTEXT">Community Page</h1>
  </div>
  <div class="content-section">
    <div class = "TEXT card article mt-5">
    <div class="card-header">
      <h4>제목 : {{post?.title}}</h4>
      <hr>
    <p> 작성자 : 
    <router-link :to="{name: 'Profile', params: {id: post.user}} ">
      {{post?.user}}
    </router-link>
    <hr>
    <p>작성시간 : {{post?.created_at}}</p>
    </div>
    <div class="card-body">
      <h5>{{post?.content}}</h5>
    </div> 
  </div>
</div>
  
    <!-- <h1>Detail</h1>
    <p>글 번호 : {{post?.id}}</p>
    <p>제목 : {{post?.title}}</p>
    <p>내용 : {{post?.content}}</p>
    <p>작성시간 : {{post?.created_at}}</p>
    <p>수정시간 : {{post?.updated_at}}</p> -->
    <!-- <h1>Detail</h1> -->
    <!-- <p>글 번호 : {{post?.id}}</p> -->
    
    
    <!-- <p>수정시간 : {{post?.updated_at}}</p> -->
    <!-- <p>댓글 갯수 : {{post?.comment_count}}</p> -->
    <!-- <p>댓글들 : {{post?.comment_set}}</p> -->
    <!-- <p>댓글의 답글 : {{post?.reply_set}}</p> -->
  </div>
  
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleDetailView',
    created() {
        this.getPostdetail()
    },
    data(){
        return{
            post: null
        }
    },
    methods: {
        getPostdetail() {
            axios({
                method: 'get',
                url: `${API_URL}/community/${this.$route.params.id}/`,
            })
            .then((res) =>{
                // console.log(res)
                this.post = res.data
            })
            .catch((err) => console.log(err))
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
  background-color: rgba(2, 2, 2, 0.7);
  height: 100vh; /* 뷰포트의 세로 크기로 설정 */
  width: 100%;
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
}

.bg-image {
  background-image: linear-gradient(90deg, rgba(149, 255, 207, 0.3), rgba(255, 146, 215, 0.3)), url(../assets/Artbg2.png);
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
.TEXT{
  font-size: 1rem;
  font-weight: 300;
  color:black;
  /* text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) ; */
}
.article {
  text-align: start;
  width: 60%; 
  margin: 0 auto; 
}
.article {
  /* text-align: start; */
  height: 50%; 
}
</style>