from flask import Flask, jsonify
from flask_cors import CORS
from firebase_admin import storage

#Initialize storage buck for firebase
bucket = storage.bucket()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/', methods=['GET'])
def home():
    return jsonify('Hello World')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Upload file to Firebase Storage
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    return 'File uploaded successfully'


@app.route('/media/<filename>', methods=['GET'])
def get_file(filename):
    # Retrieve file path from Firebase Storage or any other storage system
    # Here, 'get_file_url' is a function that retrieves the URL based on the filename
    file_url = get_file_url(filename)
    if file_url:
        # Redirect to the Firebase Storage URL
        return redirect(file_url)
    else:
        return 'File not found'

if __name__ == '__main__':
    app.run(app='app', debug=True, port=5000)