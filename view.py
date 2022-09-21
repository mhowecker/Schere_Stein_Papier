from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):

    # Klassenvariablen

    # GUI1 - Spinbox
    spB_sign: QSpinBox

    # GUI2 - ComboBox
    coB_sign: QComboBox

    l_round_number: QLabel
    l_player_points: QLabel
    l_computer_points: QLabel
    l_turn_last: QLabel
    pb_execute: QPushButton
    pb_reset: QPushButton
    pb_close: QPushButton

    def __init__(self, c: Controller):
        super().__init__()

        uic.loadUi("Schere_Stein_Papier2.ui", self)

        # GUI1 mit SpinBox
        # self.spB_sign.setValue(1)
        # self.spB_sign.setMinimum(1)
        # self.spB_sign.setMaximum(3)

        # GUI2 mit ComboBox
        self.coB_sign.addItem("Schere")
        self.coB_sign.addItem("Stein")
        self.coB_sign.addItem("Papier")

        self.pb_reset.clicked.connect(c.reset)
        self.pb_execute.clicked.connect(c.execute)

    def reset(self) -> None:
        self.l_round_number.setText("0")
        self.l_turn_last.setText("letzter Zug")
        self.l_player_points.setText("0")
        self.l_computer_points.setText("0")
        # GUI1 - SpinBox
        # self.spB_sign.setValue(1)

        # GUI2 - ComboBox
        self.coB_sign.setCurrentIndex(0)

    def get_sign(self) -> int:
        # GUI1 - SpinBox
        # return self.spB_sign.value()

        # GUI2 - ComboBox
        return self.coB_sign.currentIndex()+1

    def update(self, p1: int, p2: int, rounds: int, last: str) -> None:
        self.l_player_points.setText(str(p1))
        self.l_computer_points.setText(str(p2))
        self.l_round_number.setText(str(rounds))
        self.l_turn_last.setText(last)
