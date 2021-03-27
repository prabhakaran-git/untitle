from PyQt5 import  QtWidgets as Widgets
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
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

        #Call all ui 
        self._set_window_geometry()
        self.cotainer_frame = Widgets.QFrame(self)
        self.cotainer_frame.setObjectName('container')
        self.content_frame = Widgets.QFrame(self.cotainer_frame)
        self._toolbar_ui()
        self.content_frame.resize(self.width(), 10 + self.height() - self.toolbar_frame.height())
        self.content_frame.move(0, self.toolbar_frame.height())
        self._footer_ui()
        self._search_content_ui()
        self._load_style_sheet()
        
    def _toolbar_ui(self):

        #Toolbar frame
        self.toolbar_frame = Widgets.QFrame(self.cotainer_frame)
        self.toolbar_frame.setObjectName("toolbar")
        self.toolbar_frame.resize(self.width(), int(self.height()*0.065))
        self.toolbar_frame.mouseMoveEvent = self._toolbar_mouse_move_event
        self.toolbar_frame.mousePressEvent = self._toolbar_mouse_press_event
        
        #Window title label
        app_title_label = Widgets.QLabel('PyTube Downloader', self.toolbar_frame)
        app_title_label.setObjectName('app_title')
        app_title_label.resize(int(self.width()*0.5), self.toolbar_frame.height())
        app_title_label.move(8, 0)
        font = QFont()
        font.setPointSize(12)
        app_title_label.setFont(font)
    
    def _search_content_ui(self):

        #Search container frame
        self.seach_frame = Widgets.QFrame(self.content_frame)
        self.seach_frame.resize(self.width(), int(self.height()*0.4))
        self.seach_frame.move(0, int(self.height()*0.2))

        #Search title label
        self.search_title_label = Widgets.QLabel(self.seach_frame)
        self.search_title_label.resize(self.width(), int(self.seach_frame.height()*0.4))
        self.search_title_label.setText("PyTube")
        font = QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.search_title_label.setFont(font)
        del font
        self.search_title_label.setStyleSheet(u"color: rgb(106, 190, 190)")
        self.search_title_label.setAlignment(QtCore.Qt.AlignCenter)

        #URL textbox
        self.url_textbox = Widgets.QLineEdit(self.seach_frame)
        self.url_textbox.resize(int(self.width()*0.80), 40)
        self.url_textbox.move(int(self.width()*0.10), self.search_title_label.x()+ self.search_title_label.height())
        self.url_textbox.setPlaceholderText("Enter the youtube video URL")
        self.url_textbox.setObjectName('url_textbox')
        font = QFont()
        font.setFamily("Cambria")
        font.setPointSize(13)
        self.url_textbox.setFont(font)
        del font

        #Error label
        self.error_label = Widgets.QLabel(self.seach_frame)
        self.error_label.resize(self.width(), 40)
        self.error_label.move(0, self.url_textbox.y() + self.url_textbox.height() + 20)
        self.error_label.setObjectName("error")
        self.error_label.setText("Invliad url")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QFont()
        font.setFamily("Cambria")
        font.setPointSize(13)
        self.error_label.setFont(font)
        del font
        
    def _footer_ui(self):

        #Footer frame
        self.footer = Widgets.QFrame(self.cotainer_frame)
        self.footer.setObjectName("footer")
        self.footer.resize(self.width(), self.height() - self.content_frame.height())
        self.footer.move(0, self.content_frame.height())
        
    def _load_style_sheet(self) -> None:
        file_path = os.path.join(os.path.dirname(__file__), 'styles.css')
        with open(file_path, 'r') as file:
            self.setStyleSheet(file.read())
    
    def _set_window_geometry(self) -> None:
        size = Widgets.QApplication.primaryScreen().size()
        width, height = int(size.width() * 0.55), int(size.height() * 0.75)
        x, y = int(size.width() * 0.24), int(size.height() * 0.10)
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