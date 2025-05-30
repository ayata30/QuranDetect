import whisper

#load the model - good for testing
model = whisper.load_model("base")
result = model.transcribe("test.mp3")
transcribed_text = result["text"]

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(transcribed_text)

print("Transcription complete. Saved to output.txt")
print("Transcript preview:", transcribed_text[:100])

