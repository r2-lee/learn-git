import os
import sys

d = os.path.dirname(__file__)
__path = os.path.dirname(d)
sys.path.append(__path) # 添加自己指定的搜索路径

from PyQt5.QtCore import Qt, pyqtSlot
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QGuiApplication
from Ui_mainwindow import Ui_MainWindow


##############小部件##########
from signalDraw import signalDraw
from signalFFT import signalFFT
from Recorder import Recorder
from neo4j import neo4j

class QMyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(QGuiApplication.primaryScreen().availableSize() * 4 / 5);
        self.setWindowTitle("项目  v0.26")

###-----------------动作设置
        self.ui.actOpen.triggered.connect(self.openfile)
        self.ui.actCloseAPP.triggered.connect(self.close)

###-----------------tab页面设置
        self.ui.tabsignalDraw = QtWidgets.QWidget()
        self.ui.tabWidget.addTab(self.ui.tabsignalDraw,'信号')

        self.ui.tabsignalFFT = QtWidgets.QWidget()
        self.ui.tabWidget.addTab(self.ui.tabsignalFFT,'FFT')

        self.ui.tabRecord = QtWidgets.QWidget()
        self.ui.tabWidget.addTab(self.ui.tabRecord,'录音')

        self.ui.tabNeo4j = QtWidgets.QWidget()
        self.ui.tabWidget.addTab(self.ui.tabNeo4j,'Neo4j')

        self.__Tab1()
        self.__Tab2()
        self.__Tab3()
        self.__Tab4()



    def openfile(self):
        self.File = QtWidgets.QFileDialog.getOpenFileName(self,'选择文件','./','ALL(*.*);;媒体(*.mp3 *.wav)','媒体(*.mp3 *.wav)')


    def __Tab1(self):
        layout = QtWidgets.QHBoxLayout()
        draw = signalDraw()
        layout.addWidget(draw)
        self.ui.tabsignalDraw.setLayout(layout)

    def __Tab2(self):
        layout = QtWidgets.QHBoxLayout()
        fft = signalDraw()
        layout.addWidget(fft)
        self.ui.tabsignalFFT.setLayout(layout)

    def __Tab3(self):
        layout = QtWidgets.QHBoxLayout()
        wid = Recorder()
        layout.addWidget(wid)
        self.ui.tabRecord.setLayout(layout)

    def __Tab4(self):
        layout = QtWidgets.QHBoxLayout()
        Neo = neo4j()
        layout.addWidget(Neo)
        self.ui.tabNeo4j.setLayout(layout)


if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = QMyWin()
    app.show()
    sys.exit(qapp.exec_())
