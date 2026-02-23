import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Speech Recognition

class VoiceEngine:
    def __init__(self, voice_gender='female'):
        # Initialize the TTS engine
        self.tts_engine = pyttsx3.init()
        # Set properties before adding anything to speak
        voices = self.tts_engine.getProperty('voices')
        if voice_gender == 'female':
            self.tts_engine.setProperty('voice', voices[1].id)  # Female voice
        else:
            self.tts_engine.setProperty('voice', voices[0].id)  # Male voice

    def text_to_speech(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def recognize_speech(self):
        # Initialize the recognizer
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"