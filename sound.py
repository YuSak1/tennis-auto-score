import pyttsx3

engine = pyttsx3.init()
# engine.setProperty('rate', 150)


def say(text)->None:

    # Setting
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Play sound
    engine.say(text)
    engine.runAndWait()
