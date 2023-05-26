<template>
<div class="vh-100 bg-image profile">
  <ProfileInfo></ProfileInfo>
  <ProfileUserHistory></ProfileUserHistory>
  <!-- <router-link to="/" class="logo">Home</router-link> -->
  <!-- <b>must be changed</b> -->
</div>
</template>

<script>
import ProfileInfo from '@/components/ProfileInfo'
import ProfileUserHistory from '@/components/ProfileUserHistory'

export default {
  name: 'ProfileView',
  components:{
    ProfileInfo,
    ProfileUserHistory,
  }
}
</script>

<style>
.bg-image {
  background-image: 
    /* linear-gradient(to bottom, rgba(0,0,0,0) 60%, rgba(0,0,0,1) 100%), */
    linear-gradient(90deg, rgba(149, 255, 207, 0.3), rgba(255, 146, 215, 0.3)),
    url(../assets/bg2.png);
  background-position: center bottom 10%;
  /* filter: blur(8px);  */
}
  
</style> 