// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBjr05sY7INFySxDkYw8wRCoF0_RIo-1jI",
  authDomain: "hobbies-83557.firebaseapp.com",
  projectId: "hobbies-83557",
  storageBucket: "hobbies-83557.appspot.com",
  messagingSenderId: "1060586600513",
  appId: "1:1060586600513:web:ce1fe2f021600b6828aec0",
  measurementId: "G-1STB6K6ZCY"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);


