import copy


class Score:

    def __init__(self):
        self.sets_to_win = 1
        self.points_text_ref = ('0', '15', '30', '40', 'Ad')
        self.points = [0, 0]
        self.points_text = ["00", "00"]
        self.games = [0, 0]
        self.sets = [0, 0]
        self.previous_points = [0, 0]
        self.server = 0
        self.previous_points = [0, 0]
        self.previous_voice_text = ""
        self.game_set = False

    def new_game(self, game_won_by) -> None:
        self.points = [0, 0]
        self.points_text = ["00", "00"]
        # Change server
        if self.server == 0:
            self.server = 1
        else:
            self.server = 0

        if self.games[game_won_by] == 5:
            self.new_set(game_won_by)
        else:
            self.games[game_won_by] += 1

    def new_set(self, set_won_by) -> None:
        self.points = [0, 0]
        self.points_text = ["00", "00"]
        self.games = [0, 0]

        if self.sets[set_won_by] == self.sets_to_win-1:
            print("Game set!")
            self.game_set = True
        else:
            self.sets[set_won_by] += 1

    def new_match(self) -> None:
        self.points = [0, 0]
        self.points_text = ["00", "00"]
        self.games = [0, 0]
        self.sets = [0, 0]

    # Not used for voice_recognition_v2.py
    def increment_point(self, player) -> None:
        # undo the score
        if player == -1:
            self.points = copy.copy(self.previous_points)
            self.points_text[0] = self.points_text_ref[self.points[0]]
            self.points_text[1] = self.points_text_ref[self.points[1]]
            return None
        # increment point for player 1 or 2
        self.previous_points = copy.copy(self.points)

        if self.points == [3, 3]:
            self.points[player] += 1
        elif self.points == [4, 3] and player == 0:
            self.games[0] += 1
            self.new_game()
        elif self.points == [3, 4] and player == 1:
            self.games[1] += 1
            self.new_game()
        elif self.points == [4, 3] and player == 1:
            self.points[0] -= 1
        elif self.points == [3, 4] and player == 0:
            self.points[1] -= 1
        elif self.points[0] == 3 and player == 0:
            self.games[0] += 1
            self.new_game()
        elif self.points[1] == 3 and player == 1:
            self.games[1] += 1
            self.new_game()
        else:
            self.points[player] += 1
        # print(self.points)

        self.points_text[0] = self.points_text_ref[self.points[0]]
        self.points_text[1] = self.points_text_ref[self.points[1]]
