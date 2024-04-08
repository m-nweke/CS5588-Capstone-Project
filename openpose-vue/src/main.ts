import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import { initializeApp } from 'firebase/app'
import { getFirestore } from "firebase/firestore";
import 'firebase/auth';
import { getAuth } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyAiBggE1bmfuZUGmSWoxwrtJ8lKBExdCFU",
    authDomain: "openpose-db.firebaseapp.com",
    projectId: "openpose-db",
    storageBucket: "openpose-db.appspot.com",
    messagingSenderId: "271005034064",
    appId: "1:271005034064:web:ccd3e84835151e502b1355",
    measurementId: "G-DTH1R02B5M"
};

// Initialize Firebase app
const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth(firebaseApp);
const db = getFirestore(firebaseApp)

// const analytics = getAnalytics(firebaseApp);


// Create Vue app
const vueApp = createApp(App);

// Use router
vueApp.use(router);

// Mount Vue app
vueApp.mount('#app');

export { auth, db }