import voice_recognition as vr
import score as s


def start_match() -> None:
    # score class
    score = s.Score()

    score.new_match()
    print("===================================================="
          "\nSet:    ", score.sets[0], "-", score.sets[1],
          "\nGame:   ", score.games[0], "-", score.games[1],
          "\nPoint: ", score.points_text[0], "-", score.points_text[1],
          "\n====================================================")
    # print(score.point_player1, "-", score.point_player2)

    # result = vr.recognize_score()

    while True:
        result = vr.recognize_score()
        score.increment_point(result)
        print("===================================================="
              "\nSet:    ", score.sets[0], "-", score.sets[1],
              "\nGame:   ", score.games[0], "-", score.games[1],
              "\nPoint: ", score.points_text[0], "-", score.points_text[1],
              "\n====================================================")


if __name__ == '__main__':
    print("Play!")
    start_match()
