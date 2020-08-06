<template>
  <header class="header">
    <div v-if="isAuthenticated" class="header-nav">
      <div class="header-nav__avatar-box">
        <img class="header-nav__avatar" alt="Profile picture" />
      </div>
      <input type="checkbox" class="header-nav__checkbox" id="navi-toggle" />
      <label for="navi-toggle" class="header-nav__name">
        <span class="header-nav__icon">{{ userData[1] }}&darr;</span>
      </label>

      <div class="header-nav__toggle">
        <ul class="header-nav__ul">
          <li class="header-nav__li">
            <nuxt-link class="header-nav__link" to="/comments"
              >کامنت ها</nuxt-link
            >
          </li>
          <li class="header-nav__li">
            <nuxt-link class="header-nav__link" to="/biz">بیزینس</nuxt-link>
          </li>
          <li class="header-nav__li">
            <nuxt-link class="header-nav__link" to="/me">پروفایل من</nuxt-link>
          </li>
          <li class="header-nav__li">
            <a class="header-nav__logout" @click="logout" href="/">خروج</a>
          </li>
        </ul>
      </div>
    </div>

    <a href="/">
      <img
        src="@/assets/img/logo-large.png"
        alt="Critter Logo"
        class="header__logo--large"
      />
    </a>
    <div class="header__box">
      <svg class="header__svg">
        <use xlink:href="@/assets/icons/sprite.svg#icon-search" />
      </svg>
      <input type="text" class="header__input" />
    </div>

    <ul class="header__nav">
      <li class="header__li">
        <a href="#" class="header__link">رستوران</a>
      </li>
      <li class="header__li">
        <a href="#" class="header__link">کافه</a>
      </li>
      <li class="header__li">
        <a href="#" class="header__link">خدمات</a>
      </li>
      <li class="header__li">
        <a href="#" class="header__link">بیشتر</a>
      </li>
    </ul>
  </header>
</template>
<script>
// import TheSideNavToggle from "@/components/Navigation/TheSideNavToggle";
import { mapGetters } from 'vuex'
import axios from 'axios'
import Cookie from 'js-cookie'
export default {
  name: 'Header',
  computed: {
    ...mapGetters({
      isAuthenticated: 'register/isAuthenticated',
      userData: 'user/userData',
    }),
  },
  methods: {
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$store.dispatch('register/logout').then(this.$router.push('/'))
    },
  },
}
</script>

<style>
.spacer {
  flex: 2;
  left: 0;
}
</style>
