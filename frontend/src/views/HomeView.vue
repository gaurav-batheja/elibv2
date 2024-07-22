


<template>
<div>
    
<NavView />
<router-view />
<!-- <img src='../assets/static/img/bookbg.jpg' style="height: max-content;width: 1520.5px;"> -->

</div>
</template>
<script>

import NavView from '../components/NavView.vue'
import UserProfile from '@/components/UserProfile.vue';
import { useRouter } from 'vue-router'


export default {
  name: 'HomeView',
  components:{
    NavView,
  },
  setup() {
  const router = useRouter()

return router }}

</script>