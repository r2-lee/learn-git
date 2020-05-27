import os
import sys

d = os.path.dirname(__file__)
__path = os.path.dirname(d)
sys.path.append(__path) # 添加自己指定的搜索路径

from PyQt5.QtCore import Qt
import PyQt5.QtWidgets as QtWidgets
import matplotlib as mpl

from Ui_signalDraw import Ui_Form
import myWave.CreatWave as CreatWave
from myFigureCanvas import QmyFigureCanvas

# 黑体：SimHei 宋体：SimSun 新宋体：NSimSun 仿宋：FangSong  楷体：KaiTi
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.size'] = 9  # 显示汉字
mpl.rcParams['axes.unicode_minus'] = False  # 减号unicode编码

class signalDraw(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.wave = CreatWave.CW()

        self.__setupWidget()      #
        self.__drawSignal()

    def __setupWidget(self):
        layout = QtWidgets.QHBoxLayout()
        splitter = QtWidgets.QSplitter(self)
        splitterV = QtWidgets.QSplitter(self)
        splitterV.setOrientation(Qt.Vertical)

        splitterV.addWidget(self.ui.SetSignal)
        splitterV.addWidget(self.ui.SetNoise)

        self.Figure = QmyFigureCanvas()

        splitter.addWidget(splitterV)
        splitter.setSizes([100,200])
        splitter.addWidget(self.Figure)
        splitter.setSizes([200,600])

        layout.addWidget(splitter)
        self.setLayout(layout)

    def __drawSignal(self):
        self.Figure.figure.clear()   #清除图表

        ax1 = self.Figure.figure.add_subplot(2,1,1)
        ax1.plot(self.wave.x(),self.wave.y(noise=True))
        ax1.set_title("带有噪声的信号")

        ax2 = self.Figure.figure.add_subplot(2,1,2)
        ax2.plot(self.wave.x(),self.wave.y(noise=False))
        ax2.set_title("不带噪声的信号")

        self.Figure.figure.tight_layout()

if __name__ == "__main__":
    import sys
    qapp = QtWidgets.QApplication(sys.argv)
    app = signalDraw()
    app.show()
    sys.exit(qapp.exec_())