<template>
  <div class="movie-rec-train mt-5 mb-5 w-50 h-auto justify-contents-center align-contents m-auto animated-slide">
    <div class="train-container">
      <div v-for="movie in randomMovies" :key="movie.id" class="train-card">
        <div class="card">
          <router-link :to="{
          name: 'MovieView',
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
  </div>
</template>>

<script>
export default {
  name: 'MovieRecTrain',
    computed: {
    movies() {
      // Vuex store에서 영화 리스트를 가져오는 로직
      return this.$store.state.movies;
    },
    randomMovies() {
      // 랜덤으로 3개의 영화를 선택하는 로직
      const shuffledMovies = this.shuffleArray(this.movies);
      return shuffledMovies.slice(0, 3);
    }
  },
  methods: {
    shuffleArray(array) {
    let copyArray = [...array]; // 배열을 복사
    let currentIndex = copyArray.length, temporaryValue, randomIndex;
    while (currentIndex !== 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
      temporaryValue = copyArray[currentIndex];
      copyArray[currentIndex] = copyArray[randomIndex];
      copyArray[randomIndex] = temporaryValue;
    }
    return copyArray;
  }
  }
}
</script>

<style scoped>

.movie-rec-train {
  background-color: black;
  border-radius: 10px;
  padding: 20px;
  /* 애니메이팅 관련 코드  */
  opacity: 0; /* 초기에 투명도를 0으로 설정 */
  transform: translateX(100%); /* 초기 위치를 오른쪽으로 이동 */
  animation: slide-in 0.5s forwards; /* 애니메이션 효과를 적용 */
}

.train-container {
  display: flex;
  justify-content: space-between;
  /* width: 80%; 
  margin: auto;  */
}

.train-card {
  /* flex: 0 0 30%;  */
  margin-right: 0.5rem;
  margin-left: 0.5rem;
}

.card-img-top{
  width: 100%;  
  height: 100%; 
  object-fit: cover;
  background-color: black; 
  border: 1px solid #000;
  background-image: linear-gradient(to bottom, rgba(255,255,255,0), rgba(0,0,0,1)); 
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

/* 애니메이팅 관련 */
@keyframes slide-in {
  0% {
    opacity: 0;
    transform: translateX(100%);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

</style>