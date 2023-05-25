<template>
  <div class="full-screen-bg" :style="backgroundImageStyle">
    <div class="FI1 d-flex align-items-center justify-content-center" style="height: 40vh;">
      <iframe class="YTV" width="629" height="350" :src="video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    <!-- <div class="FI2 custom-style flex-container">
      <div class="row1">Row 1</div>
      <div class="row2">Row 2</div>
      <div class="row3">Row 3</div>
    </div> -->
  
    <div class="flex-grow-1">
      <h1 class="Mtitle">" "</h1>
      <div class="FI2 align-items-stretch exclude p-2">
       
        <div class="row w-100">
          <div class="col-md-4 p-2 d-flex align-items-start justify-content-center">
            <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path" alt="Movie Poster" class="POSTER img-fluid">
          </div>
          <div class="col-md-8 px-4 d-flex flex-column align-items-start justify-content-start">
            <h1 class="MTitle">{{ movie.title }}</h1>
            <b class="MTitle my-3">장르: {{ getGenreNames() }}</b>
            <b class="text-muted my-3">{{ movie.overview }}</b>
          </div>
        </div>
        <div class="row w-100 mt-4 flex-column align-items-start justify-content-start">
          <h1 class="text-white">평점,리뷰</h1>
          
          <form id="ratingForm" @submit.prevent="submitForm">
      
            <div class="d-flex align-items-center justify-content-start">
              
              <div>
                <font-awesome-icon style="color: yellow"
                v-for="(star, index) in 5" 
                :key="index"
                :icon="getStarIcon(star)" 
                @click="setRating(star)"></font-awesome-icon>
              </div>

              <div class="form-group ms-2 d-flex align-items-center">
                <label for="comment"></label>
                <textarea id="comment" v-model="form.comment" class="form-control custom-textarea" required></textarea>
              </div>

              <button type="submit" class="btn btn-success ms-1 align-self-center">평가</button>

            </div>

          </form>

          <div v-for="(review, index) in reviews" :key="index" class="review">
            <div class="d-flex align-items-start justify-content-start">
              <div>
                <font-awesome-icon style="color: yellow"
                v-for="star in Array(review.rating).fill(0)" 
                :key="star"
                icon="star"></font-awesome-icon>
              </div>
              <div class="form-group d-flex align-items-start ms-3">
                
                <p class="text-white">{{ review.comment }}</p>
              </div>
            </div>
          </div>
          
        </div>

     
        <div class="row w-100 mt-4 p-5">
          <h2 class="MTitle">관련 추천 영화</h2>
          <div class="card-group">
            <div class="card" v-for="randomMovie in randomMovies" :key="randomMovie.id">
              <img class="card-img-top" :src="'https://image.tmdb.org/t/p/w300' + randomMovie.poster_path" alt="Movie Poster">
              <div class="card-body">
                <p class="card-title">{{ randomMovie.title }}</p>
                <p class="card-text"> ★{{ randomMovie.vote_average }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
// import axios from 'axios'
// import {route} from 'vue-router'
export default {
  data() {
    return {
      movie : null,
      video: null,
      similarMovies: [],  
      randomMovies: [],
      rating : 0,
      form: {
      rating : 0,
      comment: '',
      },
      reviews: [],
    };
  },
  computed: {
    backgroundImageStyle() {
      return this.movie && this.movie.poster_path 
        ? { '--background-image': `url('https://image.tmdb.org/t/p/original${this.movie.poster_path}')`, 
            '-background-image': `url('https://image.tmdb.org/t/p/720${this.movie.poster_path}')` }
        : {};
    }
  },
  created() {
    this.detailmovies()
    this.videodetail()
    // this.getMoviesByGenre()
    this.getRandomMovies()
  },
    // const movieId = ${this.$route.params.id}
  methods:{
        detailmovies() {
      const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM'
          }
        };

      const URL = 'https://api.themoviedb.org/3/movie/'
      const movieId = `${this.$route.params.id}`;
      const language= 'ko-KR'
      const full = URL + movieId + '?language=' + language
      // console.log(full)
      fetch( full, options)
      // fetch(
      //   'https://api.themoviedb.org/3/movie/27505?language=ko-KR', options)
        .then(response => response.json())
        .then(response => {
        console.log(response)
        this.movie = response
        this.getSimilarMovies()
        // this.$store.state.movie = response
        }
        )
        .catch(err => console.error(err));
      },
     submitForm() {
    // 평점과 코멘트를 reviews 배열에 추가
    this.reviews.push({
      rating: this.rating,
      comment: this.form.comment
    });
    // 평점과 폼을 초기화
    this.rating = 0;
    this.form.comment = '';
  },
    getStarIcon(star) {
  // if the current star is less or equal to the rating, return 'fas', 
  // which is a solid star; otherwise return 'far', which is an empty star.
  return this.rating >= star ? ['fas', 'star'] : ['far', 'star'];
},
  setRating(star) {
    // when a star is clicked, set the rating to the current star.
    this.rating = star;
  },

    videodetail(){
      const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM'
        }
      }

      const URL = 'https://api.themoviedb.org/3/movie/'
      const movieId = `${this.$route.params.id}`;
      const language= 'ko-KR'

      const FULL = URL + movieId + '/videos?language=' + language 
    fetch(FULL, options)
    .then(res => res.json())
    .then(res => {
      const youtube = 'https://www.youtube.com/embed/'
      const parameters = '?modestbranding=1&rel=0'

      this.video = youtube + res.results[0].key+parameters
      
    }
    )
    .catch(err => console.error(err));
    },

    getGenreIds() {
    if (!this.movie || !this.movie.genres) {
      return [];
    }

    const genreIds = this.movie.genres.map(genre => genre.id);
    return genreIds;
  },


    getGenreNames() {
      if (!this.movie || !this.movie.genres) {
        return '';
      }
      
      const genreNames = this.movie.genres.map(genre => genre.name);
      return genreNames.join(', ');
    },

    getRandomMovies() {
  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM'
    }
  };

  fetch('https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc', options)
    .then(response => response.json())
    .then(data => {
      this.randomMovies = data.results.slice(0, 5);  // Get the first 5 elements from the data array
    });
},
    getSimilarMovies() {
  const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmJmNTMzY2FlODMwYmUzNzIwN2MxNGE1ZGU1MjVmNyIsInN1YiI6IjYzZDIwM2M4ZTcyZmU4MDA4ZTYxMTAwMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.krANda0Rl0-V-oSH7YOOWJzF9WaJmj3uZfDNhOdbakM'
    }
  };

  const genreIds = this.getGenreIds().join(',');

  fetch(`https://api.themoviedb.org/3/discover/movie?with_genres=${genreIds}&sort_by=vote_average.desc`, options)
    .then(response => response.json())
    .then(data => {
      this.similarMovies = data.results.slice(0, 5);  // Get the top 5 movies
    });
},
  
  },
  
}
</script>


<style scoped>
.full-screen-bg {
  width: 100%;
  height: auto;
  position: relative;
  overflow: hidden;
  background-color: black;
  z-index:0;
  /* isolation: isolate; */
}

.full-screen-bg::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh !important;
  width: 100%;
  background-image: var(--background-image) ;
  background-position: center top;
  background-repeat: no-repeat;
  background-size: 100% auto;
  z-index:0;
  /* isolation: isolate; */
}

.full-screen-bg::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  min-height: 100%;
  width: 100%;
  background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgb(0, 0, 0) 50%);
  opacity: 100%;
  z-index:0;
  /* isolation: isolate; */
}

.row{
  /* background-color: black; */
  z-index: 1;
  position: relative; 
}
.FI1{
  margin-top:2rem;
  margin-bottom:2rem;
  /* background-image: url(../assets/Exclude.png); */
  
  background-position: center;
  background-repeat: no-repeat;
  z-index: 2;
  position: relative; 
  /* opacity: 100%; */
}
.FI2:not(.exclude){
  background-color: white;
  opacity:100%;
  border-radius:1rem;
  z-index:2;
}
.FI3:not(.exclude){
  /* background-color: aquamarine !important; */
  opacity: 80% !important;
  border: radius 0.5rem !important;
  z-index: 2 !important;
}
.FI4:not(.exclude){
  /* background-color: pink !important; */
  /* opacity: 80% !important; */
  border: radius 0.5rem !important;
  z-index: 2 !important;
}
.YTV {
  border-radius: 15px;
}
.POSTER{
  border-radius: 8px !important;
}
.MTitle{
  color:white;
  font-weight:800;
}
.STitle{
  color:white;
  font-weight:600;
}

@media (min-width: 768px) {
  .flex-grow-1 {
    max-width: 70%;
    margin: auto; 
  }
}

.custom-style{
  background-color: white;
  position:relative;
  z-index:1;
  isolation: isolate;
}
.card-title{
  font-size:0.75rem;
}
.custom-textarea {
  height: 1rem;
  width: 100%; 
}
</style>