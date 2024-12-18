import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ask for URL
        url, okPressed = QInputDialog.getText(self, "Enter URL", "URL:", QLineEdit.Normal, "")
        if okPressed and url != '':
            self.browser = QWebEngineView()
            self.setCentralWidget(self.browser)
            self.browser.setUrl(QUrl(url))
        else:
            sys.exit(0)

        # Set window size to half of the screen width
        screen_rect = QApplication.desktop().availableGeometry()
        half_screen_width = screen_rect.width() // 2
        self.setGeometry(screen_rect.x(), screen_rect.y(), half_screen_width, screen_rect.height())

        # Center the window on the screen
        self.move(screen_rect.x() + (screen_rect.width() - self.width()) // 2, screen_rect.y() + (screen_rect.height() - self.height()) // 2)

        # Allow resizing and customize window
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)

        # Show the window
        self.show()

    def navigate_to_url(self):
        q, okPressed = QInputDialog.getText(self, "Enter URL", "URL:", QLineEdit.Normal, "")
        if okPressed and q != '':
            self.browser.setUrl(QUrl(q))

app = QApplication(sys.argv)
QApplication.setApplicationName("MirroMyPhone")
window = Browser()
app.exec_()
