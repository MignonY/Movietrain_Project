<template>
  <div class="main">
    <!-- <img alt="templogo" src="../assets/TempLogo.png"> -->
    <MovieRecTrain msg="MainRecommend_Train"/>
    <!-- <HelloWorld msg="Temp_Reference"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
//추가되는 컴포넌트 import 필수, export components에 추가 필수 
// import HelloWorld from '@/components/HelloWorld.vue'
import MovieRecTrain from '@/components/MovieRecTrain.vue'

export default {
  name: 'MAIN',
  components: {
    // HelloWorld,
    MovieRecTrain,
  }
}
</script>
