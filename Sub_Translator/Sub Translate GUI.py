# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
from googletrans import Translator  
import pysrt


class Ui_Trans(object):

    def setupUi(self, Trans):
        Trans.setObjectName("Trans")
        Trans.resize(408, 295)
        self.pushButton = QtWidgets.QPushButton(Trans)
        self.pushButton.setGeometry(QtCore.QRect(160, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.accept)

        self.pushButton_2 = QtWidgets.QPushButton(Trans)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 240, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.save)
        
        self.label = QtWidgets.QLabel(Trans)
        self.label.setGeometry(QtCore.QRect(10, 160, 101, 20))
        self.label.setObjectName("label")

        self.progressBar = QtWidgets.QProgressBar(Trans)
        self.progressBar.setGeometry(QtCore.QRect(10, 190, 151, 23))
        self.progressBar.setObjectName("progressBar")

        self.label_2 = QtWidgets.QLabel(Trans)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.label_2.setObjectName("label_2")

        self.pushButton_3 = QtWidgets.QPushButton(Trans)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 190, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.translate)
        
        self.pushButton_4 = QtWidgets.QPushButton(Trans)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 240, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.close_application)

        self.lineEdit = QtWidgets.QLineEdit(Trans)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 131, 21))
        self.lineEdit.setDisabled(True)

        self.comboBox = QtWidgets.QComboBox(Trans)
        self.comboBox.setGeometry(QtCore.QRect(120, 100, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[str].connect(self.outlang)

        self.label_3 = QtWidgets.QLabel(Trans)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Trans)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Trans)
        self.label_5.setGeometry(QtCore.QRect(120, 130, 121, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Trans)
        QtCore.QMetaObject.connectSlotsByName(Trans)

    def retranslateUi(self, Trans):
        _translate = QtCore.QCoreApplication.translate
        Trans.setWindowTitle(_translate("Trans", "Translator"))
        self.pushButton.setText(_translate("Trans", "Choose File"))
        self.pushButton_2.setText(_translate("Trans", "Save File"))
        self.label.setText(_translate("Trans", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Translating:</span></p></body></html>"))
        self.label_2.setText(_translate("Trans", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Subtitles Translator:</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Trans", "Translate"))
        self.pushButton_4.setText(_translate("Trans", "Close"))
        self.comboBox.setItemText(0, _translate("Trans", "English"))
        self.comboBox.setItemText(1, _translate("Trans", "Japanese"))
        self.comboBox.setItemText(2, _translate("Trans", "Korean"))
        self.label_3.setText(_translate("Trans", "Output Language:"))
        self.label_4.setText(_translate("Trans", "Detected Language:"))
        self.label_5.setText(_translate("Trans", "..."))
    
    
    def accept(self):
        global translator
        global full
        global full_trans
        global OutputLang
        global InputLang
        global a
        global subs
        global Filename
        global fname
        dlg=QtWidgets.QFileDialog()
        fname = dlg.getOpenFileName(None,'Open file',"","All Files (*);;Subtitle Files (*.srt)")
        fname=fname[0]
        fname,Filename=os.path.split(os.path.abspath(fname))
        print(fname)
        print(Filename)
        self.lineEdit.setText(Filename)
        OutputLang=''
        translator = Translator()
        full=str()
        full_trans=str()
        InputLang="English"
        a=50
        subs = pysrt.open(fname+'\\'+Filename)
        InputLang=translator.detect(subs[0].text).lang
        self.label_5.setText(InputLang)
        InputLang=self.lang(InputLang)
    
    def outlang(self,text):
        global OutputLang
        OutputLang=self.lang(text)
        #self.label_3.setText(OutputLang)

    def lang(self,text):
        if text=="English":
            text="en"
        elif text=="Japanese":
            text="ja"
        elif text=="Korean":
            text="ko"
        return(text)

    def translate(self):
        global translator
        global full
        global full_trans
        global OutputLang
        global InputLang
        global a
        global subs
        global Filename 
        self.safety()
        #Translating...
        print("Started Translating:")

        for k in range(0,a):
            for i in range((k*len(subs))//a,((k+1)*len(subs))//a):
                full=full+subs[i].text+"\n\n"
            full_trans+="\n\n"+translator.translate(full,dest=OutputLang,src=InputLang).text
            full=""
            self.progressBar.setValue(((k+1)*100)//a)
            print(k+1,"/",a,"parts Done")
        full=full_trans.split('\n\n')

        full.pop(0)

        for i in range(len(subs)):
            subs[i].text=full[i]

    def save(self):
        global OutputLang
        global subs
        global Filename
        global fname
        self.safety()
        print("saving...")
        Filename=os.path.splitext(Filename)[0]
        subs.save(fname+'\\'+Filename+"-"+OutputLang+".srt", encoding='utf-8')
        self.progressBar.setValue(0)
        print("Done...")

    def close_application(self):
        sys.exit()

    def safety(self):
        global OutputLang
        if OutputLang=='':
            OutputLang="English"
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Trans = QtWidgets.QDialog()
    ui = Ui_Trans()
    ui.setupUi(Trans)
    Trans.show()
    sys.exit(app.exec_())
