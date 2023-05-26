<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{post?.id}}</p>
    <p> 작성자 : 
    <router-link :to="{name: 'ProfileView', params: {id: post.user}} ">
      {{post?.user}}
    </router-link>
    <p>제목 : {{post?.title}}</p>
    <p>내용 : {{post?.content}}</p>
    <p>댓글 갯수 : {{post?.comment_count}}</p>
    <p>댓글들 : {{post?.comment_set}}</p>
    <p>댓글의 답글 : {{post?.reply_set}}</p>
    <p>작성시간 : {{post?.created_at}}</p>
    <p>수정시간 : {{post?.updated_at}}</p>
  </div>
  
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'DetailView',
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

                // console.log(this.post)
            })
            .catch((err) => console.log(err))
        }
    }
}
</script>

<style>
</style>


// methods: {
//         getPostdetail() {
//           this.$store.state.community_id = this.$route.params.id

//             axios({
//                 method: 'get',
//                 url: `${API_URL}/community/${this.$store.state.community_id}/`,
//             })
//             .then((res) =>{
//                 console.log(res.data)  
//                 console.log(this.post)
//             })
//             .catch((err) => console.log(err))
//         }
//     }