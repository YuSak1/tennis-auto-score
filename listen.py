import speech_recognition as sr


def listen_to_voice():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice)
            # voice_text = listener.recognize_google(voice, language="ja-JP")
            # print(voice_text)
            return voice_text
    except:
        return "error"
