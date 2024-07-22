
<template>
    <!-- <div class="container"> -->
        <nav class="navbar navbar-expand-lg bg-body-tertiary gradient-custom">
            <div class="container">
              <a class="navbar-brand"><RouterLink to ="/" style="text-decoration: none;color: white;">Read Hub</RouterLink></a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">

                    <ul class="navbar-nav ms-auto d-flex flex-row mt-3 mt-lg-0">
                        <li class="nav-link text-center mx-2 mx-lg-1">
                          <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Books</button>
                          
                        </li>
                        <li class="nav-link text-center mx-2 mx-lg-1">
                          <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Sections</button>
                            
                        </li>
                        <li class="nav-link text-center mx-2 mx-lg-1">
                          <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Requests</button>
                        </li>
                    </ul>
                    <form action="/search" method="POST" class="d-flex input-group w-auto ms-lg-2 my-1 my-lg-0 mx-auto">
                        <input type="search" class="form-control" placeholder="Search" aria-label="Search" name="query"
                            required>
                        <button class="btn btn-light" type="submit" data-mdb-ripple-color="dark">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-search" viewBox="0 0 16 16">
                                <path
                                    d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
                            </svg>
                        </button>
                        <!-- Conditionally render AdminNav based on isAdmin -->
                    <AdminNav v-if="isAdmin" />
                    </form>
              
                    <ul class="navbar-nav ms-auto d-flex flex-row mt-3 mt-lg-0">
                      <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;"><img src="../assets/static/img/profile_pic.jpg"alt="Profile Pic" width="40" height="40"></button>
                    <!-- <RouterLink to ="/userprofile"><img src="../assets/static/img/profile_pic.jpg" alt="Profile Pic" width="40" height="40"></RouterLink> -->
                        <li class="nav-item text-center mx-2 mx-lg-1"></li>
                        <button class="btn btn-outline-danger" @click="logout()">Logout</button>
                    </ul>

                </div>
            </div>
        </nav>
    <!-- </div> -->
</template>

<style>
.btn {
    padding: .45rem 1.5rem .35rem;
    color: white;
  }
.nav-link {
  color: white;
  text-decoration-color: white;
}
  
  .gradient-custom {
    background: -webkit-linear-gradient(to right, red, orange,orange);
  
    background: linear-gradient(to right, red, orange,orange)
  }
  .white {
    color: rgb(255, 255, 255);
  }
  .white-bg {
    background-color: rgba(245, 245, 245, 0.83);
  }
  .no-decor {
    text-decoration: none;
    box-decoration-break: none  ;
  }
  body {
    background-image: url("/static/bookbg.jpg");
    background-color: #cccccc; /* Used if the image is unavailable */
    height: auto; /* You must set a specified height */
    background-position: center; /* Center the image */
    background-repeat: no-repeat; /* Do not repeat the image */
    background-size: cover; /* Resize the background image to cover the entire container */
  }
</style>

<script>
import axios from 'axios'
import { ref } from 'vue'
import { jwtDecode } from "jwt-decode"
import AdminNav from './AdminNav.vue'
import { useRouter } from 'vue-router'

export default {
  name: 'NavView',
  components:{
    AdminNav,
  },
  setup() {
  const router = useRouter()
  const isAdmin = ref(false)
  // Check token and decode it
  const check = localStorage.getItem('token')
  if (check) {
    try {
      const decodedToken = jwtDecode(check)
      isAdmin.value = decodedToken.is_administrator
      console.log("Admin",isAdmin)
    } catch (error) {
      console.error('Failed to decode token:', error)
    }
    }
    const navigateTo = (component) => {
      router.push({ name: `${component}` })
    }

    return { router, isAdmin ,navigateTo}
  },
  methods: {
    async logout() {
      try {
        const access_token = localStorage.getItem("token")
        await axios.post('http://localhost:5000/api/logout', {}, {
          headers: {
            Authorization: `Bearer ${access_token}`
          }
        })
        localStorage.removeItem('token')
        localStorage.removeItem('user_info')
        this.router.push('/login')
      } catch (error) {
        console.error('Error during logout:', error)
      }
    }
  }
}
</script>