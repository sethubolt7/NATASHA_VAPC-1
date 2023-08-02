import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate(r"natasha-bd631-firebase-adminsdk-htd4a-b09ad6e75d.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://natasha-bd631-default-rtdb.firebaseio.com/'
})
ref = db.reference('data')
ref.set('true')
