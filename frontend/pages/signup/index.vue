<template>
  <div class="admin-auth-page">
    <h1>Signup/Login to continue.</h1>
    <div v-if="isLogin" class="auth-container">
       <form @submit.prevent="access">
          <AppControlInput v-model="email" type="email" placeholder="Email" />
          <AppControlInput v-model="password" type="password" placeholder="Password" />
          <AppButton type="submit">{{ isLogin ? 'Login' : 'Signup' }}</AppButton>
          <AppButton
          type="button"
          btn-style="inverted"
          style="margin-left: 10px;"
          @click="isLogin = !isLogin"
          >Switch to {{ isLogin ? 'Signup' : 'Login' }}</AppButton>
        </form>
    </div>
    <div v-else class="auth-container">
      <form @submit.prevent="onSubmit">
        <AppControlInput
          v-model="first_name"
          type="text"
          placeholder="Firstname"
        />
        <AppControlInput
          v-model="last_name"
          type="text"
          placeholder="lastname"
        />
        <AppControlInput v-model="email" type="email" placeholder="Email" />
        <AppControlInput
          v-model="password"
          type="password"
          placeholder="Password"
        />
        <AppControlInput
          v-model="username"
          type="text"
          placeholder="Username"
        />
        <AppControlInput v-model="name" type="text" placeholder="Name" />
        <AppControlInput v-model="phone" type="text" placeholder="Phone" />
        <AppButton type="submit">{{ !isLogin ? 'Signup' : 'Login' }}</AppButton>
        <AppButton
          type="button"
          btn-style="inverted"
          style="margin-left: 10px;"
          @click="isLogin =! isLogin"
        >Switch to {{ isLogin ? 'Signup' : 'Login' }}</AppButton>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage',
  data() {
    return {
      isLogin: false,
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      username: '',
      name: '',
      phone: '',
    }
  },

  methods: {
    onSubmit() {
      this.$store
        .dispatch('signingup', {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password,
          username: this.username,
          name: this.name,
          phone: this.phone,
        })
        .then(() => {
          this.$router.push('/activate')
        })
    },
    access(){
            this.$store.dispatch('accessToken', {
                email: this.email,
                password: this.password
            }).then(()=>{
                this.$router.push('/comments')
            })
        }
  },
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
