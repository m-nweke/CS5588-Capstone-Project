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
      <div v-if="workoutResult.length > 0">
        <h3>Posture Improvement Recommendations:</h3>
        <ul>
          <li v-for="recommendation in workoutResult" :key="recommendation">{{ recommendation }}</li>
        </ul>
      </div>
    </div>
    <div v-if="showLoading" class="loading-spinner"></div>
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
const showLoading = ref(false); // This will be set to true when loading
const postureDetectionResult = computed(() => {
  // This would be fetched from the backend after submission,
  // but for now, we'll hard code it
  return "Our posture detection model detected you sitting with a hunched back, with hands folded and right leg kneeling. This is pretty good posture, but we have some recommendations for improvement!";
});

const workoutResult = computed(() => {
  return [
    "To fix the hunched back, openPosture recommends 3x1min child's pose with 90 seconds rest, 3 times a day.",
    "For the kneeling, we recommend 3x20 each leg hamstring curls twice a day (use ankle weights if available)"
  ];
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
  showLoading.value = true;
  setTimeout(() => {
    showLoading.value = false;
    showResults.value = true;
  }, 5000); // Show loading spinner for 5 seconds
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

.loading-spinner {
  border: 5px solid #f3f3f3; /* Light grey */
  border-top: 5px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 2s linear infinite;
  margin: 20px auto;
}

.uploaded-image {
  width: 100%; /* Set image width to 100% of the container */
  height: auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
