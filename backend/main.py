from fastapi import FastAPI, File, UploadFile
import whisper


app = FastAPI()
model = whisper.load_model("medium")  # load Whisper once on startup

@app.get("/")
def read_root():
    return {"message": "QuranDetect API is running"}


@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    contents = await file.read()
    temp_file_path = "temp_audio.mp3"
    with open(temp_file_path, "wb") as f:
        f.write(contents)
    
    # Run whisper transcription
    result = model.transcribe(temp_file_path)
    text = result["text"]
    
    # Optionally, delete temp_file_path if you want
    
    return {"transcription": text}
