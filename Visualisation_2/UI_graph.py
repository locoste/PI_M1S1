# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\GraphWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(890, 709)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\UI\\icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GraphWindow.setWindowIcon(icon)
        self.MainGrid = QtWidgets.QWidget(GraphWindow)
        self.MainGrid.setObjectName("MainGrid")
        self.gridLayout = QtWidgets.QGridLayout(self.MainGrid)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.GraphLayout = QtWidgets.QGridLayout()
        self.GraphLayout.setObjectName("GraphLayout")
        self.horizontalLayout.addLayout(self.GraphLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        GraphWindow.setCentralWidget(self.MainGrid)
        self.menuBar = QtWidgets.QMenuBar(GraphWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 890, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFichier = QtWidgets.QMenu(self.menuBar)
        self.menuFichier.setObjectName("menuFichier")
        GraphWindow.setMenuBar(self.menuBar)
        self.actionQuitter = QtWidgets.QAction(GraphWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionEnregistrer = QtWidgets.QAction(GraphWindow)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionCapturer = QtWidgets.QAction(GraphWindow)
        self.actionCapturer.setObjectName("actionCapturer")
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionCapturer)
        self.menuBar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "DataViz"))
        self.menuFichier.setTitle(_translate("GraphWindow", "Fichier"))
        self.actionQuitter.setText(_translate("GraphWindow", "Quitter"))
        self.actionEnregistrer.setText(_translate("GraphWindow", "Enregistrer"))
        self.actionCapturer.setText(_translate("GraphWindow", "Capturer"))
