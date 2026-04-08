// Import Firebase SDK in your HTML before this file
// <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js"></script>
// <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js"></script>

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

// Example: Save order
document.getElementById("checkout-form")?.addEventListener("submit", e => {
  e.preventDefault();
  db.collection("orders").add({
    name: e.target[0].value,
    address: e.target[1].value,
    payment: e.target[2].value,
    cart: JSON.parse(localStorage.getItem("cart"))
  }).then(() => alert("Order placed successfully!"));
});
// firebase.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.11.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.11.0/firebase-analytics.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/12.11.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyADodoysinulcBMWMH2LsXsVWsok7yjcaI",
  authDomain: "muhammad-tayyab-67606.firebaseapp.com",
  projectId: "muhammad-tayyab-67606",
  storageBucket: "muhammad-tayyab-67606.firebasestorage.app",
  messagingSenderId: "365718499684",
  appId: "1:365718499684:web:92dd940abd0c67b71e8a71",
  measurementId: "G-8DHFDCQ5YC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const db = getFirestore(app);
