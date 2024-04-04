<template>
  <div class="container">
    <h1>Create a Posture Profile</h1>
    <div class="form">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" placeholder="Enter your name" v-model="name" />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" placeholder="Enter your email" v-model="email" />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" placeholder="Enter your password" v-model="password" />
      </div>
      <button style="background-color: orange; color: #ffffff" @click="register">Submit</button>
    </div>
    <p class="separator">or</p>
    <button class="btn-google" @click="signInWithGoogle">Sign in with Google</button>
    <p class="sign-in-here">Already have an account? <router-link to="/login">Sign in here</router-link>.</p>
  </div>
</template>

<style scoped>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: var(--color-background); /* Set background color same as the rest of the page */
}

h1 {
  text-align: center;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-google {
  background-color: #db4437;
  color: #fff;
}

.separator {
  text-align: center;
  margin: 20px 0;
}

.sign-in-here {
  text-align: center;
  margin-top: 20px;
}

.sign-in-here a {
  color: orange; /* Set the color of the text within the router-link to orange */
  text-decoration: underline; /* Add underline to the text within the router-link */
}

</style>

<script setup lang="ts">
import { ref } from 'vue';
import { createUserWithEmailAndPassword, updateProfile } from 'firebase/auth';
import { useRouter } from 'vue-router';
import { auth } from '@/main';

const name = ref('');
const email = ref('');
const password = ref('');
const router = useRouter();

const register = () => {
  createUserWithEmailAndPassword(auth, email.value, password.value)
      .then(() => {
        const user = auth.currentUser;
        if (user) {
          updateProfile(user, {displayName: name.value})
              .then(() => {
                console.log("Successfully Registered!");
                router.push('/dashboard');
              })
              .catch((error) => {
                console.error(error);
                alert(error.message);
              })
        }
        router.push('/dashboard');
      })
      .catch(error => {
        console.error(error);
        alert(error.message);
      });
};

const signInWithGoogle = () => {
  // Implement sign in with Google
};
</script>
