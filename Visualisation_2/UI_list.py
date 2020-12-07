# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\ListWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        ListWindow.setObjectName("ListWindow")
        ListWindow.setWindowModality(QtCore.Qt.WindowModal)
        ListWindow.resize(378, 511)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListWindow.sizePolicy().hasHeightForWidth())
        ListWindow.setSizePolicy(sizePolicy)
        ListWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(ListWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RemoveButton = QtWidgets.QPushButton(ListWindow)
        self.RemoveButton.setObjectName("RemoveButton")
        self.horizontalLayout_2.addWidget(self.RemoveButton)
        self.AddButton = QtWidgets.QPushButton(ListWindow)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout_2.addWidget(self.AddButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(ListWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.ElementsArea = QtWidgets.QWidget()
        self.ElementsArea.setGeometry(QtCore.QRect(0, 0, 358, 429))
        self.ElementsArea.setAutoFillBackground(True)
        self.ElementsArea.setObjectName("ElementsArea")
        self.ElementLayout = QtWidgets.QVBoxLayout(self.ElementsArea)
        self.ElementLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.ElementLayout.setObjectName("ElementLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ElementLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.ElementsArea)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.OkButton = QtWidgets.QPushButton(ListWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OkButton.sizePolicy().hasHeightForWidth())
        self.OkButton.setSizePolicy(sizePolicy)
        self.OkButton.setMinimumSize(QtCore.QSize(100, 0))
        self.OkButton.setObjectName("OkButton")
        self.horizontalLayout.addWidget(self.OkButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ListWindow)
        self.OkButton.clicked.connect(ListWindow.accept)
        QtCore.QMetaObject.connectSlotsByName(ListWindow)

    def retranslateUi(self, ListWindow):
        _translate = QtCore.QCoreApplication.translate
        ListWindow.setWindowTitle(_translate("ListWindow", "List"))
        self.RemoveButton.setText(_translate("ListWindow", "Retirer"))
        self.AddButton.setText(_translate("ListWindow", "Ajouter"))
        self.OkButton.setText(_translate("ListWindow", "Valider"))
