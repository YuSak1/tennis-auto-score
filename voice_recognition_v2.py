import speech_recognition as sr


def listen_to_voice():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # print("Listening...")
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice)
            # voice_text = listener.recognize_google(voice, language="ja-JP")
            print(voice_text)
            return voice_text
    except:
        # print('Sorry, I could not understand')
        return "error"


def recognize_score(score):
    not_recognized = True
    voice_text = listen_to_voice()

    # Player 1 is serving
    while not_recognized:
        not_recognized = False
        if voice_text == "cancel":
            return -1
        # ------------------------------------------------------
        elif score.points == [0, 0] and voice_text == "15 love":
            score.points = [1, 0]
        elif score.points == [1, 0] and voice_text == "30 love":
            score.points = [2, 0]
        elif score.points == [2, 0] and voice_text == "40 love":
            score.points = [3, 0]
        elif score.points == [3, 0] and voice_text == "game":
            score.games[0] += 1
            score.new_game()
        # ------------------------------------------------------
        elif score.points == [0, 0] and voice_text == "love 15":
            score.points = [0, 1]
        elif score.points == [0, 1] and voice_text == "love 30":
            score.points = [0, 2]
        elif score.points == [0, 2] and voice_text == "love 40":
            score.points = [0, 3]
        elif score.points == [0, 3] and voice_text == "game":
            score.games[1] += 1
            score.new_game()
        # ------------------------------------------------------
        elif score.points == [0, 1] and voice_text == "1515":
            score.points = [1, 1]
        elif score.points == [1, 1] and voice_text == "3015":
            score.points = [2, 1]
        elif score.points == [2, 1] and voice_text == "4015":
            score.points = [3, 1]
        elif score.points == [3, 1] and voice_text == "game":
            score.games[0] += 1
            score.new_game()
        # ------------------------------------------------------
        elif score.points == [1, 0] and voice_text == "1515":
            score.points = [1, 1]
        elif score.points == [1, 1] and voice_text == "1530":
            score.points = [1, 2]
        elif score.points == [1, 2] and voice_text == "1540":
            score.points = [1, 3]
        elif score.points == [1, 3] and voice_text == "game":
            score.games[1] += 1
            score.new_game()
        # ------------------------------------------------------
        elif score.points == [0, 2] and voice_text == "1530":
            score.points = [1, 2]
        elif score.points == [1, 2] and voice_text == "3030":
            score.points = [2, 2]
        elif score.points == [2, 2] and voice_text == "4030":
            score.points = [3, 2]
        elif score.points == [3, 2] and voice_text == "game":
            score.games[0] += 1
            score.new_game()
        # ------------------------------------------------------
        elif score.points == [2, 0] and voice_text == "3015":
            score.points = [2, 1]
        elif score.points == [2, 1] and voice_text == "3030":
            score.points = [2, 2]
        elif score.points == [2, 2] and voice_text == "3040":
            score.points = [2, 3]
        elif score.points == [2, 3] and voice_text == "game":
            score.games[1] += 1
            score.new_game()
        # ------------------------------------------------------
        elif score.points == [0, 3] and voice_text == "1540":
            score.points = [1, 3]
        elif score.points == [1, 3] and voice_text == "3040":
            score.points = [2, 3]
        elif score.points == [2, 3] and voice_text == "deuce":
            score.points = [3, 3]
        # ------------------------------------------------------
        elif score.points == [3, 0] and voice_text == "4015":
            score.points = [3, 1]
        elif score.points == [3, 1] and voice_text == "4030":
            score.points = [3, 2]
        elif score.points == [3, 2] and voice_text == "deuce":
            score.points = [3, 3]
        # ------------------------------------------------------
        elif score.points == [3, 3] and voice_text == "ad in":
            score.points = [4, 3]
        elif score.points == [3, 3] and voice_text == "ad out":
            score.points = [3, 4]
        elif score.points == [4, 3] and voice_text == "deuce":
            score.points = [3, 3]
        elif score.points == [3, 4] and voice_text == "deuce":
            score.points = [3, 3]
        elif score.points == [4, 3] and voice_text == "game":
            score.games[0] += 1
            score.new_game()
        elif score.points == [3, 4] and voice_text == "game":
            score.games[1] += 1
            score.new_game()
        else:
            not_recognized = True
            voice_text = listen_to_voice()

    score.points_text[0] = score.points_text_ref[score.points[0]]
    score.points_text[1] = score.points_text_ref[score.points[1]]

