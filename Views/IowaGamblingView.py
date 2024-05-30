from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QApplication, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class IowaGamblingView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Iowa Gambling Game")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.balance_label = QLabel(f"Balance: $1000")
        self.layout.addWidget(self.balance_label)

        self.deck_buttons = []
        for i in range(4):
            button = QPushButton(f"Deck {i+1}")
            self.deck_buttons.append(button)
            self.layout.addWidget(button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def update_chart(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        data.groupby("Deck").sum().plot(kind='bar', y='Result', ax=ax)
        self.canvas.draw()
