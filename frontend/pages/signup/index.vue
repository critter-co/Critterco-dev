<template>
  <div>
    <section class="section-sign">
      <div v-if="isLogin">
        <form class="form" @submit.prevent="access">
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
            <AppButton type="submit" class="btn btn--blue form__btn">ورود &rarr; {{ !isLogin ? 'Signup' : 'Login' }} </AppButton>
      
            <AppButton
            type="button"
            btn-style="inverted"
            style="margin-left: 10px;"
            @click="isLogin = !isLogin"
            >Switch to {{ isLogin ? 'Signup' : 'Login' }}</AppButton>
        </form>
      </div>
      <div v-else>
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

            <!-- <AppControlInput
            v-model="name"
            type="text"
            placeholder="نام و نام خانوادگی"
            inputClass="form__input"
            required
          >نام</AppControlInput> -->

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

          <AppButton type="submit" class="btn btn--blue form__btn">ثبت نام &rarr; {{ !isLogin ? 'Signup' : 'Login' }} </AppButton>
          <AppButton
            type="button"
            btn-style="inverted"
            style="margin-left: 10px;"
            @click="isLogin =! isLogin"
          >Switch to {{ isLogin ? 'Signup' : 'Login' }}</AppButton>
        </form>
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
      this.$store
        .dispatch('signingup', {
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
