#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

#создание элементов интерфейса
app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Определитель победителя')
my_win.move(100, 100)
my_win.resize(400,200)
 
#vidzhety okna
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

#widgets geolocation
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)
#degenerator
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')

button.clicked.connect(show_winner)


#привязка элементов к вертикальной линии

#обработка событий

#запуск приложения
my_win.show()
app.exec_()
