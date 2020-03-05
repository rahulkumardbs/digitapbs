import firebase from 'firebase';
const config = {
    apiKey: "AIzaSyDFKwkBwwDvzy-Tx87VJaXxlkFo-fQnc6Y",
    authDomain: "digitapbs-8865a",
    databaseURL: "https://digitapbs-8865a.firebaseio.com",
    projectId: "digitapbs-8865a",
    storageBucket: "ENTER YOURS HERE",
    messagingSenderId: "ENTER YOURS HERE"
}
firebase.initializeApp(config);
export const databaseRef = firebase.database().ref();