# flask backend

from flask import Flask, render_template, request, redirect, url_for
import os
from whisper_test import transcribe_audio

from match_surah import find_surah_match

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return 'No file part'
    file = request.files['audio']
    if file.filename == '':
        return 'No selected file'
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    transcription = transcribe_audio(filepath)
    matched_surah = find_surah_match(transcription)
    return render_template('index.html', transcription=transcription, surah=matched_surah)

if __name__ == '__main__':
    app.run(debug=True)
