from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from Views.base_view import BaseView

class MenuView(BaseView):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.setWindowTitle("Menu")
        
        layout = QVBoxLayout()
        
        start_button = QPushButton("Start Game")
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button)
        
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(self.quit_game)
        layout.addWidget(quit_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def start_game(self):
        from Views.game_view import GameView
        game_view = GameView(self.scene_manager)
        self.scene_manager.set_scene(game_view)
    
    def quit_game(self):
        self.scene_manager.current_scene.close()
