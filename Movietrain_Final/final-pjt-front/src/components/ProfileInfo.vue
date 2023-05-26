<template>
  <div class="profileinfo">
      <!-- <div class="video-bg">
        <video autoplay muted>
          <source src="../assets/bgim.webm" type="video/webm">
        </video>
      </div> -->
      <h1 id="bg"></h1>
      <div class="CT_info">
          <div class="px-4 py-2 text-black" style="background-color: #f8f9fa; opacity:90%">
            <div class="d-flex justify-content-center text-center py-1">
              <div class = "px-5">
                <!-- <p class="mb-1 h3">{{followers}}</p> -->
                <p class="mb-1 h3">0</p>
                <p class="small text-muted mb-0">Followers</p>
              </div>
              <div class = "px-5">
                <!-- <p class="mb-1 h3">{{followings}}</p> -->
                <p class="mb-1 h3">0</p>
                <p class="small text-muted mb-0">Followings</p>
              </div>
              <div class = "px-5">
                <!-- <p class="mb-1 h3">{{posts}}</p> -->
                <p class="mb-1 h3">0</p>
                <p class="small text-muted mb-0">Posts</p>
              </div>
              <div class = "px-5">
                <!-- <p class="mb-1 h3">{{post_likes}}</p> -->
                <p class="mb-1 h3">0</p>
                <p class="small text-muted mb-0">Likes</p>
              </div>
              <!-- <div v-if="!this.Mine">
                <button @click.prevent="follow" >{{ followButtonText }}</button>
              </div> -->


            </div>
          </div>
      </div>
    <div id ="profileset" class="CT_all">
      <div id=pimage class="circle-image">
        <img class= "photo" :src="profileImage" alt="Profile Image">
        <input type="file" ref="fileInput" style="display: none" @change ="fileChange" >
      </div>
      <button id="Pbutton" @click="uploadButtonClick" class="d-flex justify-content-center align-items-center" >
         <BIconCameraFill class="camera-icon"></BIconCameraFill>
      </button>
      <!-- <span id="nickname">USER_NICKNAME</span> -->
      <span id="nickname">{{profile?.username}}</span>
    </div>
  </div>
</template>

<script>

const API_URL = 'http://127.0.0.1:8000'
import axios from 'axios'

export default {
  name:'ProfileInfo',
  data(){
    return {
      profile: null,
      followers : 0,
      followings: 0,
      posts : null,
      post_likes : null,
      // follow: null,
      follower_flag : null,
      username: null,
      Mine : false,
      followButtonText: 'Follow',
      profileImage: require('../assets/default-profile.png'), //프로필이미지 url
    };
  },
  created(){
    this.getProfile()
  },
  computed: {
    isLogin() {
    return this.$store.getters.isLogin //로그인 여부
  },
  },
  methods:{
    getProfile(){
      const userid = `${this.$route.params.id}`
      console.log('prams:',this.$route.params.id )
      console.log('userid:', userid)
      console.log('stateid:',this.$store.state.id)
      if (this.$route.params.id == this.$store.state.id) {
        this.Mine=true
      }
      console.log(this.Mine)

    axios({
      method: 'get',
      url: `${API_URL}/user/${userid}/`,
    })
    .then((res)=>{
      // console.log(res)
      this.profile = res.data
      console.log(res.data)
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
    fileChange(event){
      const file = event.target.files[0];
      if (file){
        //FileReader를 사용하여 이미지 파일 읽어옴
        const reader = new FileReader();
        reader.onload = (e) =>{
          this.profileImage = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    //파일업로드창
    uploadButtonClick() {
      this.isClicked = true; // 클릭 시 상태 변경
      this.$refs.fileInput.click();
    },
    stopEaseInOut() {
      this.isClicked = false; // 클릭 시 상태 변경
    },
  }
}
</script>

<style scoped>
/* #profileset{
  bottom:5rem !important;
} */
.profileinfo {
  position: relative;
}

#bg{
  width: 100%;
  height: 14rem;
  background-image: url("../assets/profilebg1.png");
  background-size: cover;
  background-position: center;
  margin-right: auto;
  margin-left: auto;
  margin-bottom: 0;
  text-align: center;
  line-height: 14rem;
}

.video-bg {
  width: 100%;
  height: 14rem;
  position: relative;
  overflow: hidden;
}

.video-bg video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.circle-image {
  position: absolute;
  left: 2rem;
  top: 2rem;
  width: 15rem;
  height: 15rem;
  border-radius: 50%;
  overflow: hidden;
  display: flex;  /* 정렬 */
  justify-content: center;  /* 정렬 */
  align-items: center;  /* 정렬 */
  padding: 0.3rem;  /* padding 추가 */
  background: linear-gradient(to left, rgb(247, 255, 163), rgb(6, 155, 255), rgb(64, 206, 151), rgb(254, 14, 130)); /* 무지개빛 그라데이션을 설정 */
  background-clip: padding-box;  /* 배경을 padding-box로 제한 */
  box-sizing: border-box;  /* padding과 border가 width와 height에 포함되도록 설정 */
  box-shadow: 0 0 2rem rgba(255, 251, 0, 0.3);  /* 외부 그림자 추가 */

}


#Pbutton{
  position: absolute;
  left:12.75rem;
  top:11rem;
  width: 4.5rem;
  height: 4.5rem;
  border-radius: 70%;
  overflow:hidden;
  line-height: 4.5rem;
  background-color: white;
  opacity:75%;
  /* box-shadow: 0 0 2rem rgba(0, 255, 208, 0.3);   */
}
.photo{
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%; /* 추가 */
}
#nickname{
  position:absolute;
  font-size: 3.5rem;
  font-weight: 800;
  color:white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) ;
  /* text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8), 0px 0px 2rem rgba(255, 255, 0, 0.8) ; */
  left:20rem;
  top:8rem;

}
@media (max-width: 1130px) {
  .CT_info {
    position: sticky;
    bottom: 0;
    background-color: #f8f9fa;
  }
   .CT_info .d-flex {
    justify-content: center;
  }
}
.mb-1{
  font-weight: 900;
}

.camera-icon{
  font-size:2.5rem;
  
}



@keyframes shake {
  0% {
    transform: translate(0px, -2px);
  }
  50% {
    transform: translate(0px, 2px);
  }
  100% {
    transform: translate(0px, -2px);
  }
}

#Pbutton:hover .camera-icon {
  animation: shake 0.8s infinite;
  transform: translateY(-2px) 
}

/* 클릭 시 hover 효과를 멈추고 ease-in-out 효과만 발생 */
#Pbutton:active .camera-icon,
#Pbutton.isClicked:hover .camera-icon {
  animation: none;
  transition: transform 0.1s ease-in-out; 
  transform: scale(0.8);
}

</style>