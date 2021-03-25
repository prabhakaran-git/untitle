from PyQt5 import  QtWidgets as Widgets
from PyQt5 import QtCore
import qtawesome as qta
import sys
import os

class MainWindow(Widgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) 
        self.setWindowTitle("PyTube Download")
        self.dragPos = QtCore.QPoint()
        self.initUI()
        
    def initUI(self) -> None:
        self._set_window_geometry()
        self.cotainer = Widgets.QFrame(self)
        self.cotainer.setObjectName('container')
        self.content = Widgets.QFrame(self.cotainer)
        self._toolbar_ui()
        self.content.resize(self.width(), 10 + self.height() - self.toolbar.height())
        self.content.move(0, self.toolbar.height())
        self._footer_ui()
        self._load_style_sheet()
        
    def _toolbar_ui(self):
        self.toolbar = Widgets.QFrame(self.cotainer)
        self.toolbar.setObjectName("toolbar")
        self.toolbar.resize(self.width(), 50)
        self.toolbar.mouseMoveEvent = self._toolbar_mouse_move_event
        self.toolbar.mousePressEvent = self._toolbar_mouse_press_event
        title_label = Widgets.QLabel('[ PyTube Downloader ]', self.toolbar)
        title_label.setObjectName('title_label')
        title_label.resize(int(self.width()*0.18), self.toolbar.height())
        title_label.move(0, 0)
        title_label.setAlignment(QtCore.Qt.AlignCenter)

    def _footer_ui(self):
        self.footer = Widgets.QFrame(self.cotainer)
        self.footer.setObjectName("footer")
        self.footer.resize(self.width(), self.height() - self.content.height())
        self.footer.move(0, self.content.height())
        
    def _load_style_sheet(self) -> None:
        file_path = os.path.join(os.path.dirname(__file__), 'styles.css')
        with open(file_path, 'r') as file:
            self.setStyleSheet(file.read())
    
    def _set_window_geometry(self) -> None:
        size = Widgets.QApplication.primaryScreen().size()
        width, height = int(size.width() * 0.62), int(size.height() * 0.86)
        x, y = int(size.width() * 0.17), int(size.height() * 0.04)
        self.setGeometry(x, y, width, height)
    
    def _toolbar_mouse_press_event(self, event): 
        self.dragPos = event.globalPos()
        
    def _toolbar_mouse_move_event(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept() 
            
if __name__ == '__main__':
    
    application =  Widgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec())