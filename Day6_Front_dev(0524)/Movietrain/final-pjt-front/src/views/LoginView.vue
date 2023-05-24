<template>
  <div class="login">
    <section class="vh-100 gradient-form" >
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-xl-10">
            <div class="card rounded-4 text-black custom-card-size">
              <div class="row g-0">
                <div class="col-lg-6">
                  <div class="card-body p-md-5 mx-md-4">
                    <div class="text-center">
                      <img src="../assets/TempLogo.png" class="rounded-2"
                        style="width: 18rem;" alt="logo">
                      <h4 class="mt-1 mb-4 pb-1"> </h4>
                    </div>

                    <form>
                      <h2 class="mb-4 TEXT">Log in</h2>

                      <div class="form-outline">
                        <input type="email" id="form2Example11" class="form-control"
                          placeholder="User ID or email address" />
                        <label class="form-label" for="form2Example11"></label>
                      </div>

                      <div class="form-outline mb-3">
                        <input type="password" id="form2Example22" class="form-control" placeholder="Password" />
                        <label class="form-label" for="form2Example22"></label>
                      </div>

                      <div class="d-flex align-items-center justify-content-center pb-5">
                        <!-- <p class="mb-0 me-2">Don't have an account?</p> -->
                         <router-link to="/"><button type="button" class="btn btn-success mx-2">Log In</button></router-link>
                        <router-link to="/"><button type="button" class="btn btn-outline-success mx-2">Go Back</button></router-link>
                      </div>
                      <div class="d-flex align-items-center justify-content-center ">
                        <!-- <p class="mb-0 me-2">back</p>
                        <button type="button" class="btn btn-outline-danger">Create new</button> -->
                      </div>

                      <p class="text-center text-muted mt-1 mb-0">Don't have an account? <router-link to="/signup"
                        class="fw-bold text-body TEXT"><u>Sign UP</u></router-link></p>

                    </form>

                  </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center image-background">
                  <div class="px-3 py-4 p-md-5 mx-md-4">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LoginView'
}
</script>

<style scoped>

html, body {
  height: 100vh;
  margin: 0;
  padding: 0;
}

body {
    background-color: #000;
}

.gradient-form {
  background-image: 
    /* linear-gradient(to bottom, rgba(0,0,0,0) 60%, rgba(0,0,0,1) 100%), */
    linear-gradient(90deg, rgba(149, 255, 207, 0.3), rgba(255, 146, 215, 0.3)),
    url(../assets/bg4.png);
  background-position: center bottom 20%;
  /* filter: blur(8px);  */
  
}

 .custom-card-size {
    max-width: 800px;  /* 원하는 크기로 조절하세요 */
    margin-top:auto;
    margin-bottom:auto;
    background-color:rgb(30, 29, 29);
    box-shadow: 0px 0px 2rem rgba(255, 247, 0, 0.2), inset 0px 3px 1rem rgba(255, 255, 255, 0.1);
    opacity: 100%;
  }

  .image-background {
    background-image: url('../assets/trainticket4.jpg');
    /* background-color: blue; */
    background-position:center;
    overflow: hidden;
    background-size:cover;
    border-top-right-radius: 1rem; /* 추가 */
    border-bottom-right-radius: 1rem; /* 추가 */
  }
  
  
  .TEXT{
    background: -webkit-linear-gradient(top, rgb(15, 186, 124), rgb(0, 251, 255));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;  /* 원하는 굵기로 변경 가능 */
    line-height: 1.5;  /* 'g' 문자가 잘리지 않도록 높이를 조정 */
    padding-bottom: 5px;  /* 필요한 경우 아래쪽에 여백을 추가 */
    overflow: visible;  /* 문자가 박스 바깥으로 나가도 잘리지 않게 함 */
  }

  .rounded-2 {
    transform: translateX(-20px); /* 왼쪽으로 20px 만큼 이동 */
  }
  .form-control:focus {
  background-color: #e9ecef;  /* 배경색 변경 */
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15), 0 0 0 0.2rem rgba(0, 255, 217, 0.5);  /* 그림자 추가 */
}
  @media (max-width: 768px) {
  .image-background {
    display: none !important;
  }
}
</style>