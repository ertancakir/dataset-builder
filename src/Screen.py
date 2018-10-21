from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QListWidget

from ImageCutter import ImageCutter

class Ui_DatasetBuilder(object):
    def setupUi(self, DatasetBuilder):
        DatasetBuilder.setObjectName("DatasetBuilder")
        DatasetBuilder.resize(721, 196)

        self.centralwidget = QtWidgets.QWidget(DatasetBuilder)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 261, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.txtPath = QtWidgets.QLineEdit(self.frame)
        self.txtPath.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.txtPath.setReadOnly(True)
        self.txtPath.setObjectName("txtPath")

        self.btnChoose = QtWidgets.QPushButton(self.frame)
        self.btnChoose.setGeometry(QtCore.QRect(160, 10, 91, 31))
        self.btnChoose.setObjectName("btnChoose")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label.setObjectName("label")

        self.txtDataName = QtWidgets.QLineEdit(self.frame)
        self.txtDataName.setGeometry(QtCore.QRect(100, 50, 151, 31))
        self.txtDataName.setObjectName("txtDataName")

        self.btnCut = QtWidgets.QPushButton(self.frame)
        self.btnCut.setEnabled(False)
        self.btnCut.setGeometry(QtCore.QRect(160, 120, 89, 25))
        self.btnCut.setObjectName("btnCut")

        self.btnClean = QtWidgets.QPushButton(self.frame)
        self.btnClean.setEnabled(False)
        self.btnClean.setGeometry(QtCore.QRect(70, 120, 89, 25))
        self.btnClean.setObjectName("btnClean")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(280, 10, 211, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 211, 151))
        self.groupBox.setObjectName("groupBox")

        self.listImages = QtWidgets.QListWidget(self.groupBox)
        self.listImages.setGeometry(QtCore.QRect(0, 20, 211, 131))
        self.listImages.setObjectName("listImages")

        self.imageView = QtWidgets.QLabel(self.centralwidget)
        self.imageView.setGeometry(QtCore.QRect(500, 10, 211, 151))
        self.imageView.setText("")
        self.imageView.setObjectName("imageView")

        self.retranslateUi(DatasetBuilder)
        QtCore.QMetaObject.connectSlotsByName(DatasetBuilder)

        #Click Events
        self.btnChoose.clicked.connect(self.btnChooseClicked)
        self.btnCut.clicked.connect(self.btnCutClicked)
        self.btnClean.clicked.connect(self.btnCleanClicked)

        #Text Change Events
        self.txtDataName.textChanged.connect(self.txtDataNameChanged)

        #ListWidget Get Selected
        self.listImages.itemSelectionChanged.connect(self.listImagesSelectionChanged)

    def retranslateUi(self, DatasetBuilder):
        _translate = QtCore.QCoreApplication.translate
        DatasetBuilder.setWindowTitle(_translate("DatasetBuilder", "DataSet Builder"))
        self.btnChoose.setText(_translate("DatasetBuilder", "Choose"))
        self.label.setText(_translate("DatasetBuilder", "Data Name : "))
        self.btnCut.setText(_translate("DatasetBuilder", "Cut"))
        self.btnClean.setText(_translate("DatasetBuilder", "Clean"))
        self.groupBox.setTitle(_translate("DatasetBuilder", "Image List"))


    def btnChooseClicked(self):
        fileChooser = QWidget()
        fileChooser.setGeometry(10,10,640,480)
        fileChooser.setWindowTitle('Choose a Image File')

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(fileChooser,"Choose a Image File", "","Image Files (*.png)", options=options)
        fileChooser.show()

        self.txtPath.setText(fileName)
        self.btnClean.setEnabled(True)
        

    def btnCutClicked(self):
        imgPath = self.txtPath.text()
        dataName = self.txtDataName.text()
        
        imgCutter = ImageCutter(imgPath)
        imageList = imgCutter.cutImage(dataName)

        for image in imageList:
            self.listImages.addItem(image)

    def btnCleanClicked(self):
        self.txtPath.setText("")
        self.txtDataName.setText("")
        self.btnClean.setEnabled(False)
        self.btnCut.setEnabled(False)
        self.listImages.clear()

    def txtDataNameChanged(self):
        self.btnCut.setEnabled(True)


    #Burada hata var clear butonuna basildiktan sonra ve list widget temizlendiginde program crash oluyor
    def listImagesSelectionChanged(self):
        if(self.listImages.count() is not 0):
            selectedImagePath = self.listImages.selectedItems()[0].text()
            image = QPixmap(selectedImagePath)
            self.imageView.setPixmap(image)
        
        