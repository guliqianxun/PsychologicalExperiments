from PySide6.QtWidgets import QMainWindow

class SceneManager:
    def __init__(self):
        self.current_scene = None

    def set_scene(self, scene: QMainWindow):
        if self.current_scene:
            self.current_scene.close()
        self.current_scene = scene
        self.current_scene.show()
