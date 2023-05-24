<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{post?.id}}</p>
    <p>제목 : {{post?.title}}</p>
    <p>내용 : {{post?.content}}</p>
    <p>작성시간 : {{post?.created_at}}</p>
    <p>수정시간 : {{post?.updated_at}}</p>
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

<style>
</style>