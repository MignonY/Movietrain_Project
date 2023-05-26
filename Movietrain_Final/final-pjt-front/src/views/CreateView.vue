<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createPost">
      <label for="title"> 제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content"> 내용 :</label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id=submit>
    </form>

    <h2>뒤로가기 버튼 추가해야함 </h2>
    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createPost(){
      const title= this.title
      const content = this.content

      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content){
        alert('내용을 입력해주세요')
       return
      }
      const token = this.$store.state.token
      const data = {
        title: title,
        content: content,
      }
      const headers = {
        Authorization : `Token ${token}`
      }
      axios.post(
        `${API_URL}/community/`, data, {headers})
    
      // axios({
      //   method: 'post',
      //   url: `${API_URL}/community/`,
      //   data: {title, content},
      // })
      .then((res) =>{ 
        console.log('res:',res)
        this.$router.push({name:'Article'})
      })
      .catch((err)=>{
        console.log(err)
        // console.log(err.response.data)
      })
    }
  }
}
</script>

<style>

</style>