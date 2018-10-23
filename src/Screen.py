# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatasetBuilder.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QListWidget

from ImageCutter import ImageCutter

class Ui_DatasetBuilder(object):
    def setupUi(self, DatasetBuilder):
        DatasetBuilder.setObjectName("DatasetBuilder")
        DatasetBuilder.resize(219, 467)
        self.centralwidget = QtWidgets.QWidget(DatasetBuilder)
        self.centralwidget.setObjectName("centralwidget")

        self.listImages = QtWidgets.QListWidget(self.centralwidget)
        self.listImages.setGeometry(QtCore.QRect(10, 30, 201, 281))
        self.listImages.setObjectName("listImages")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 17))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")

        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(10, 320, 91, 41))
        self.btnAdd.setObjectName("btnAdd")

        self.btnDiscard = QtWidgets.QPushButton(self.centralwidget)
        self.btnDiscard.setGeometry(QtCore.QRect(120, 320, 91, 41))
        self.btnDiscard.setObjectName("btnDiscard")

        self.txtDataName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDataName.setGeometry(QtCore.QRect(100, 370, 111, 25))
        self.txtDataName.setObjectName("txtDataName")

        self.btnCut = QtWidgets.QPushButton(self.centralwidget)
        self.btnCut.setGeometry(QtCore.QRect(10, 400, 201, 41))
        self.btnCut.setObjectName("btnCut")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 370, 91, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DatasetBuilder)
        QtCore.QMetaObject.connectSlotsByName(DatasetBuilder)

        #Click Events
        self.btnCut.clicked.connect(self.btnCutClicked)
        self.btnAdd.clicked.connect(self.btnAddClicked)
        self.btnDiscard.clicked.connect(self.btnDiscardClicked)

    def retranslateUi(self, DatasetBuilder):
        _translate = QtCore.QCoreApplication.translate
        DatasetBuilder.setWindowTitle(_translate("DatasetBuilder", "Dataset Builder"))
        self.label.setText(_translate("DatasetBuilder", "Image List"))
        self.btnAdd.setText(_translate("DatasetBuilder", "Add"))
        self.btnDiscard.setText(_translate("DatasetBuilder", "Discard"))
        self.btnCut.setText(_translate("DatasetBuilder", "Cut"))
        self.label_2.setText(_translate("DatasetBuilder", "Data Name : "))

    def btnAddClicked(self):
        fileChooser = QWidget()
        fileChooser.setGeometry(10,10,640,480)
        fileChooser.setWindowTitle('Choose a Image File')


        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileNames, _ = QFileDialog.getOpenFileNames(fileChooser,"Choose a Image File", "","Image Files (*.png)", options=options)
        fileChooser.show()

        for fileName in fileNames:
            self.listImages.addItem(fileName)

    def btnDiscardClicked(self):
        listModel = self.listImages.model()

        index_num = self.listImages.indexFromItem(self.listImages.selectedItems()[0])
        listModel.removeRow(index_num.row())


    def btnCutClicked(self):
        dataName = self.txtDataName.text()

        for item in xrange(self.listImages.count()):
            cutter = ImageCutter(self.listImages.item(item).text())
            cutter.cutImage(dataName)

        self.listImages.clear()
        self.txtDataName.clear()

        

        


        