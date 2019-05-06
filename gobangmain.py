#定义主程序,启动游戏界面并循环规则

WIDTH=540
HEIGHT=540

from chessboard import *
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon,QPalette,QBrush,QPixmap

class GoBang(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.chessbord=ChessBoard()
        palette_board= QPalette()
        palette_board.setBrush(self.backgroundRole(),QBrush(QPixmap('img/chessboard.jpg')))
        self.setPalette(palette_board)

        self.resize(WIDTH,HEIGHT)

        self.setWindowTitle('五子棋')
        self.setWindowIcon(QIcon('img/chessboard.jpg'))
        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    gb=GoBang()
    sys.exit(app.exec_())