from PySide6.QtWidgets import QMainWindow

class BaseView(QMainWindow):
    def __init__(self, scene_manager):
        super().__init__()
        self.scene_manager = scene_manager
