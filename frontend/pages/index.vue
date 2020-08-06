<template>
  <div>
    <section class="section-auth">
      <div class="row">
        <div class="reg">
          <nuxt-link to="/signup" class="btn btn--light u-margin-right-medium"
            >ثبت نام</nuxt-link
          >
          <nuxt-link to="/login" class="btn btn--light">ورود</nuxt-link>
        </div>
        <div class="reg__signup"></div>
        <div class="reg__signin"></div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style scoped>
h1 {
  text-align: center;
}
</style>
