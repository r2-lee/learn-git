# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\codes\project\code\gui\signalFFT.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(540, 480)
        self.GraphDraw = QtWidgets.QGroupBox(Form)
        self.GraphDraw.setGeometry(QtCore.QRect(11, 11, 314, 93))
        self.GraphDraw.setObjectName("GraphDraw")
        self.gridLayout = QtWidgets.QGridLayout(self.GraphDraw)
        self.gridLayout.setObjectName("gridLayout")
        self.chk_absfft = QtWidgets.QCheckBox(self.GraphDraw)
        self.chk_absfft.setObjectName("chk_absfft")
        self.gridLayout.addWidget(self.chk_absfft, 0, 0, 1, 1)
        self.chk_phifft = QtWidgets.QCheckBox(self.GraphDraw)
        self.chk_phifft.setObjectName("chk_phifft")
        self.gridLayout.addWidget(self.chk_phifft, 0, 1, 1, 1)
        self.chk_signal = QtWidgets.QCheckBox(self.GraphDraw)
        self.chk_signal.setObjectName("chk_signal")
        self.gridLayout.addWidget(self.chk_signal, 0, 2, 1, 1)
        self.chk_origin = QtWidgets.QCheckBox(self.GraphDraw)
        self.chk_origin.setObjectName("chk_origin")
        self.gridLayout.addWidget(self.chk_origin, 1, 0, 1, 1)
        self.chk_noise = QtWidgets.QCheckBox(self.GraphDraw)
        self.chk_noise.setObjectName("chk_noise")
        self.gridLayout.addWidget(self.chk_noise, 1, 1, 1, 1)
        self.btn_draw = QtWidgets.QPushButton(self.GraphDraw)
        self.btn_draw.setObjectName("btn_draw")
        self.gridLayout.addWidget(self.btn_draw, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.GraphDraw.setTitle(_translate("Form", "图像"))
        self.chk_absfft.setText(_translate("Form", "幅频图"))
        self.chk_phifft.setText(_translate("Form", "相频图"))
        self.chk_signal.setText(_translate("Form", "原始信号图"))
        self.chk_origin.setText(_translate("Form", "显示信号"))
        self.chk_noise.setText(_translate("Form", "显示杂波"))
        self.btn_draw.setText(_translate("Form", "绘制"))
