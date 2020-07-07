<template>
  <div>
    <div class="admin-auth-page">
      <h1>Activate Page</h1>
        <div class="auth-container">
          <form @submit.prevent="activate">
            <AppControlInput v-model="code" type="text" placeholder="Activation Code"/>
            <AppButton type="submit">Activate</AppButton>
          </form>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActivatePage',
  data() {
    return {
     code: ''
    }
  },
  methods: {
    activate() {
      this.$store.dispatch('activate',{
        code: this.code
      }).then(() => {
          this.$router.push('/login')
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