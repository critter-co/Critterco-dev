<template>
  <div>
    <form @submit.prevent="activate">
      <section  class="verification-section">
        <div class="verification">
          <div class="verification__logo-box">
            <img src="@/assets/img/logo-large.png" alt="Critter Logo" class="verification__logo" />
          </div>
          <h1 class="heading--primary verification__heading">لطفا ایمیل خود را تایید کنید</h1>
          <p
            class="verification__text"
          >متنی حاوی کد فعالسازی برای شما ارسال شد لطفا کد را در پایین یادداشت کنید و دکمه ارسال را بزنید. تشکر</p>
          
          <input v-model="code" type="text" class="verification__input" />
          <button type="submit" class="btn btn--blue verification__btn">ارسال</button>
        </div>

        <footer class="sign-footer">
          <ul class="sign-footer__ul">
            <li class="sign-footer__li">
              <a href class="sign-footer__link">درباره ما</a>
            </li>
            <li class="sign-footer__li">
              <a href class="sign-footer__link">بیشتر بدانید</a>
            </li>
            <li class="sign-footer__li">
              <a href class="sign-footer__link">برای صاحبان کار</a>
            </li>
            <li class="sign-footer__li">
              <a href class="sign-footer__link">زبان</a>
            </li>
          </ul>
        </footer>

        <div class="social">
          <svg class="social__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-google" />
          </svg>
          <svg class="social__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-instagram" />
          </svg>
          <svg class="social__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-twitter" />
          </svg>
          <svg class="social__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-linkedin" />
          </svg>
        </div>
      </section>
    </form>
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
      this.$store.dispatch('register/activate',{
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