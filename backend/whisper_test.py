import os
import whisper

# Get absolute path to test.mp3 relative to this script's location
base_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(base_dir, "..", "test.mp3")

# Sanity check
if not os.path.exists(audio_path):
    print("ERROR: Audio file not found at:", audio_path)
    exit(1)

# Load Whisper model
model = whisper.load_model("base")

# Transcribe the audio
result = model.transcribe(audio_path)
transcribed_text = result["text"]

# Save output
output_path = os.path.join(base_dir, "output.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(transcribed_text)

print("Transcription complete. Saved to:", output_path)
print("Transcript preview:", transcribed_text[:100])
