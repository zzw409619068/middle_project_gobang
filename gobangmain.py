#定义主程序,启动游戏界面并循环规则

from chessboard import *
import sys
from PyQt5.QtWidgets import QApplication,QWidget

class GoBang(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def UI(self):
        self.chessbord=ChessBoard()

