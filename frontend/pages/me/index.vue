<template>
	<div class="admin-post-page">
		<section class="update-form">
			<form @submit.prevent="onSave">
				<AppControlInput v-model="info[1]">FirstName</AppControlInput>

				<AppControlInput v-model="info[2]">Lastname</AppControlInput>

				<AppControlInput v-model="info[0]">Email</AppControlInput>

				<AppControlInput v-model="info[3]">Username</AppControlInput>

				<AppControlInput v-model="info[5]">phone</AppControlInput>
				
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
    components: User,
    middleware: ['auth'],
		computed:{
			 ...mapGetters({info: 'userData'})
			 },
		date(){
			return{
				email: info[0],
				first_name: info[1],
				last_name: info[2],
				username: info[3],
				phone: info[5]
			}
		},
		methods: {
			onSave(){
				this.$store.dispatch('updateUser', {
					first_name: this.info[1],
					last_name: this.info[2],
					email: this.info[0],
					username: this.info[3],
					phone: this.info[5]
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