<template>
 <section class="h-100 gradient-form" style="background-color: #eee;">
        <div class="container py-5 h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-xl-10">
              <div class="card rounded-3 text-black">
                <div class="row g-0">
                  <div class="col-lg-6">
                    <div class="card-body p-md-5 mx-md-4">
                        <div class="text-center">
                            <!-- <img src="/static/logo.png" style="width: 185px;" alt="logo"> -->
                          </div>
                    <form @submit.prevent="signup">
                        <div class="mb-3">
                            <label for="exampleInputEmail1" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="exampleInputEmail1"
                                aria-describedby="emailHelp" v-model="email" placeholder="example@gmail.com" required>
                        </div>
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="username" class="form-control" id="exampleInputEmail1"
                                aria-describedby="emailHelp" v-model="username" placeholder="Username" required>
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputPassword1" class="form-label">Password</label>
                            <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" placeholder="password" required>
                        </div>
                        <div class="mb-3">
                            <label for="exampleInputPassword1" class="form-label">Password again</label>
                            <input type="password" class="form-control" id="exampleInputPassword1" v-model="passwordagain" placeholder="Just one more time!" required>
                        </div>
                        <button type="submit" class="btn btn-danger">Register</button>
                        
                        <div class="d-flex align-items-center justify-content-center pb-4">
                          <p class="mb-0 me-2">Already a reader?</p>
                          <RouterLink to ="/login"><button class="btn btn-outline-danger"> Login </button></RouterLink>
                          </div>

                    </form>
                </div>
            </div>
            <div class="col-lg-6 d-flex align-items-center bg-primary gradient-custom-2" style="background-image: linear-gradient(to right, red, orange   );">
              <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                <h4 class="mb-4">We are more than just an E-Lib</h4>
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
</template>
<style>
.container-white{
    color: white;
}
</style>
<script>
import axios from 'axios'
import { useRouter } from 'vue-router'


export default {
  name: 'Signup',
  data() {
    return {
      username: '',
      password: '',
      passwordagain: '',
      email: '',
      message: "Registered!"
    }
  },
  setup()  {
    const router = useRouter()
    return { router }
  },
  methods: {
    async signup() {
      try {
        const response = await axios.post('http://localhost:5000/api/signup',{
          username: this.username,
          password: this.password,
          passwordagain: this.passwordagain,
          email: this.email  
        })
        alert(response.data.message)
        if(response.data.message == "Signup successful"){
          this.router.push('/login')
        }
      } catch (error) {
        console.error("Error",error)
      }
    }
  }
}
</script>