from PyQt5 import  QtWidgets as Widgets
from PyQt5 import QtCore
import sys
import os

class MainWindow(Widgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) 
        self.setWindowTitle("Youtube Video Downloader")
        self.dragPos = QtCore.QPoint()
        self.initUI()
        
        
    def initUI(self) -> None:
       
        self._set_window_geometry()
        self.container_frame = Widgets.QFrame(self)
        self.footer_frame = Widgets.QFrame(self)
        self._toolbar_ui()
        self._load_style_sheet()
    
    def _toolbar_ui(self):
        self.toolbar_frame = Widgets.QFrame(self)
        self.toolbar_frame.setObjectName("toolbar_frame")
        self.toolbar_frame.setFixedWidth(self.width())
        self.toolbar_frame.setFixedHeight(60)
        self.toolbar_frame.mouseMoveEvent = self.mouseMoveEvent_
        self.toolbar_frame.mousePressEvent = self.mousePressEvent_
        
    def _load_style_sheet(self) -> None:
        """
        Read the extrnal styles.css file and set the styles
        """
        file_path = os.path.join(os.path.dirname(__file__), 'styles.css')
        with open(file_path, 'r') as file:
            self.setStyleSheet(file.read())
    
    def _set_window_geometry(self) -> None:
        """
        Return the current desktop screen width and height
        """
        size = Widgets.QApplication.primaryScreen().size()
        width, height = int(size.width() * 0.62), int(size.height() * 0.86)
        x, y = int(size.width() * 0.17), int(size.height() * 0.04)
        self.setGeometry(x, y, width, height)
    
    def mousePressEvent_(self, event):                                 # +
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent_(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept() 
            
if __name__ == '__main__':
    
    application =  Widgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec())