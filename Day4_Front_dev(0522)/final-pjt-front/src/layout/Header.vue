<template>
<div class = "header">
  <nav class="navbar navbar-expand navbar-dark flex-column flex-md-row bd-navbar bg-dark">
    <div class="row w-100 m-0 align-items-center">
      <div class="navbar_left col-xxl-3 d-flex align-items-center">
        <router-link to="/" class="navbar-brand">
          <img id="navlogo" class="" alt="templogo" src="../assets/TempLogo.png" height="40" witdh="100%">
        </router-link>
        <ul class="navbar-nav d-flex">
          <li><router-link to="/" class="nav-item px-3">HOME</router-link></li>
          <li><router-link to="/" class="nav-item px-3">COMMUNITY</router-link></li>
        </ul>
      </div>
      <div class="navbar_mid flex-grow-1 col-xl-auto col-wrap">
        <form class="form-inline w-10 d-flex ">
          <div class="dropdown me-1">
            <b-dropdown text="Category" variant="outline-success" class="s-1">
              <b-dropdown-item href="#">MOVIE</b-dropdown-item>
              <b-dropdown-item href="#">COMMUNITY</b-dropdown-item>
              <b-dropdown-item href="#">USER</b-dropdown-item>
            </b-dropdown>
          </div>
          <input class="form-control input-lg w-100" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-success ms-1" type="submit">Search</button>
        </form> 
      </div>
      <div class="navbar_right col-md-2 d-flex">
        <ul class="navbar-nav  justify-content-between">
          <li><router-link to="/Profile" class='nav-item px-3'>PROFILE</router-link></li>
          <li><router-link to="/Login" class='nav-item px-3'>LOGIN</router-link></li>
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
  /* color:gray; */
  color:#42b983;
  font-weight:normal;
  text-decoration : none;
}

</style>