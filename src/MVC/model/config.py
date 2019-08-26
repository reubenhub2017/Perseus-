import os
import sys
import pyrebase
""" Config file for Firebase """
#This is is for data entry within file management system """
config = {
    "apiKey": "AIzaSyB9XhuZEVEVRkZGT9tiTPRCewNNsdZHCFU",
    "authDomain": "perseus-1f484.firebaseapp.com",
    "databaseURL": "https://perseus-1f484.firebaseio.com",
    "projectId": "perseus-1f484",
    "storageBucket": "",
    "messagingSenderId": "556348833840",
    "serviceAccount": "/Users/owner/Desktop/perseus-1f484-firebase-adminsdk-q6i1x-8f3c2b15e8.json"

}
firebase = pyrebase.initialize_app(config)


# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("reubenukah2017@gmail.com", "!Drogba96")

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])
