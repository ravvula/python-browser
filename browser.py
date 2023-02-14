import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton)

class Browser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Browser")
        self.setGeometry(100, 100, 800, 600)

        self.urlbar = QLineEdit()
        self.view = QWebEngineView()

        self.layout = QVBoxLayout()
        self.navigation_bar = QHBoxLayout()

        self.back_button = QPushButton("<")
        self.forward_button = QPushButton(">")

        self.back_button.clicked.connect(self.view.back)
        self.forward_button.clicked.connect(self.view.forward)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        self.navigation_bar.addWidget(self.back_button)
        self.navigation_bar.addWidget(self.forward_button)
        self.navigation_bar.addWidget(self.urlbar)

        self.layout.addLayout(self.navigation_bar)
        self.layout.addWidget(self.view)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.show()

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.view.load(q)

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())