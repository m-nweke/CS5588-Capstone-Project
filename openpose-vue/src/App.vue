<template>
  <header>
    <img alt="OpenPose logo" class="logo" src="@/assets/openPose.png" width="200" height="200" />

    <div class="wrapper">
      <HelloWorld class="title" msg="OpenPosture" />

      <nav>
        <router-link class="nav-link" to="/">Home</router-link>
        <router-link class="nav-link" to="/dashboard">Dashboard</router-link>
        <router-link class="nav-link" to="/register">Register</router-link>
        <router-link class="nav-link" to="/login">Login</router-link>
        <button class="btn-signout" @click="handleSignOut" v-if="isLoggedIn">Sign out</button>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { onMounted, ref } from 'vue';
import { onAuthStateChanged, signOut } from "firebase/auth";
import { useRouter } from "vue-router";
import { auth } from '@/main';

const router = useRouter();
const isLoggedIn = ref(false);
onMounted(() => {
  onAuthStateChanged(auth, (user) => {
    isLoggedIn.value = !!user;
  })
})
const handleSignOut = () => {
  signOut(auth).then(() => {
    router.push('/')
  })
};
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.wrapper {
  color: orange;
}

.nav-link {
  color: orange;
}

.title {
  color: orange;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

.btn-signout {
  background-color: #db4437;
  color: #fff;
  padding: 8px 12px;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-signout:hover {
  background-color: #c4322e;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
