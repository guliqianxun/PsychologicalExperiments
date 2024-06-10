import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider, QTextEdit, QLineEdit, QRadioButton, QButtonGroup, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer, Qt

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Psychology Experiment")
        self.setGeometry(100, 100, 600, 400)
        self.current_pair_index = 0
        self.trial_index = 0
        self.init_ui()

    def init_ui(self):
        self.start_button = QPushButton('Start Experiment', self)
        self.start_button.clicked.connect(self.show_instructions)
        self.setCentralWidget(self.start_button)

    def show_instructions(self):
        self.clear_window()
        instructions = QTextEdit()
        instructions.setReadOnly(True)
        instructions.setText("Welcome to the experiment...\nInstructions here...")
        next_button = QPushButton('Continue')
        next_button.clicked.connect(self.start_practice_trial)
        
        layout = QVBoxLayout()
        layout.addWidget(instructions)
        layout.addWidget(next_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_practice_trial(self):
        self.clear_window()
        self.encoding_task(1)

    def encoding_task(self, trial_index):
        if trial_index <= len(trial_order):
            trial = trial_order[trial_index - 1]
            self.show_image_with_task(images[trial], tasks[(trial - 1) // 6])
        else:
            self.distractor_task()

    def show_image_with_task(self, image_path, task_text):
        self.clear_window()
        task_label = QLabel(task_text)
        task_label.setAlignment(Qt.AlignCenter)
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap)
        next_button = QPushButton('Next')
        next_button.clicked.connect(lambda: self.show_rating_task(self.trial_index))
        
        layout = QVBoxLayout()
        layout.addWidget(task_label)
        layout.addWidget(image_label)
        layout.addWidget(next_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_rating_task(self, trial_index):
        self.clear_window()
        rating_text = QTextEdit()
        rating_text.setReadOnly(True)
        rating_text.setText("Rate how vivid the image is using the 5-point scale:\n1: No image at all...\n2: Vague and dim...\n3: Moderately clear and vivid...\n4: Clear and reasonably vivid...\n5: Perfectly clear and as vivid as normal vision")
        rating_slider = QSlider(Qt.Horizontal)
        rating_slider.setRange(1, 5)
        confirm_button = QPushButton('Submit')
        confirm_button.clicked.connect(lambda: self.submit_rating(rating_slider.value(), trial_index))
        
        layout = QVBoxLayout()
        layout.addWidget(rating_text)
        layout.addWidget(rating_slider)
        layout.addWidget(confirm_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def submit_rating(self, rating, trial_index):
        # Save rating (implementation needed)
        self.show_fixation_cross(trial_index + 1)

    def show_fixation_cross(self, next_trial_index):
        self.clear_window()
        cross_label = QLabel("+")
        cross_label.setAlignment(Qt.AlignCenter)
        cross_label.setStyleSheet("font-size: 48px;")
        
        layout = QVBoxLayout()
        layout.addWidget(cross_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        QTimer.singleShot(1000, lambda: self.encoding_task(next_trial_index))

    def distractor_task(self):
        self.clear_window()
        instruction_label = QLabel('Enter the reverse of "ke67a":')
        input_field = QLineEdit()
        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(lambda: self.check_distractor_answer(input_field.text()))
        
        layout = QVBoxLayout()
        layout.addWidget(instruction_label)
        layout.addWidget(input_field)
        layout.addWidget(submit_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def check_distractor_answer(self, answer):
        if answer == 'a76ek':
            self.temporal_memory_task()
        else:
            QMessageBox.critical(self, 'Error', 'Incorrect. Try again.')

    def temporal_memory_task(self):
        self.clear_window()
        if self.current_pair_index >= len(test_pairs):
            QMessageBox.information(self, 'Information', 'All tasks completed')
            return

        pair = test_pairs[test_pair_order[self.current_pair_index]]
        memory_task_label = QLabel('Please select the image that was seen first:')
        left_img = QLabel()
        right_img = QLabel()
        left_img.setPixmap(QPixmap(pair[0]))
        right_img.setPixmap(QPixmap(pair[1]))
        left_button = QPushButton('Left')
        right_button = QPushButton('Right')
        
        left_button.clicked.connect(lambda: self.choose_first_image('left'))
        right_button.clicked.connect(lambda: self.choose_first_image('right'))
        
        layout = QVBoxLayout()
        layout.addWidget(memory_task_label)
        layout.addWidget(left_img)
        layout.addWidget(right_img)
        layout.addWidget(left_button)
        layout.addWidget(right_button)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def choose_first_image(self, choice):
        self.current_pair_index += 1
        self.temporal_memory_task()

    def clear_window(self):
        if self.centralWidget():
            self.centralWidget().deleteLater()

if __name__ == "__main__":
    # Initialize image paths and tasks
    image_folder = './images'  # Folder containing image files
    images = [f"{image_folder}/image{i}.jpg" for i in range(1, 37)]  # Replace with actual image paths
    tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5', 'Task 6']
    trial_order = random.sample(range(len(images)), len(images))
    test_pairs = [
        [images[0], images[35]], [images[14], images[15]], [images[20], images[21]], 
        [images[3], images[7]], [images[10], images[14]], [images[16], images[20]],
        [images[22], images[26]], [images[28], images[32]], [images[1], images[5]],
        [images[7], images[11]], [images[13], images[17]], [images[19], images[23]], 
        [images[25], images[29]]
    ]
    test_pair_order = random.sample(range(len(test_pairs)), len(test_pairs))

    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
