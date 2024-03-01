from firebase_admin import credentials, initialize_app, storage

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/michaelnweke/PhpstormProjects/CS5588-Capstone-Project/API/db/openpose-db-firebase-adminsdk-pl8gq-05904164a8.json')
# initialize_app(cred, {
#     'storageBucket': 'openpose-db.appspot.com'
# })
initialize_app(cred)

# Get reference to the default Cloud Storage bucket
bucket_name = 'openpose-db.appspot.com'
bucket = storage.bucket(bucket_name)
