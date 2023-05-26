<template>
<div class = "header">
  <nav class="navbar navbar-expand navbar-dark flex-column flex-md-row bd-navbar bg-dark">
    <div class="row w-100 m-0 align-items-center">
      <router-link to="/" class="na-item col-sm-1 col-auto">
        <img id="navlogo" class="" alt="templogo" src="../assets/TempLogo.png" height="50">
      </router-link>
      <div class="navbar_left col-sm-2 d-flex">
        <ul class="navbar-nav flex-sm-row">
          <router-link to="/" class ='nav-item m-2'>HOME</router-link>
          <router-link to="/" class ='nav-item m-2'>COMMUNITY</router-link>
        </ul>
      </div>
      <div class="navbar_mid flex-grow-1 col">
        <form class="form-inline w-10 d-flex flex-sm-row">
          <input class="form-control input-lg w-100" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-success ms-1" type="submit">Search</button>
        </form> 
      </div>
      <div class="navbar_right col-sm-2 d-flex">
        <ul class="navbar-nav ml-auto flex-sm-row">
          <router-link to="/Profile" class ='nav-item m-2'>Profile</router-link>
          <router-link to="/Login" class ='nav-item m-2'>Login</router-link>
        </ul>
      </div>
    </div>
  </nav>
</div>
</template>

<script>
export default {
  name: 'HeaderLayout',
}
</script>

<style scoped>
.nav-item{
  color:gray;
  font-weight:normal;
  text-decoration : none;
}
</style>