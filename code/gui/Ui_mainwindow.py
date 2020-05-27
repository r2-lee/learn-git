# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\codes\project\code\gui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 500)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actOpen = QtWidgets.QAction(MainWindow)
        self.actOpen.setObjectName("actOpen")
        self.actCloseFile = QtWidgets.QAction(MainWindow)
        self.actCloseFile.setObjectName("actCloseFile")
        self.actCloseAPP = QtWidgets.QAction(MainWindow)
        self.actCloseAPP.setObjectName("actCloseAPP")
        self.menu.addAction(self.actOpen)
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menu.addAction(self.actCloseFile)
        self.menu.addAction(self.actCloseAPP)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.actOpen.setText(_translate("MainWindow", "打开"))
        self.actOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actCloseFile.setText(_translate("MainWindow", "关闭文件"))
        self.actCloseAPP.setText(_translate("MainWindow", "关闭软件"))
