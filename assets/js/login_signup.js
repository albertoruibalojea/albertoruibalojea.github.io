import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getAuth, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";
import { getFirestore, doc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js";

// Configuración de Firebase
const firebaseConfig = {
  apiKey: "AIzaSyB-8935XhLufIx8E-xqKoRzC5b4KUh4DAQ",
  authDomain: "cron-d3463.firebaseapp.com",
  projectId: "cron-d3463",
  storageBucket: "cron-d3463.firebasestorage.app",
  messagingSenderId: "303808058544",
  appId: "1:303808058544:web:a1f1f868d8fa823f695775",
  measurementId: "G-R14FTBJWH3"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// Elementos del DOM
const emailInput = document.getElementById('email');
const passInput = document.getElementById('password');
const loginBtn = document.getElementById('login-btn');
const msgDiv = document.getElementById('msg');

// Función login
loginBtn.addEventListener('click', async () => {
  const email = emailInput.value;
  const pass = passInput.value;

  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, pass);
    const user = userCredential.user;

    // Verificar si el documento del usuario existe
    const userRef = doc(db, "users", user.uid);
    const userDoc = await getDoc(userRef);

    if (!userDoc.exists()) {
      await setDoc(userRef, {
        email: user.email,
        premium: false
      });
    }

    window.location.href = "premium.html";
  } catch (err) {
    msgDiv.innerText = err.message;
  }
});