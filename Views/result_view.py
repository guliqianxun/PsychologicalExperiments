from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from Views.base_view import BaseView

class ResultView(BaseView):
    def __init__(self, scene_manager):
        super().__init__(scene_manager)
        self.setWindowTitle("Game Results")
        
        layout = QVBoxLayout()
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.display_game_results()
    
    def display_game_results(self):
        data = pd.read_csv("game_data.csv")
        self.update_chart(data)
    
    def update_chart(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        data.groupby("Deck").sum().plot(kind='bar', y='Result', ax=ax)
        self.canvas.draw()
