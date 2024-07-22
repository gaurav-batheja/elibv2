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
  
                  <form @submit.prevent="login">
                    <p>Admin Login for Read Hub</p>
  
                    <div data-mdb-input-init class="form-outline mb-4">
                      <input type="name" id="form2Example11" class="form-control"
                        placeholder="Username" v-model="username" required>
                    </div>
  
                    <div data-mdb-input-init class="form-outline mb-4">
                      <input type="password" id="form2Example22" class="form-control" v-model="password" placeholder="password" required>
                    </div>
                    <button type="submit" class="btn btn-danger">Login</button>
  
                    <div class="d-flex align-items-center justify-content-center pb-4">
                      <p class="mb-0 me-2">Not an admin?</p>
                      <RouterLink to="/login"><button class="btn btn-outline-danger">User login</button></RouterLink>
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

<script>

import axios from 'axios'
import { useRouter } from 'vue-router'


export default {
name: 'UserLogin',
data() {
return {
  username: '',
  password: ''
}
},
setup()  {
const router = useRouter()
return { router }
},
methods: {
async login() {
  try {
    const response = await axios.post('http://localhost:5000/api/adminlogin', {
      username: this.username,
      password: this.password
    })
    console.log(response.data.message)
    if(response.data.message == 'Invalid name or password'){
      alert("User Not Found")
      return this.router.push('/login')
    }
    else{

    const token = response.data.access_token
    const user_info = response.data.user_info
    localStorage.setItem('token', token)
    localStorage.setItem('user_info',JSON.stringify(user_info))
    console.log(token)
    alert(response.data.message)
    this.router.push('/')
    }
  } catch (error) {
    console.error('There was an error!', error)
  }
}
}
}

</script>
