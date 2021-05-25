<template>
	<div class="admin-post-page">
		<section class="update-form">
			<form @submit.prevent="onSave">
				<AppControlInput id="firstname" v-model="information.firstname">First Name</AppControlInput>

				<AppControlInput v-model="information.lastname">Last Name</AppControlInput>

				<AppControlInput v-model="information.email">Email</AppControlInput>

				<AppControlInput v-model="information.username">Username</AppControlInput>

				<AppControlInput v-model="information.phone">phone</AppControlInput>
				
				<AppButton type="submit">Save</AppButton>

				<AppButton type="button" style="margin-left: 10px" btn-style="cancel" @click="onCancel">Cancel</AppButton>
			</form>
		</section>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import User from "@/components/User/User"
export default {
    name: 'UserProfile',
    middleware: ['auth'],
		computed:{
      information: {
        get(){
          var info = []
          info = this.$store.state.user.user
          return {
            email: info[0],
            firstname: info[1],
            lastname: info[2],
            username: info[3],
            phone: info[5]
          }
        },
        set(value){
          info.push(value)
        }
      },
			 },
		methods: {
			onSave(){
				this.$store.dispatch('user/updateUser', {
					first_name: this.information.firstname,
					last_name: this.information.lastname,
					email: this.information.email,
					username: this.information.username,
					phone: this.information.phone
				}).then(() => {this.$router.push("/")})
		},
		onCancel() {
      // NAvigate Back
      this.$router.push("/");
    }
	}
}
</script>

<style scoped>
.update-form {
  width: 90%;
  margin: 20px auto;
}
@media (min-width: 768px) {
  .update-form {
    width: 500px;
  }
}
</style>