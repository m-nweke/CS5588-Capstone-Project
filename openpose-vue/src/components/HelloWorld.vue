<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      You’ve successfully created a project with
      <a href="https://vitejs.dev/" target="_blank" rel="noopener">Vite</a> +
      <a href="https://vuejs.org/" target="_blank" rel="noopener">Vue 3</a>. What's next?
    </h3>
    <p>{{ testData }}</p>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>

<script setup lang="ts">
/* eslint-disable */
defineProps<{
  msg: string
}>()

import axios from 'axios';
import { ref, onBeforeMount } from 'vue';

const testData = ref('');

const getData = () => {
  return axios.get('http://127.0.0.1:5000/'); // Return the axios promise
};

onBeforeMount(async() => {
  try {
    const response = await getData();
    console.log(response.data);
    testData.value = response.data; // Return the data
  } catch (error) {
    console.error('Error getting data: ', error);
    return null; // Return null in case of error
  }
})

</script>
