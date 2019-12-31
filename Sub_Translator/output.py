# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(408, 295)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(10, 100, 101, 20))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 130, 118, 23))
        self.progressBar.setProperty("value", 25)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 130, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 240, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.pushButton.setText(_translate("dialog", "Choose File"))
        self.pushButton_2.setText(_translate("dialog", "Save File"))
        self.label.setText(_translate("dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Translating:</span></p></body></html>"))
        self.label_2.setText(_translate("dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Subtitles Translator:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("dialog", "Translate"))
        self.pushButton_4.setText(_translate("dialog", "Close"))
        self.label_3.setText(_translate("dialog", "No File chosen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
