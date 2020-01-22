const admin = require("firebase-admin");
const csv = require("csv-writer").createObjectCsvWriter;
const certificate = require("./innova");

admin.initializeApp({
    credential : admin.credential.cert(certificate)
});

csvWriter = csv({
    path : "./firebase-db.csv",
    header : [
        {id : "name", title : "Name"},
        {id : "email", title : "email"},
        {id : "org", title : "Org"},
        {id : "prof", title : "Profession"},
        {id : "phone", title : "Phone no."},
        {id : "pref", title : "Preference"},
        {id : "food", title : "Food"},
        {id : "tshirt", title : "T-shirt"},
    ]
});

const db = admin.firestore();

var records = []; // hold all documents

db.collection("innova1").get().then(function(snap) {
    snap.forEach(function(doc) {
        if (doc.exists) records.push(doc.data());
        else console.log("No document found");
    });
    csvWriter.writeRecords(records).then(function() {
        console.log("Done...");
    });
}).catch(function(err) {
    console.log(err);
});