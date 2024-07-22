<template>
<div class="navbar-nav ms-auto d-flex flex-row mt-3 mt-lg-0" style="margin-top: 2rem;">
    <li class="nav-link text-center mx-2 mx-lg-1">
      <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Add Section</button>
</li>
<li class="nav-link text-center mx-2 mx-lg-1">
  <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Add Book</button>
</li>
<!-- <ul><a href='{{url_for("sections")}}'>Sections</a></ul> -->
<!-- <ul><a href='{{url_for("viewbook")}}'>All Books</a></ul> -->
<!-- <ul><a href='{{url_for("viewreq")}}'>Upcoming Requests</a></ul> -->
 <li class="nav-link text-center mx-2 mx-lg-1">
  <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">All Users</button>
</li>
<!-- <a class="btn white" href='{{url_for("addadmin")}}'>Make Admin</a>
<a class="btn white" href='{{url_for("deladmin")}}'>Delete Admin</a> -->
<li class="nav-link text-center mx-2 mx-lg-1">
  <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Plots</button>

</li>
<li class="nav-link text-center mx-2 mx-lg-1">
  <button @click="navigateTo('userprofile')" class="nav-link" style="color: white;">Feedbacks</button>
</li>
</div>
</template>
<script>
// import axios from 'axios'
// import AdminNav from './AdminNav.vue'
import { useRouter } from 'vue-router'

export default {
  name: 'AdminNav',
  setup() {
    const router = useRouter()

    const navigateTo = (component) => {
      router.push({ name: `${component}` })
    }

    return { router ,navigateTo}
    
  }}
  </script>