import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# List of language codes
LANGUAGES = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian Creole': 'ht',
    'Hausa': 'ha',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jv',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish (Kurmanji)': 'ku',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Zulu': 'zu'
}

def display_languages():
    print("Available languages:")
    for language, code in LANGUAGES.items():
        print(f"{language}: {code}")

def recognize_speech(src_lang):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio, language=src_lang)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return None

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    print(f"Translated to {dest_lang}: {translated.text}")
    return translated.text

def speak_text(text, lang):
    tts = gTTS(text=text, lang=lang)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    # Play the generated speech using pygame
    pygame.mixer.music.load(audio_stream, 'mp3')
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

def main():
    display_languages()

    # Ask the user for source and destination languages
    src_lang = input("Enter source language code (e.g., 'en' for English): ").strip()
    dest_lang = input("Enter destination language code (e.g., 'es' for Spanish): ").strip()

    if src_lang not in LANGUAGES.values() or dest_lang not in LANGUAGES.values():
        print("Invalid language code. Please refer to the list of available languages.")
        return

    print("Speak in your source language...")
    text = recognize_speech(src_lang)
    if text:
        translated_text = translate_text(text, src_lang, dest_lang)
        speak_text(translated_text, dest_lang)

if __name__ == "__main__":
    main()
