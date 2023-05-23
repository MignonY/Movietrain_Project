<template>
  <div>
    <div class="card">
      <div class="image-container">
      <router-link :to="{
      name: 'MovieDetailView',
      params : {id: movie.id}}">
        <img :src="'https://image.tmdb.org/t/p/w780' + movie.poster_path" alt="Movie Poster" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">{{ movie.title }}</h5>
          <!-- <p class="card-text">{{ movie.description }}</p> -->
        </div>
       </router-link>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }

}
</script>

<style scoped>
.card-img-top{
  width: 100%;  
  height: 100%; 
  object-fit: cover;
  background-color: black; 
  border: 1px solid #000;
  background-image: linear-gradient(to bottom, rgba(255,255,255,0), rgba(0,0,0,1)); 
}

.image-container {
  position: relative;
  overflow: hidden;
}

.card {
  flex: 1 0 auto;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  /* hover 관련 구현 */
  position: relative;
  overflow: hidden;
  transition: 0.3s;
  text-align:center;
}
.card:hover {
  transform: scale(1.05);
}

.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 반투명한 검은색 배경 */
  opacity: 0;
  transition: 0.3s;
}

.card:hover::before {
  opacity: 1;
}

.card-title {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 1rem;
  margin: 0;
  background-color: rgba(0, 0, 0, 0.7); /* 반투명한 검은색 배경 */
  color: white;
  opacity: 0;
  transition: 0.3s;
  font-size:1rem;
  /* transform: translateY(100%); */
}

.card:hover{
  filter: brightness(70%); /* 이미지 밝기 조절 */
  transform: scale(1.05);
  transition: filter 0.3s, transform 0.3s;
  box-shadow: 0 0 20px rgba(242, 255, 0, 0.5); /* outer glow 효과 */
}

.card:hover .card-title {
  opacity: 1;
  text-align:center;
  /* transform: translateY(0); */
}
</style>