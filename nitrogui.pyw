import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton
import requests
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nitro Generator")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_url)
        layout.addWidget(self.generate_button)

        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_box)
        layout.addWidget(self.copy_button)

        self.url_display = QTextEdit()
        layout.addWidget(self.url_display)

        self.central_widget.setLayout(layout)

        self.generate_timer = QTimer()
        self.generate_timer.setSingleShot(True)
        self.generate_timer.timeout.connect(lambda: self.generate_button.setText("Generate"))

        self.copy_timer = QTimer()
        self.copy_timer.setSingleShot(True)
        self.copy_timer.timeout.connect(lambda: self.copy_button.setText("Copy"))

    def get_token(self):
        url = "https://api.gx.me/profile/token"
        headers = {
            'accept':
            'application/json',
            'accept-language':
            'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            'authority':
            'api.gx.me',
            'cookie':
            'SESSION_TYPE=user; SESSION=NzFjMjg3NDAtMDhkOC00ODkwLWJhNzEtODA0YTcwMjNiM2U0',
            'origin':
            'https://www.opera.com',
            'referer':
            'https://www.opera.com/',
            'sec-ch-ua':
            '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'cross-site',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']
        else:
            print("Failed to retrieve token")
            return None

    def generate_url(self):
        token = self.get_token()
        if token:
            new_url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}\n"
            self.url_display.insertPlainText(new_url)
            self.generate_button.setText("Generated")
            self.generate_timer.start(2000)

    def copy_box(self):
        content = self.url_display.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(content)
        self.copy_button.setText("Copied")
        self.copy_timer.start(2000)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
