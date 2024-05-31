from PySide6.QtWidgets import QApplication
import sys
from utils.scene_manager import SceneManager
from Views.menu_view import MenuView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scene_manager = SceneManager()
    
    # 初始化并显示菜单场景
    menu_view = MenuView(scene_manager)
    scene_manager.set_scene(menu_view)
    
    sys.exit(app.exec())
