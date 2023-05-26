<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link :to="{name: 'HomeView'}">Movies</router-link>|</li> 
        <li>
          <router-link :to="{name: 'PostView'}">Community</router-link>|
          <!-- <router-link to="/Post">Community</router-link>  -->
        </li>
        <!-- :to="{name: SearchView} -->
       <router-link :to="{name: 'SearchView'}">
          <form @enter.prevent="searchMovie">
            <input type="text" id="title" v-model.trim="title">
          </form>
        </router-link>

        <div>
        <li v-if="!$store.state.username">
          <router-link :to="{ name: 'SignUpView' }">SignUp</router-link> | 
          <router-link :to="{ name: 'LoginView' }">Login</router-link>
        </li>
        <li v-if="$store.state.username">
          <a @click="logout">Logout</a> |
          <router-link :to="{ name: 'ProfileView', params: {id : $store.state.id} }">Profile</router-link> 
        </li>
        </div>
      </ul>
    </nav>
    <router-view/>
  </div>
</template>


<script>

export default {
  data() {
    return {
      isLoggedIn : false, 
      title : null,
    }
  },
  mounted() {
    this.isLoggedIn = true
  },
  methods:{
    searchMovie(){
      this.$store.state.title = this.title
      console.log(this.$store.state.title)
      this.$store.dispatch('searchMovie')
    },

    logout() {
      this.$store.commit('LOGOUT');
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
