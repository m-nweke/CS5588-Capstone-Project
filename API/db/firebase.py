from firebase_admin import credentials, initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to//Users/michaelnweke/PhpstormProjects/CS5588-Capstone-Project/API/db/openpose-db-firebase-adminsdk-pl8gq-05904164a8.json')
initialize_app(cred, {
    'storageBucket': 'gs://openpose-db.appspot.com'
})