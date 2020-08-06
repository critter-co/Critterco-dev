<template>
  <div class="profile-page">
    <section class="mountain"></section>

    <div class="profile">
      <img alt class="profile__img" />
      <div class="profile__exit">خروج از حساب</div>
      <span class="profile__name">{{ information.firstname }}</span>
      <span class="profile__find">دوست پیدا کن &plus;</span>
      <span class="profile__address">البرز - کرج</span>
      <div class="profile__stats">
        <div class="profile__info">
          <svg class="profile__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-search" />
          </svg>
          <span class="profile__text">دوستان</span>
          <span class="profile__text--friends">15</span>
        </div>

        <div class="profile__info">
          <svg class="profile__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-search" />
          </svg>
          <span class="profile__text">نظرات</span>
          <span class="profile__text--comments">54</span>
        </div>

        <div class="profile__info">
          <svg class="profile__svg">
            <use xlink:href="@/assets/icons/sprite.svg#icon-search" />
          </svg>
          <span class="profile__text">عکس ها</span>
          <span class="profile__text--pictures">5</span>
        </div>
      </div>

      <div class="about">
        <span class="about__name">درباره من</span>
        <div class="about__title">مکان</div>
        <span class="about__location">البرز - کرج</span>
        <div class="about__title">عضو کریتر از:</div>
        <span class="about__date">فروردین 1400</span>
        <div class="about__title">چیزهایی که دوست دارم!!!!</div>
        <span class="about__favorite">تریستانا</span>
      </div>
    </div>

    <div class="right">
      <ul class="right__nav">
        <li class="right__li">
          <a href class="right__link">پروفایل</a>
        </li>
        <li class="right__li">
          <a href class="right__link">دوستان</a>
        </li>
        <li class="right__li">
          <a href class="right__link">نظرات</a>
        </li>
        <li class="right__li">
          <a href class="right__link">تعریف ها</a>
        </li>
        <li class="right__li">
          <a href class="right__link">نکات</a>
        </li>
        <li class="right__li">
          <a href class="right__link">مناسبت ها</a>
        </li>
        <li class="right__li">
          <a href class="right__link">دنبال کننده ها</a>
        </li>
        <li class="right__li">
          <a href class="right__link">دنبال شونده ها</a>
        </li>
      </ul>

      <div class="right__news">
        <span>اطلاعیه ها</span>
      </div>

      <div class="right__activities">
        <span>فعالیت های اخیر</span>
      </div>
      <img
        src="@/assets/img/juice.jpg"
        alt
        class="right__image right__image--1"
      />
      <img
        src="@/assets/img/icecream2.jpg"
        alt
        class="right__image right__image--2"
      />
    </div>

    <footer class="footer">
      <div class="footer__box"></div>
      <ul class="footer-nav">
        <li class="footer-nav__li">
          <a href class="footer-nav__link">درباره ما</a>
        </li>
        <li class="footer-nav__li">
          <a href class="footer-nav__link">کریتر برای صاحبان کار</a>
        </li>
        <li class="footer-nav__li">
          <a href class="footer-nav__link">بیشتر بدانید</a>
        </li>
        <li class="footer-nav__li">
          <a href class="footer-nav__link">زبان</a>
        </li>
      </ul>

      <img src alt="Footer image" class="footer__img" />
    </footer>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import User from '@/components/User/User'
export default {
  name: 'UserProfile',
  middleware: ['auth'],
  computed: {
    information: {
      get() {
        var info = []
        info = this.$store.state.user.user
        return {
          email: info[0],
          firstname: info[1],
          lastname: info[2],
          username: info[3],
          phone: info[5],
        }
      },
      set(value) {
        info.push(value)
      },
    },
  },
  methods: {
    onSave() {
      this.$store
        .dispatch('user/updateUser', {
          first_name: this.information.firstname,
          last_name: this.information.lastname,
          email: this.information.email,
          username: this.information.username,
          phone: this.information.phone,
        })
        .then(() => {
          this.$router.push('/')
        })
    },
    onCancel() {
      // NAvigate Back
      this.$router.push('/')
    },
  },
}
</script>
