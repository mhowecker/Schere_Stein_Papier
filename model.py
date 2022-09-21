class Option:
    def __init__(self, n: int):
        self.number = n
        if n == 1: self.text = "Schere"
        elif n == 2: self.text = "Stein"
        elif n == 3: self.text = "Papier"


class Spiel:

    # 1 - Schere
    # 2 - Stein
    # 3 - Papier
    def __init__(self):
        self.rounds = 0
        self.p1_points = 0
        self.p2_points = 0
        self.p1_last_move = None
        self.p2_last_move = None

    def reset(self):
        self.rounds = 0
        self.p1_points = 0
        self.p2_points = 0
        self.p1_last_move = None
        self.p2_last_move = None

    def new_turn(self, player1: Option, player2: Option):
        winner = Spiel._calc_winner_(player1.number, player2.number)
        self.p1_last_move = player1
        self.p2_last_move = player2
        self.rounds += 1
        if winner == 1: self.p1_points += 1
        if winner == 2: self.p2_points += 1

    @staticmethod
    def _calc_winner_(p1: int, p2: int) -> int:
        if p1 == p2: return 0
        elif p1 == 1:
            if p2 == 2: return 2
            else: return 1
        elif p1 == 2:
            if p2 == 1: return 1
            else: return 2
        elif p1 == 3:
            if p2 == 1: return 2
            else: return 1


if __name__ == '__main__':
    rounds = ((1, 1), (2, 2), (3, 3),
              (1, 2), (2, 3), (3, 1),
              (1, 3), (2, 1), (3, 2))
    s = Spiel()
    for r in range(len(rounds)):
        s.new_turn(rounds[r][0], rounds[r][1])
        print("{0} Runden gespielt: Player1 {1} - {2} Player2".format(s.rounds, s.p1_points, s.p2_points))
