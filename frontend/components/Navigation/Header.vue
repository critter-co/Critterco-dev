<template>
  <div class="header-container">
    <header class="the-header">
      <!-- <TheSideNavToggle @toggle="$emit('sidenavToggle')" /> -->
      <div class="logo">
        <nuxt-link to="/">Critter</nuxt-link>
      </div>
      <div class="spacer"></div>
      <div v-if="isAuthenticated" class="navigation-items">
        <ul class="nav-list">
          <li class="nav-item">
            <nuxt-link to="/comments">Comment</nuxt-link>
          </li>
          <li class="nav-item">
            <nuxt-link to="/biz">Bizs</nuxt-link>
          </li>
          <li class="nav-item">
            <a @click="logout">Logout</a>
          </li>
          <!-- <li class="nav-item">
            <nuxt-link to="/admin">Admin</nuxt-link>
          </li> -->
        </ul>
      </div>
      <div v-else class="navigation-items">
          <li class="nav-item">
            <nuxt-link to="/signup">Signup/Login</nuxt-link>
          </li>
      </div>
    </header>
  </div>
</template>

<script>
// import TheSideNavToggle from "@/components/Navigation/TheSideNavToggle";
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Header",
  computed: mapGetters(["isAuthenticated"]),
  methods:{
      logout(){
          this.$store.dispatch("logout").then(this.$router.push("/"))
      }
  }
};
</script>


<style scoped>
.header-container {
  height: 60px;
}

.the-header {
  width: 100%;
  position: fixed;
  height: 60px;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: black;
  z-index: 100;
  box-sizing: border-box;
  padding: 0 20px;
}

.logo {
  margin: 0 10px;
  font-size: 1.3rem;
}

.logo a {
  text-decoration: none;
  color: white;
}

.spacer {
  flex: 1;
}

.navigation-items {
  display: none;
}

@media (min-width: 768px) {
  .navigation-items {
    display: block;
  }
}

.nav-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
}

.nav-item {
  margin: 0 10px;
}

.nav-item a {
  text-decoration: none;
  color: white;
}

.nav-item a:hover,
.nav-item a:active,
.nav-item a.nuxt-link-active {
  color: red;
}
</style>
