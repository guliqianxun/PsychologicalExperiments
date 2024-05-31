from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from Views.base_view import BaseView
from Models.IowaGamblingModel import IowaGamblingModel
import pandas as pd

class GameView(BaseView):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.setWindowTitle("Iowa Gambling Game")
        
        self.model = IowaGamblingModel()
        
        layout = QVBoxLayout()
        
        self.balance_label = QLabel(f"Balance: $1000")
        layout.addWidget(self.balance_label)
        
        self.deck_buttons = []
        for i in range(4):
            button = QPushButton(f"Deck {i+1}")
            button.clicked.connect(self.create_play_game_handler(i))
            self.deck_buttons.append(button)
            layout.addWidget(button)
        
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def create_play_game_handler(self, deck_index):
        def handler():
            self.play_game(deck_index)
        return handler
    
    def play_game(self, deck_index):
        result, balance = self.model.play_game(deck_index)
        self.balance_label.setText(f"Balance: ${balance}")
        self.result_label.setText(f"Drew {result} from Deck {deck_index + 1}")
        
        if self.model.is_game_over():
            self.end_game()
    
    def end_game(self):
        self.result_label.setText("Game Over!")
        for button in self.deck_buttons:
            button.setDisabled(True)
        self.model.save_game_data()
        
        from Views.result_view import ResultView
        result_view = ResultView(self.scene_manager)
        self.scene_manager.set_scene(result_view)
