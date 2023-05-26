<template>
  <div>
    <h1> PROFILE PAGE</h1>
    <p>profile data: {{profile}}</p>
    <p>username: {{username}}</p>
    <p>followers: {{followers}}</p>
    <p>followings:{{followings}}</p>
    <p>posts: {{posts}}</p>
    <p>post_likes: {{post_likes}}</p>
    <!-- <p>{{follow}}</p> -->
    <!-- <p>username: {{profile?.username}}</p>
    <p>image: {{profile?.image}}</p>
    <p>email: {{profile?.email}}</p>
    <p>followers_count: {{profile?.followers_count}}</p>
    <p>following_count: {{profile?.following_count}}</p> -->
    <!-- <h1>{{ userProfile.user.username }}</h1>
    <p>Followers: {{follow}}</p> -->
    <div v-if="!this.Mine">
      <button @click.prevent="follow" >{{ followButtonText }}</button>
    </div>
    
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'

export default {
    name: 'ProfileItem',
        data(){
        return{
            profile: null,
            followers : null,
            followings: null,
            posts : null,
            post_likes : null,
            // follow: null,
            follower_flag : null,
            username : null,
            Mine : false,
            followButtonText: 'Follow'
        }
    },
    created(){
      this.getProfile()
    },
    computed: {
      isLogin() {
      return this.$store.getters.isLogin //로그인 여부
    }
    },
    methods:{
      getProfile(){
        const userid = `${this.$route.params.id}`
        console.log('prams:',this.$route.params.id )
        console.log('userid:', userid)
        console.log('stateid:',this.$store.state.id)
        if (this.$route.params.id == this.$store.state.id) {
          this.Mine=true
        } else if ({

        })
        console.log(this.Mine)

      axios({
        method: 'get',
        url: `${API_URL}/user/${userid}/`,
      })
      .then((res)=>{
        // console.log(res)
        this.profile = res.data
        // console.log(res.data)
        this.followers = res.data.followers.length
        this.followings = res.data.followings.length
        this.posts = res.data.post_set.length
        this.post_likes = res.data.like_posts.length
        this.username = res.data.username
      })
      .catch((err) => console.log(err))
      },

      follow() {
        const username = localStorage.getItem('id')
        // console.log(username) // 내 아이디
        // yourname은 어떻게 할꺼?
        // profile/<int:username>/<int:yourname>/
        const yourname = this.$route.params.id
        axios.post(`${API_URL}/user/${username}/${yourname}/`, )
        .then((res)=>{
          // console.log(res.data.flag)
          if (res.data.flag) {
            this.followers ++
            this.followButtonText = 'Unfollow'
          }
          else{
            this.followers --
            this.followButtonText = 'Follow'
          }
        })
        .catch((err) => console.log(err))
      },
    },
}
</script>

<style>

</style>

