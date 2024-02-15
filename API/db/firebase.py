from firebase_admin import credentials, initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate('Path to your secret key file')
initialize_app(cred, {
    'storageBucket': 'gs://openpose-db.appspot.com'
})