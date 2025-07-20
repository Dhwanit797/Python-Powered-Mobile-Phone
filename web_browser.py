import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

def open_browser():
    print("Web browser is running!")

    class WebBrowser(QWidget):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Dhwanit Web Browser :-")
            self.setGeometry(100, 100, 800, 600)

            layout = QVBoxLayout()

            nav_bar = QHBoxLayout()

            back_button = QPushButton("<")
            back_button.clicked.connect(self.go_back)
            nav_bar.addWidget(back_button)

            forward_button = QPushButton(">")
            forward_button.clicked.connect(self.go_forward)
            nav_bar.addWidget(forward_button)

            refresh_button = QPushButton("⟳")
            refresh_button.clicked.connect(self.refresh_page)
            nav_bar.addWidget(refresh_button)

            home_button = QPushButton("🏠")
            home_button.clicked.connect(self.go_home)
            nav_bar.addWidget(home_button)

            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.load_url)
            nav_bar.addWidget(self.url_bar)

            go_button = QPushButton("Go")
            go_button.clicked.connect(self.load_url)
            nav_bar.addWidget(go_button)

            layout.addLayout(nav_bar)

            self.browser = QWebEngineView()
            self.browser.urlChanged.connect(self.update_url_bar)
            layout.addWidget(self.browser)

            self.setLayout(layout)

            self.go_home()

        def load_url(self):
            url = self.url_bar.text()
            if not url.startswith("http"):
                url = "http://" + url
            self.browser.setUrl(QUrl(url))

        def go_home(self):
            self.browser.setUrl(QUrl("http://www.google.com"))
            self.url_bar.setText("http://www.google.com")

        def go_back(self):
            self.browser.back()

        def go_forward(self):
            self.browser.forward()

        def refresh_page(self):
            self.browser.reload()

        def update_url_bar(self, qurl):
            self.url_bar.setText(qurl.toString())

    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    open_browser()