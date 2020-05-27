# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\codes\project\code\gui\signalDraw.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 592)
        self.SetSignal = QtWidgets.QGroupBox(Form)
        self.SetSignal.setGeometry(QtCore.QRect(70, 60, 619, 216))
        self.SetSignal.setObjectName("SetSignal")
        self.checkBox = QtWidgets.QCheckBox(self.SetSignal)
        self.checkBox.setGeometry(QtCore.QRect(80, 140, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.SetNoise = QtWidgets.QGroupBox(Form)
        self.SetNoise.setGeometry(QtCore.QRect(50, 330, 619, 216))
        self.SetNoise.setObjectName("SetNoise")
        self.checkBox_2 = QtWidgets.QCheckBox(self.SetNoise)
        self.checkBox_2.setGeometry(QtCore.QRect(390, 170, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SetSignal.setTitle(_translate("Form", "设置信号"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.SetNoise.setTitle(_translate("Form", "设置杂波"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
