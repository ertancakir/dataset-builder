# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatasetBuilder.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

from imageCutter import ImageCutter

class Ui_DatasetBuilder(object):
    def setupUi(self, DatasetBuilder):
        DatasetBuilder.setObjectName("DatasetBuilder")
        DatasetBuilder.resize(744, 172)
        self.centralwidget = QtWidgets.QWidget(DatasetBuilder)
        self.centralwidget.setObjectName("centralwidget")
        self.imgPath = QtWidgets.QTextEdit(self.centralwidget)
        self.imgPath.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.imgPath.setReadOnly(True)
        self.imgPath.setObjectName("imgPath")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.fileChooseButtonClicked)   #This code for click event

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 17))
        self.label.setObjectName("label")
        self.dataName = QtWidgets.QTextEdit(self.centralwidget)
        self.dataName.setGeometry(QtCore.QRect(100, 50, 171, 31))
        self.dataName.setObjectName("dataName")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(100, 120, 166, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(280, 10, 201, 131))
        self.listView.setObjectName("listView")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(490, 10, 241, 131))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(DatasetBuilder)
        QtCore.QMetaObject.connectSlotsByName(DatasetBuilder)

    def retranslateUi(self, DatasetBuilder):
        _translate = QtCore.QCoreApplication.translate
        DatasetBuilder.setWindowTitle(_translate("DatasetBuilder", "Dataset Builder"))
        self.pushButton.setText(_translate("DatasetBuilder", "Choose"))
        self.label.setText(_translate("DatasetBuilder", "Data Name : "))


    def fileChooseButtonClicked(self):
        fileChooser = QWidget()
        fileChooser.setGeometry(10,10,640,480)
        fileChooser.setWindowTitle('Choose a Image File')

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(fileChooser,"Choose a Image File", "","Image Files (*.png)", options=options)
        fileChooser.show()

        self.imgPath.setText(fileName)

        imgCutter = ImageCutter(fileName)
        imgCutter.cutImage()


