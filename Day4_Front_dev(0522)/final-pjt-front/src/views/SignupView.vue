<template>
  <div>
    <section class="vh-100 bg-image"
      style="background-image: url('');">
    <!-- <section class="vh-100 bg-image"
      style="background-image: url('https://mdbcdn.b-cdn.net/img/Photos/new-templates/search-box/img4.webp');"> -->
      <div class="mask d-flex align-items-center h-100 gradient-custom-3">
        <div class="container h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-9 col-lg-7 col-xl-6">
              <div class="card" style="border-radius: 15px;">
                <div class="card-body p-5">
                  <h2 id= "CA" class="text-uppercase text-center mb-5">Create an account</h2>

                  <form>

                    <div class="form-outline mb-1">
                      <input type="text" id="form3Example1cg" class="form-control form-control-lg" placeholder="Your Name" />
                      <label class="form-label" for="form3Example1cg"></label>
                    </div>

                    <div class="form-outline mb-1">
                      <input type="email" id="form3Example3cg" class="form-control form-control-lg" placeholder="Your Email" />
                      <label class="form-label" for="form3Example3cg"></label>
                    </div>

                    <div class="form-outline mb-1">
                      <input type="password" id="form3Example4cg" class="form-control form-control-lg" placeholder="Password" />
                      <label class="form-label" for="form3Example4cg"></label>
                    </div>

                    <div class="form-outline mb-1">
                      <input type="password" id="form3Example4cdg" class="form-control form-control-lg" placeholder="Confirm password" />
                      <label class="form-label" for="form3Example4cdg"></label>
                    </div>

                    <div class="form-check d-flex justify-content-center mb-4">
                      <input class="form-check-input me-2" type="checkbox" value="" id="form2Example3cg" />
                      <label class="form-check-label" for="form2Example3g">
                        I agree all statements in <a href="#!" class="text-body"><u>Terms of service</u></a>
                      </label>
                    </div>

                    <div class="d-flex justify-content-center">
                      <button type="button"
                        id="butt" class="btn btn-success btn-lg">Register</button>
                    </div>

                    <p class="text-center text-muted mt-4 mb-0">Have already an account? <router-link to="/login"
                        class="fw-bold text-body"><u>Login here</u></router-link></p>
                    <p class="text-center text-muted mt-1 mb-0"><router-link to="/"
                        class="fw-bold text-body"><u>Go Main</u></router-link></p>

                  </form>

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
  name: 'SignupView',

}
</script>

<style>
  /* #butt{
    background: linear-gradient(to right, rgba(0, 255, 225, 0.5), rgba(2, 96, 49, 0.5))
  } */
  #CA{
    font-weight:900;
  }
</style>