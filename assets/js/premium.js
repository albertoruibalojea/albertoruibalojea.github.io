import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getAuth, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";
import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-firestore.js";

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

onAuthStateChanged(auth, async (user) => {
  if (user) {
    const userRef = doc(db, "users", user.uid);
    const userDoc = await getDoc(userRef);

    if (!userDoc.exists()) {
      await setDoc(userRef, {
        premium: false,
        email: user.email
      });
    }

    const isPremium = userDoc.data()?.premium === true;

    if (isPremium) {
      document.getElementById("premium-content").style.display = "block";
    } else {
      document.getElementById("free-teaser").style.display = "block";
    }

    document.getElementById("logout-btn").style.display = "block";
  } else {
    window.location.href = "login_signup.html";
  }
});