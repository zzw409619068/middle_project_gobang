# 定义主程序,启动游戏界面并循环规则

WIDTH = 540
HEIGHT = 540

from chessboard import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QPainter, QColor,QPen
from PyQt5.QtCore import Qt

class GoBang(QWidget):
    def __init__(self):
        super().__init__()
        # self.initUI()
        self.UI()

    def initUI(self):
        self.chessbord = ChessBoard()
        palette_board = QPalette()
        palette_board.setBrush(self.backgroundRole(), QBrush(QPixmap('img/chessboard.jpg')))
        self.setPalette(palette_board)

        self.resize(WIDTH, HEIGHT)

        self.setWindowTitle('五子棋')
        self.setWindowIcon(QIcon('img/chessboard.jpg'))
        self.show()

    def UI(self):
        self.setFixedSize(520, 520)
        self.setAutoFillBackground(True)
        palette_board = QPalette()
        palette_board.setColor(palette_board.Background, QColor('#B1723C'))
        self.setPalette(palette_board)

        mouseflag = False
        centralWidget = self.setMouseTracking(True)

        painter = QPainter()
        painter.setRenderHint(painter.Antialiasing, True)

        qpen=QPen()
        pen=painter.pen()
        pen.setColor(QColor('8D5822'))
        pen.setWidth(7)
        painter.setPen(pen)

        brash=QBrush()
        brash.setColor(QColor('#EEC085'))
        brash.setStyle(Qt.SolidPattern)
        painter.setBrush(brash)
        painter.drawRect(20,20,500,500)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gb = GoBang()
    sys.exit(app.exec_())
