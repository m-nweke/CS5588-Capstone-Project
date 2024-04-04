<template>
  <div class="container">
    <h1>Log into your PostureProfile</h1>
    <div class="form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" placeholder="Enter your email" v-model="email" />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" placeholder="Enter your password" v-model="password" />
      </div>
      <p class="error" v-if="errMsg">{{ errMsg }}</p>
      <button style="background-color: orange; color: #ffffff" @click="login">Log in</button>
    </div>
    <p class="separator">or</p>
    <button class="btn-google" @click="signInWithGoogle">Sign in with Google</button>
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

.error {
  color: #db4437;
}

.separator {
  text-align: center;
  margin: 20px 0;
}
</style>

<script setup lang="ts">
import { ref } from 'vue';
import { signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from 'firebase/auth';
import { useRouter } from 'vue-router';
import { auth } from '@/main';

const email = ref('');
const password = ref('');
const errMsg = ref('');
const router = useRouter();

const login = () => {
  signInWithEmailAndPassword(auth, email.value, password.value)
      .then(() => {
        console.log("Successfully signed in!")
        router.push('/dashboard');
        errMsg.value = '';
      })
      .catch(error => {
        errMsg.value = '';
        console.error(error.code);
        switch (error.code) {
          case "auth/invalid-email":
            errMsg.value = "Invalid email";
            break;
          case "auth/user-not-found":
            errMsg.value = "No account with that email was found";
            break;
          case "auth/wrong-password":
            errMsg.value = "Incorrect password";
            break;
          default:
            errMsg.value = "Email or password incorrect";
            break;
        }
      });
};

const signInWithGoogle = () => {
  const provider = new GoogleAuthProvider();
  signInWithPopup(auth, provider).then((result) => {
    console.log(result.user);
    router.push('/dashboard')
  })
};
</script>