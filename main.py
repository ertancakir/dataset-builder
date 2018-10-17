import sys
from PyQt5.QtWidgets import QApplication, QDialog
from template import Ui_DatasetBuilder

def window():
    app = QApplication(sys.argv)
    screen = QDialog()
    ui = Ui_DatasetBuilder()
    ui.setupUi(screen)

    screen.show()   
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()