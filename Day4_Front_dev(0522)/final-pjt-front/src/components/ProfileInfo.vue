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
                <p class="mb-1 h3">30</p>
                <p class="small text-muted mb-0">Followers</p>
              </div>
              <div class = "px-5">
                <p class="mb-1 h3">105</p>
                <p class="small text-muted mb-0">Following</p>
              </div>
              <div class = "px-5">
                <p class="mb-1 h3">253</p>
                <p class="small text-muted mb-0">Visits</p>
              </div>
              <div class = "px-5">
                <p class="mb-1 h3">1024</p>
                <p class="small text-muted mb-0">Likes</p>
              </div>
            </div>
          </div>
      </div>
    <div id ="profileset" class="CT_all">
      <div id=pimage>photo 
        <!-- <img class= "photo" src=""> -->
      </div>
      <div id=Pbutton>ICON</div>
      <span id="nickname">USER_NICKNAME</span>
    </div>
  </div>
</template>

<script>
export default {
  name:'ProfileInfo'
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
  background-image: url("../assets/bgim_2.jpg");
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
#pimage{
  position: absolute;
  left:2rem;
  top:2rem;
  width: 15rem;
  height: 15rem;
  border-radius: 70%;
  overflow:hidden;
  line-height: 15rem;
  background-color: palevioletred;
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
  background-color: rgb(23, 38, 74);
  color:white;
}
.photo{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
#nickname{
  position:absolute;
  font-size: 3.5rem;
  font-weight: 800;
  color:white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
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


</style>