import requests
import json
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QApplication
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.line = QLineEdit(self)
        self.line.setGeometry(100, 40, 70, 50)
        self.label = QLabel(self)
        self.label.setGeometry(200, 100, 800, 200)
        self.button = QPushButton(self)
        self.button.setGeometry(100, 100, 70, 50)
        self.button.setText('Вывод JSON')
        self.button.clicked.connect(self.run)

    def run(self):
        api = f'https://api.github.com/users/{self.line.text()}'
        user_data = requests.get(api).json()
        company = user_data['company']
        created_at = user_data['created_at']
        email = user_data['email']
        id = user_data['id']
        name = user_data['name']
        url = user_data['url']
        json_data = {'company': company, 'created_at': created_at, 'email': email, 'id': id, 'name': name, 'url': url}
        with open('C:/Users/Daniel/Desktop/VS Code/PL-Rodionov/PL-Rodionov/res.json', 'w') as wr:
            json.dump(json_data, wr)
        self.label.setText(f'{json_data}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())