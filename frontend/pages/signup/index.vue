<template>
  <div>
    <section class="section-sign">
      <form class="form" @submit.prevent="onSubmit">
        <h2 class="heading-secondary form__heading">به ما بپیوندید</h2>

        <AppControlInput
          v-model="last_name"
          type="text"
          placeholder="نام خانوادگی"
          inputClass="form__input"
          required
        >نام خانوادگی</AppControlInput>

        <AppControlInput
          v-model="first_name"
          type="text"
          placeholder="نام"
          inputClass="form__input"
          required
        >نام</AppControlInput>

        <AppControlInput
          v-model="email"
          type="email"
          placeholder="ایمیل "
          inputClass="form__input"
          groupClass="form__group"
          required
        >ایمیل</AppControlInput>

        <AppControlInput
          v-model="password"
          type="password"
          placeholder="کلمه عبور "
          inputClass="form__input"
          groupClass="form__group"
          required
        >کلمه عبور</AppControlInput>

        <AppControlInput
          v-model="confirmPassword"
          type="password"
          placeholder="تایید کلمه عبور  "
          inputClass="form__input"
          groupClass="form__group"
          required
        >تایید کلمه عبور</AppControlInput>

        <AppControlInput
          v-model="username"
          type="text"
          placeholder="شناسه کاربری"
          inputClass="form__input"
          groupClass="form__group"
          required
        >شناسه کاربری</AppControlInput>

        <AppControlInput
          v-model="phone"
          type="tel"
          pattern="[0]{1}[9]{1}[0-9]{9}"
          placeholder="شماره موبایل "
          inputClass="form__input"
          groupClass="form__group"
          required
        >شماره موبایل</AppControlInput>

        <button class="btn btn--blue form__btn">ثبت نام &rarr;</button>
      </form>

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
      confirmPassword: '',
      username: '',
      phone: '',
    }
  },

  methods: {
    onSubmit() {
      this.$store.dispatch('register/signingup', {
          first_name: this.first_name,
          last_name: this.last_name,
          email: this.email,
          password: this.password,
          username: this.username,
          phone: this.phone,
        })
        .then(() => {
          this.$router.push('/activate')
        })
    },
    access(){
            this.$store.dispatch('register/accessToken', {
                email: this.email,
                password: this.password
            }).then(()=>{
                this.$router.push('/comments')
            })
        }
  },
}
</script>

<style>
</style>