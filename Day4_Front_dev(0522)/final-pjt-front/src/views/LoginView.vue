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
                      <h3 class="mb-4">Log in</h3>

                      <div class="form-outline ">
                        <input type="email" id="form2Example11" class="form-control"
                          placeholder="User ID or email address" />
                        <label class="form-label" for="form2Example11"></label>
                      </div>

                      <div class="form-outline mb-3">
                        <input type="password" id="form2Example22" class="form-control" placeholder="Password" />
                        <label class="form-label" for="form2Example22"></label>
                      </div>

                      <!-- <div class="text-center pt-1 mb-5 pb-1">
                        <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button">Log
                          in</button>
                        <a class="text-muted" href="#!">Forgot password?</a>
                      </div> -->

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
                        class="fw-bold text-body"><u>Sign UP</u></router-link></p>

                    </form>

                  </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                  <div class="px-3 py-4 p-md-5 mx-md-4">
                    <h4 class="mb-4">We are more than just a company</h4>
                    <p class="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                      exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
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

<style>

/* html, body {
  height: 100vh;
  margin: 0;
  padding: 0;
}

body {
    background-color: #000;
}

.gradient-form {
  background-image: 
    linear-gradient(to bottom, rgba(0,0,0,0) 10%, rgba(0,0,0,1) 100%),
    url(../assets/bg2.png);
} */

 .custom-card-size {
    max-width: 800px;  /* 원하는 크기로 조절하세요 */
    margin-top:auto;
    margin-bottom:auto;
  }

</style>