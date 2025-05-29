from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# uploads folder exists
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({
        'message': 'File uploaded!',
        'surah': 'Al-Fatiha',
        'ayah': 1
    })

if __name__ == '__main__':
    app.run(debug=True)
