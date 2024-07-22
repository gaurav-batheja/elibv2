<template>
<div class="row row-cols-1 row-cols-md-1">
<div class="main" style="margin-top: 50px;">
<div class="user_profile">
    <div class="container text-center">
        <div class="row">
            <div class="col-1">
            </div>
            <div class="col">
                <div class="container text-center">
                    <div class="w-50 border-round white-bg row" style="margin-top: 2rem; margin-left: 13%; padding: 2rem;">
                        <div class="col-4">
                            <img src='../assets/static/img/profile_pic.jpg' class="float-start"
                                style="height: 175px; width: 175px; border-radius: 10rem;">
                        </div>
                        <div class="col-7 " style="margin-top: 4rem; margin-left: 2rem;">
                            <div class="user_info">
                                <p> Username - <Strong>user_name </Strong></p>                                          
                                    <p>Books Issued - <strong> totalbooks </strong></p>
                                    <p> Email - <strong>user_mail</strong></p>
                                <p><a class="btn btn-success p-2" href="{{url_for('editprofile',user_id=curr_user.user_id)}}"> &#9998; Edit Profile</a></p>
                         </div>
                     </div>
                </div>
            </div>
            <div class="col-1">
            </div>
        </div>
    </div>
</div>
<br>
</div>
</div>
</div>
<div class="row row-cols-1 row-cols-md-2"></div>
</template>
<script>
import NavView from './NavView.vue';
import { useRouter } from 'vue-router'
export default {
  name: 'UserProfile',
  setup() {
    const router = useRouter()
    return { router }
  },
  components:{
    NavView,
  }}
</script>