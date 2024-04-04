<template>
  <div class="container">
    <h1>Hello, {{ name }}</h1>
    <div class="card">
      <p class="instructions">Input an image of you sitting for posture evaluation. This image must be taken from a side angle.</p>
      <input type="file" accept="image/*" @change="handleFileUpload">
      <button class="submit-button" @click="submitImage">Submit</button>
      <button class="clear-button" @click="clearImage">Clear</button>
    </div>
    <div class="results" v-if="showResults">
      <h2>Here are your results:</h2>
      <img :src="imageUrl" v-if="imageUrl && showResults" alt="Uploaded Image" class="uploaded-image">
      <p>{{ postureDetectionResult }}</p>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref, computed } from 'vue';
import { auth, db } from '@/main';
import { collection, addDoc } from 'firebase/firestore';

const name = ref(auth.currentUser?.displayName);
const imageFile = ref<File | null>(null);
const imageUrl = ref<string | null>(null);
const showResults = ref(false); // This will be set to true when results are available
const postureDetectionResult = computed(() => {
  // This would be fetched from the backend after submission,
  // but for now, we'll hard code it
  return "Our posture detection model detected you sitting with a hunched back, with hands folded and non-kneeling. This is pretty good posture, but we have some recommendations for improvement!";
});

const handleFileUpload = (event: Event) => {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (file) {
    imageFile.value = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      if (e.target) {
        imageUrl.value = e.target.result as string;
      }
    };
    reader.readAsDataURL(file);
  }
};

const submitImage = () => {
  // Logic for submitting the image goes here
  console.log('Submit button clicked');
  showResults.value = true;
};

const clearImage = () => {
  // Clear the uploaded image and hide the results
  imageFile.value = null;
  imageUrl.value = null;
  showResults.value = false;
};

</script>


<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.card {
  background-color: orange;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.instructions {
  margin-bottom: 20px;
  color: black;
}

input[type="file"] {
  margin-bottom: 20px;
}

.submit-button, .clear-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button {
  background-color: limegreen;
  color: white;
}

.submit-button:hover {
  background-color: darkgreen;
}

.clear-button {
  background-color: red;
  color: white;
}

.clear-button:hover {
  background-color: darkred;
}

.results {
  margin-top: 40px;
  text-align: left;
}

.results h2 {
  text-align: center;
}


.uploaded-image {
  max-width: 100%;
  height: auto;
}
</style>
