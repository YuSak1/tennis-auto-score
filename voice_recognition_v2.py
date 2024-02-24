import speech_recognition as sr
import sound
import copy


def listen_to_voice():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # print("Listening...")
            voice = listener.listen(source, timeout=5, phrase_time_limit=3)
            voice_text = listener.recognize_google(voice)
            # voice_text = listener.recognize_google(voice, language="ja-JP")
            # print(voice_text)
            return voice_text
    except:
        # print('Sorry, I could not understand')
        return "error"


def recognize_score(score):
    not_recognized: bool = True
    voice_text = listen_to_voice()

    # Player 1 is serving
    if score.server == 0:
        while not_recognized:
            not_recognized = False
            if voice_text == "cancel":
                score.points = copy.copy(score.previous_points)
                print("Score is canceled.")
                break
            # ------------------------------------------------------
            score.previous_points = copy.copy(score.points)
            if score.points == [0, 0] and (voice_text == "15 love" or voice_text == "one"):
                score.points = [1, 0]
                sound.say("15 love")
            elif score.points == [1, 0] and (voice_text == "30 love" or voice_text == "one"):
                score.points = [2, 0]
                sound.say("30 love")
            elif score.points == [2, 0] and (voice_text == "40 love" or voice_text == "one"):
                score.points = [3, 0]
                sound.say("40 love")
            elif score.points == [3, 0] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 0] and (voice_text == "love 15" or voice_text == "two"):
                score.points = [0, 1]
                sound.say("love 15")
            elif score.points == [0, 1] and (voice_text == "love 30" or voice_text == "two"):
                score.points = [0, 2]
                sound.say("love 30")
            elif score.points == [0, 2] and (voice_text == "love 40" or voice_text == "two"):
                score.points = [0, 3]
                sound.say("love 40")
            elif score.points == [0, 3] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 1] and (voice_text == "15 all" or voice_text == "one"):
                score.points = [1, 1]
                sound.say("15 all")
            elif score.points == [1, 1] and (voice_text == "3015" or voice_text == "one"):
                score.points = [2, 1]
                sound.say("30 15")
            elif score.points == [2, 1] and (voice_text == "4015" or voice_text == "one"):
                score.points = [3, 1]
                sound.say("40 15")
            elif score.points == [3, 1] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [1, 0] and (voice_text == "15 all" or voice_text == "two"):
                score.points = [1, 1]
                sound.say("15 all")
            elif score.points == [1, 1] and (voice_text == "1530" or voice_text == "two"):
                score.points = [1, 2]
                sound.say("15 30")
            elif score.points == [1, 2] and (voice_text == "1540" or voice_text == "two"):
                score.points = [1, 3]
                sound.say("15 40")
            elif score.points == [1, 3] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 2] and (voice_text == "1530" or voice_text == "one"):
                score.points = [1, 2]
                sound.say("15 30")
            elif score.points == [1, 2] and (voice_text == "30 all" or voice_text == "one"):
                score.points = [2, 2]
                sound.say("30 all")
            elif score.points == [2, 2] and (voice_text == "4030" or voice_text == "one"):
                score.points = [3, 2]
                sound.say("40 30")
            elif score.points == [3, 2] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [2, 0] and (voice_text == "3015" or voice_text == "two"):
                score.points = [2, 1]
                sound.say("30 15")
            elif score.points == [2, 1] and (voice_text == "30 all" or voice_text == "two"):
                score.points = [2, 2]
                sound.say("30 all")
            elif score.points == [2, 2] and (voice_text == "3040" or voice_text == "two"):
                score.points = [2, 3]
                sound.say("30 40")
            elif score.points == [2, 3] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 3] and (voice_text == "1540" or voice_text == "one"):
                score.points = [1, 3]
                sound.say("15 40")
            elif score.points == [1, 3] and (voice_text == "3040" or voice_text == "one"):
                score.points = [2, 3]
                sound.say("30 40")
            elif score.points == [2, 3] and (voice_text == "deuce" or voice_text == "one"):
                score.points = [3, 3]
                sound.say("Deuce")
            # ------------------------------------------------------
            elif score.points == [3, 0] and (voice_text == "4015" or voice_text == "two"):
                score.points = [3, 1]
                sound.say("40 15")
            elif score.points == [3, 1] and (voice_text == "4030" or voice_text == "two"):
                score.points = [3, 2]
                sound.say("40 30")
            elif score.points == [3, 2] and (voice_text == "deuce" or voice_text == "two"):
                score.points = [3, 3]
                sound.say("Deuce")
            # ------------------------------------------------------
            elif score.points == [3, 3] and (voice_text == "add in" or voice_text == "one"):
                score.points = [4, 3]
                sound.say("Add in")
            elif score.points == [3, 3] and (voice_text == "add out" or voice_text == "two"):
                score.points = [3, 4]
                sound.say("Add out")
            elif score.points == [4, 3] and (voice_text == "deuce" or voice_text == "two"):
                score.points = [3, 3]
                sound.say("Deuce")
            elif score.points == [3, 4] and (voice_text == "deuce" or voice_text == "one"):
                score.points = [3, 3]
                sound.say("Deuce")
            elif score.points == [4, 3] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            elif score.points == [3, 4] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            else:
                not_recognized = True
                print(voice_text)
                voice_text = listen_to_voice()

    # Player 2 is serving
    else:
        while not_recognized:
            not_recognized = False
            if voice_text == "cancel":
                score.points = copy.copy(score.previous_points)
                print("Score is canceled.")
                break
            # ------------------------------------------------------
            score.previous_points = copy.copy(score.points)
            if score.points == [0, 0] and (voice_text == "love 15" or voice_text == "one"):
                score.points = [1, 0]
                sound.say("love 15")
            elif score.points == [1, 0] and (voice_text == "love 30" or voice_text == "one"):
                score.points = [2, 0]
                sound.say("love 30")
            elif score.points == [2, 0] and (voice_text == "love 40" or voice_text == "one"):
                score.points = [3, 0]
                sound.say("love 40")
            elif score.points == [3, 0] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 0] and (voice_text == "15 love" or voice_text == "two"):
                score.points = [0, 1]
                sound.say("15 love")
            elif score.points == [0, 1] and (voice_text == "30 love" or voice_text == "two"):
                score.points = [0, 2]
                sound.say("30 love")
            elif score.points == [0, 2] and (voice_text == "40 love" or voice_text == "two"):
                score.points = [0, 3]
                sound.say("40 love")
            elif score.points == [0, 3] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 1] and (voice_text == "15 all" or voice_text == "one"):
                score.points = [1, 1]
                sound.say("15 all")
            elif score.points == [1, 1] and (voice_text == "1530" or voice_text == "one"):
                score.points = [2, 1]
                sound.say("15 30")
            elif score.points == [2, 1] and (voice_text == "1540" or voice_text == "one"):
                score.points = [3, 1]
                sound.say("15 40")
            elif score.points == [3, 1] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [1, 0] and (voice_text == "15 all" or voice_text == "two"):
                score.points = [1, 1]
                sound.say("15 all")
            elif score.points == [1, 1] and (voice_text == "3015" or voice_text == "two"):
                score.points = [1, 2]
                sound.say("30 15")
            elif score.points == [1, 2] and (voice_text == "4015" or voice_text == "two"):
                score.points = [1, 3]
                sound.say("40 15")
            elif score.points == [1, 3] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 2] and (voice_text == "3015" or voice_text == "one"):
                score.points = [1, 2]
                sound.say("30 15")
            elif score.points == [1, 2] and (voice_text == "30 all" or voice_text == "one"):
                score.points = [2, 2]
                sound.say("30 all")
            elif score.points == [2, 2] and (voice_text == "3040" or voice_text == "one"):
                score.points = [3, 2]
                sound.say("30 40")
            elif score.points == [3, 2] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [2, 0] and (voice_text == "1530" or voice_text == "two"):
                score.points = [2, 1]
                sound.say("15 30")
            elif score.points == [2, 1] and (voice_text == "30 all" or voice_text == "two"):
                score.points = [2, 2]
                sound.say("30 all")
            elif score.points == [2, 2] and (voice_text == "4030" or voice_text == "two"):
                score.points = [2, 3]
                sound.say("40 30")
            elif score.points == [2, 3] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            # ------------------------------------------------------
            elif score.points == [0, 3] and (voice_text == "4015" or voice_text == "one"):
                score.points = [1, 3]
                sound.say("40 15")
            elif score.points == [1, 3] and (voice_text == "4030" or voice_text == "one"):
                score.points = [2, 3]
                sound.say("40 30")
            elif score.points == [2, 3] and (voice_text == "deuce" or voice_text == "one"):
                score.points = [3, 3]
                sound.say("Deuce")
            # ------------------------------------------------------
            elif score.points == [3, 0] and (voice_text == "1540" or voice_text == "two"):
                score.points = [3, 1]
                sound.say("15 40")
            elif score.points == [3, 1] and (voice_text == "3040" or voice_text == "two"):
                score.points = [3, 2]
                sound.say("30 40")
            elif score.points == [3, 2] and (voice_text == "deuce" or voice_text == "two"):
                score.points = [3, 3]
                sound.say("Deuce")
            # ------------------------------------------------------
            elif score.points == [3, 3] and (voice_text == "add out" or voice_text == "one"):
                score.points = [4, 3]
                sound.say("Add out")
            elif score.points == [3, 3] and (voice_text == "add in" or voice_text == "two"):
                score.points = [3, 4]
                sound.say("Add in")
            elif score.points == [4, 3] and (voice_text == "deuce" or voice_text == "two"):
                score.points = [3, 3]
                sound.say("Deuce")
            elif score.points == [3, 4] and (voice_text == "deuce" or voice_text == "one"):
                score.points = [3, 3]
                sound.say("Deuce")
            elif score.points == [4, 3] and (voice_text == "game" or voice_text == "one"):
                score.new_game(0)
                sound.say("Game")
            elif score.points == [3, 4] and (voice_text == "game" or voice_text == "two"):
                score.new_game(1)
                sound.say("Game")
            else:
                not_recognized = True
                print(voice_text)
                voice_text = listen_to_voice()

    score.points_text[0] = score.points_text_ref[score.points[0]]
    score.points_text[1] = score.points_text_ref[score.points[1]]

