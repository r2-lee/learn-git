import os
import sys

d = os.path.dirname(__file__)
__path = os.path.dirname(d)
sys.path.append(__path) # 添加自己指定的搜索路径

from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as QtWidgets
import matplotlib as mpl

from Ui_signalFFT import Ui_Form
import myWave.CreatWave as CreatWave
from myFigureCanvas import QmyFigureCanvas

# 黑体：SimHei 宋体：SimSun 新宋体：NSimSun 仿宋：FangSong  楷体：KaiTi
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.size'] = 9  # 显示汉字
mpl.rcParams['axes.unicode_minus'] = False  # 减号unicode编码

class signalFFT(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.wave = CreatWave.CW()

        self.__setupWidget()      #
        self.__drawFFT()


    def __setupWidget(self):
        layout = QtWidgets.QHBoxLayout()
        splitter = QtWidgets.QSplitter(self)
        splitter.setOrientation(Qt.Horizontal)

        self.Figure = QmyFigureCanvas()

        splitter.addWidget(self.Figure)
        splitter.addWidget(self.ui.GraphDraw)
        splitter.setStretchFactor(3,1)

        layout.addWidget(splitter)
        self.setLayout(layout)     

    def __drawFFT(self):
        self.Figure.figure.clear()

        ax1 = self.Figure.figure.add_subplot(2,1,1)
        ax1.plot(self.wave.fftx(),self.wave.ffty())
        ax1.set_title("幅频特性")

        ax1 = self.Figure.figure.add_subplot(2,1,2)
        ax1.plot(self.wave.fftx(),self.wave.phase())
        ax1.set_title("相频特性")

if __name__ == "__main__":
    import sys
    qapp = QtWidgets.QApplication(sys.argv)
    app = signalFFT()
    app.show()
    sys.exit(qapp.exec_())