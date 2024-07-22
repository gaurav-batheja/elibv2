import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUp from '../../authorization/SignUp.vue'
import LoginView from '../../authorization/LoginView.vue'
import AdminLogin from '../../authorization/adminLogin.vue'
import UserProfile from '@/components/UserProfile.vue'


const routes= [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
      meta: { requiredAuth: true },
      children: [
        {
          path : '/userprofile',
          name : 'userprofile',
          component : UserProfile
        }
      ]
    },
    {
      path : '/signup',
      name : 'Signup',
      component : SignUp
    }, 
    {
      path : '/login',
      name : 'LoginView',
      component : LoginView
    },
    {
      path : '/adminlogin',
      name : 'adminLogin',
      component : AdminLogin
    },

  ]
// const isAuthenticated = localStorage.getItem('token')
// console.log(!Boolean(isAuthenticated),"hi")

// if(!Boolean(isAuthenticated)){
//   console.log("inside router")
//   // next({ name: 'userlogin' })
//   router.push("/login")
//   console.log("pushed")
// }

// Global navigation guard
const router = createRouter({
  history: createWebHistory(),
  routes
})

// Global navigation guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const isAuthenticated = !!token // Converts token to boolean

  console.log(`Is Authenticated: ${isAuthenticated}`)

  if (to.name === "HomeView" && !isAuthenticated) {
    console.log('Not authenticated, redirecting to login')
    next({ name: 'LoginView' })
  } else if (to.name === 'LoginView' && isAuthenticated) {
    console.log('Authenticated user attempting to access login, redirecting to home')
    next({ name: 'HomeView' })
  } else {
    next()
  }
})
export default router
