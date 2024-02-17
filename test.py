import speech_recognition as sr

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source, timeout=5, phrase_time_limit=3)
        print("Recognizing...")
        voice_text = listener.recognize_google(voice)
        # voice_text = listener.recognize_google(voice, language="ja-JP")
        # voice_text = listener.recognize_whisper_api(voice)

        print(voice_text)
except:
    print('Sorry, I could not listen')