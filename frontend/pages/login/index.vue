<template>
    <div>
        <h1>Login Page!</h1>
        <div class="admin-auth-page">
            <div class="auth-container">
                <form @submit.prevent="access">
                    <AppControlInput v-model="email" type="email" placeholder="Email" />
                    <AppControlInput v-model="password" type="password" placeholder="Password" />
                    <AppButton type="submit">Login</AppButton>
                </form>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'LoginPage',
    data(){
        return {
            email: '',
            password: ''
        }
    },
    methods:{
    async access(){
            this.$store.dispatch('accessToken', {
                email: this.email,
                password: this.password
            }),
            await this.$store.dispatch('gettingInfo', {
                email: this.email
            }).then(()=>{
                this.$router.push('/comments')
            })
        }
    }
}
</script>

<style scoped>
h1 {
  text-align: center;
  text-decoration: bold;
  padding: 0px 0px 20px 0px;
}
.admin-auth-page {
  padding: 20px;
}

.auth-container {
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 2px #ccc;
  width: 300px;
  margin: auto;
  padding: 10px;
  box-sizing: border-box;
}
</style>