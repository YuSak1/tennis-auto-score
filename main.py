import voice_recognition as vr
import voice_recognition_v2 as vr2
import score as s
import listen


def start_match() -> None:
    # score class
    score = s.Score()
    print("Who is serving first? (1 or 2)")
    while True:
        text_player = listen.listen_to_voice()
        if text_player == "one":
            score.server = 0
            break
        elif text_player == "two":
            score.server = 1
            break

    score.new_match()
    # print("===================================================="
    #       "\n          Player1       Player2",
    #       "\nSet:       ", score.sets[0], "     -     ", score.sets[1],
    #       "\nGame:      ", score.games[0], "     -     ", score.games[1],
    #       "\nPoint:    ", score.points_text[0], "     -    ", score.points_text[1],
    #       "\n====================================================")
    # print(score.point_player1, "-", score.point_player2)

    while not score.game_set:
        # result = vr.recognize_score()
        # score.increment_point(result)
        print("===================================================="
              "\n          Player1       Player2",
              "\nSet:       ", score.sets[0], "     -     ", score.sets[1],
              "\nGame:      ", score.games[0], "     -     ", score.games[1],
              "\nPoint:    ", score.points_text[0], "     -    ", score.points_text[1],
              "\n====================================================")

        vr2.recognize_score(score)


if __name__ == '__main__':
    print("Say 'Play' to start.")
    while True:
        text_start = listen.listen_to_voice()
        if text_start == "play":
            start_match()
            break



