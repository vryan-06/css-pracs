import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDlR__dYoX_ks_5D1roCgplJJjkaINVW3Y",
  authDomain: "anotherproject-d4105.firebaseapp.com",
  projectId: "anotherproject-d4105",
  storageBucket: "anotherproject-d4105.appspot.com",
  messagingSenderId: "512593875387",
  appId: "1:512593875387:web:1a6b8c8ee4fe958481749e",
  measurementId: "G-6FX69Y7PQS"
};

export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const auth = getAuth(app);