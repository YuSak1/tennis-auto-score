import copy


class Score:

    def __init__(self):
        self.points_text_ref = ('0', '15', '30', '40', 'Ad')
        self.points = [0, 0]
        self.points_text = ["00", "00"]
        self.games = [0, 0]
        self.sets = [0, 0]
        self.previous_points = [0, 0]
        self.server = 0

    def new_game(self) -> None:
        self.points = [0, 0]
        self.points_text = ["00", "00"]

    def new_set(self) -> None:
        self.games = [0, 0]
        self.new_game()

    def new_match(self) -> None:
        self.new_set()
        self.new_game()
        self.sets = [0, 0]

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
