import os 
from dotenv import load_dotenv 
from google import genai
from google.genai import types
load_dotenv()

from gtts import gTTS
import io

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)




def note_summarizer(images):
    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images, "Summarize the picture in note format in max 100 words"]
    )

    return response.text


def quiz_generator(images, difficulty):
    prompt = f"Create a {difficulty} level quiz with 3 multiple-choice questions based on this image. Provide the correct answers at the very end."
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=[images, prompt]
    )
    return response.text




def generate_audio_summary(text):

    tts = gTTS(text=text,lang="en",slow=False)
    audio_buffer = io.BytesIO()

    tts.write_to_fp(audio_buffer)

    return audio_buffer



