import sys
import os
import pandas as pd
from Models.IowaGamblingModel import IowaGamblingModel
from Views.IowaGamblingView import IowaGamblingView
from PySide6.QtCore import Slot, QUrl
from PySide6.QtWidgets import QApplication
from pyecharts.charts import Bar
from pyecharts import options as opts

class IowaGamblingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        for index, button in enumerate(self.view.deck_buttons):
            button.clicked.connect(self.create_play_game_handler(index))

    def create_play_game_handler(self, deck_index):
        @Slot()
        def handler():
            self.play_game(deck_index)
        return handler

    def play_game(self, deck_index):
        result, balance = self.model.play_game(deck_index)
        self.view.balance_label.setText(f"Balance: ${balance}")
        self.view.result_label.setText(f"Drew {result} from Deck {deck_index + 1}")

        if self.model.is_game_over():
            self.end_game()

    def end_game(self):
        self.view.result_label.setText("Game Over!")
        for button in self.view.deck_buttons:
            button.setDisabled(True)
        self.model.save_game_data()
        self.display_game_results()

    def display_game_results(self):
        data = pd.read_csv("game_data.csv")
        self.view.update_chart(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = IowaGamblingModel()
    view = IowaGamblingView()
    controller = IowaGamblingController(model, view)
    view.show()
    sys.exit(app.exec())