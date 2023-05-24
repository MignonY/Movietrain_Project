<template>
<div class="profile">
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

</style> 