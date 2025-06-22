from gtts import gTTS
import os

def generate_audio(summary_text,filename="audio/summary.mp3"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tts = gTTS(summary_text)
    tts.save(filename)
    print(f"Audio saved to {filename}")