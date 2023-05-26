<template>
  <div id="defaultlayout">
    <Header></Header>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './Header';
import Footer from './Footer';
export default{
  name:'DefaultLayout',
  components:{
    Header,
    Footer,
  }
}
</script>

<style>

</style>