from flask import Flask, jsonify, send_file
from flask_cors import CORS
from db.firebase import initialize_firebase
from firebase_admin import storage
import io

# Import Firebase initialization
initialize_firebase()

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


# Endpoint to serve JPEG image files
@app.route('/images/<filename>')
def serve_jpeg_image(image_path):
    blob = bucket.blob(image_path)
    file_data = blob.download_as_string()

    return send_file(
        io.BytesIO(file_data),
        mimetype='image/jpeg',
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(app='app', debug=True, port=5000)