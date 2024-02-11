import speech_recognition as sr


def listen_to_voice():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice)
            # voice_text = listener.recognize_google(voice, language="ja-JP")
            print(voice_text)
            return voice_text
    except:
        print('Sorry, I could not understand')
        return "error"


def recognize_score():
    voice_text = listen_to_voice()
    while True:
        if voice_text == "one":
            return 0
        elif voice_text == "two":
            return 1
        elif voice_text == "cancel":
            return -1
        else:
            voice_text = listen_to_voice()


