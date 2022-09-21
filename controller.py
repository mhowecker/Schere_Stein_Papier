import sys
from PyQt6.QtWidgets import QApplication
import model
import view
import random

class Controller:
    def __init__(self):
        self.model = model.Spiel()
        self.view = view.View(self)

    def reset(self):
        self.model.reset()
        self.view.reset()

    def execute(self):
        sign = self.view.get_sign()
        self.model.new_turn(model.Option(sign), model.Option(random.randint(1, 3)))
        lp1 = self.model.p1_last_move.text
        lp2 = self.model.p2_last_move.text
        pp1 = self.model.p1_points
        pp2 = self.model.p2_points
        r = self.model.rounds

        t = "Spieler [{0}], Computer [{1}]".format(lp1, lp2)

        self.view.update(pp1, pp2, r, t)


if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
