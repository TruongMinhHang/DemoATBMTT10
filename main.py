from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from BitVector import *
from aes_encrypt_function import *
from aes_decrypt_function import *
import sys
import random
import string
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Tạo các biến
        self.Y = ''
        self.X = ''
        self.K = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 650)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 120, 151, 70))
        self.label.setMaximumSize(QtCore.QSize(163, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, -10, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 60, 291, 191))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 360, 291, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 400, 151, 70))
        self.label_3.setMaximumSize(QtCore.QSize(163, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(530, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")       
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 280, 121, 61))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 140, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 390, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 480, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(850, -10, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(640, 130, 151, 70))
        self.label_5.setMaximumSize(QtCore.QSize(163, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(740, 60, 291, 191))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1260, 120, 151, 70))
        self.label_6.setMaximumSize(QtCore.QSize(163, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(640, 410, 151, 70))
        self.label_7.setMaximumSize(QtCore.QSize(163, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(740, 360, 291, 191))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(830, 280, 121, 61))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1060, 140, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1070, 450, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Event
        self.pushButton.clicked.connect(self.encrypt)
        self.pushButton_3.clicked.connect(self.send)
        self.btnClear.clicked.connect(self.clear)      
        self.pushButton_5.clicked.connect(self.decrypt)
        self.pushButton_2.clicked.connect(self.openFileEncrypt)
        self.pushButton_4.clicked.connect(self.saveFileEncrypt)
        self.pushButton_6.clicked.connect(self.openFileDecrypt)
        self.pushButton_7.clicked.connect(self.saveFileDecrypt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bản rõ:"))
        self.label_2.setText(_translate("MainWindow", "MÃ HÓA"))
        self.label_3.setText(_translate("MainWindow", "Bản mã:"))
        self.pushButton.setText(_translate("MainWindow", "Mã hóa"))
        self.pushButton_2.setText(_translate("MainWindow", "File"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Chuyển"))
        self.pushButton_4.setText(_translate("MainWindow", "Lưu"))
        self.label_4.setText(_translate("MainWindow", "GIẢI MÃ"))
        self.label_5.setText(_translate("MainWindow", "Bản mã:"))
        self.label_6.setText(_translate("MainWindow", "Bản rõ:"))
        self.label_7.setText(_translate("MainWindow", "Bản rõ:"))
        self.pushButton_5.setText(_translate("MainWindow", "Giải mã"))
        self.pushButton_6.setText(_translate("MainWindow", "File"))
        self.pushButton_7.setText(_translate("MainWindow", "Lưu"))

    def generate_key(self):
        self.characters = string.ascii_letters + string.digits
        self.random_key = ''.join(random.choice(self.characters.lower()) for i in range(16))
        return self.random_key

    def openFileEncrypt(self):
        linkFile = App().initUIOpen()
        if not linkFile == '':
            f = open(linkFile,"r",encoding="utf-8")
            self.textEdit.setText(f.read())
            f.close()
    
    def saveFileEncrypt(self):
        linkFile = App().initUISave()
        if not linkFile == '':
            f = open(linkFile,"w", encoding='utf-8')
            f.write(self.textEdit_2.toPlainText())
            f.close()

    def openFileDecrypt(self):
        linkFile = App().initUIOpen()
        if not linkFile == '':
            f = open(linkFile,'r',encoding="utf-8")
            self.textEdit_3.setText(f.read())
            f.close()

    def saveFileDecrypt(self):
        linkFile = App().initUISave()
        if not linkFile == '':
            f = open(linkFile,"w",encoding="utf-8")
            f.write(self.textEdit_4.toPlainText())
            f.close()
    
    def send(self):
        self.textEdit_3.setText(self.Y)

    def encrypt(self):
        self.key = self.generate_key()
        self.K = self.key
        message = self.textEdit.toPlainText()
        message=BitVector(textstring=message)
        message=message.get_bitvector_in_hex()
        replacementptr=0
        while(replacementptr<len(message)):
            if(message[replacementptr:replacementptr+2]=='0a'):
                message=message[0:replacementptr]+'0d'+message[replacementptr:len(message)]
                replacementptr=replacementptr+4
            else:
                replacementptr=replacementptr+2

        message=BitVector(hexstring=message)
        message=message.get_bitvector_in_ascii()

        start=0
        end=0
        length=len(message)
        loopmsg=0.00
        loopmsg=math.ceil(length/16)+1
        outputhex=""
        #need to setup roundkeys here

        self.key=BitVector(textstring=self.key)
        roundkey1=findroundkey(self.key.get_bitvector_in_hex(),1)
        roundkey2=findroundkey(roundkey1,2)
        roundkey3=findroundkey(roundkey2,3)
        roundkey4=findroundkey(roundkey3,4)
        roundkey5=findroundkey(roundkey4,5)
        roundkey6=findroundkey(roundkey5,6)
        roundkey7=findroundkey(roundkey6,7)
        roundkey8=findroundkey(roundkey7,8)
        roundkey9=findroundkey(roundkey8,9)
        roundkey10=findroundkey(roundkey9,10)
        roundkeys=[roundkey1,roundkey2,roundkey3,roundkey4,roundkey5,roundkey6,roundkey7,roundkey8,roundkey9,roundkey10]

        for y in range(1, loopmsg): 
            if(end+16<length): 
                plaintextseg = message[start:end + 16]
            else: 
                plaintextseg = message[start:length]
                for z in range(0,((end+16)-length),1): 
                    plaintextseg = plaintextseg+"\00"

            #add round self.key zero/ find round self.key one
            bv1 = BitVector(textstring=plaintextseg)
            bv2 = self.key
            resultbv=bv1^bv2
            myhexstring = resultbv.get_bitvector_in_hex()

            for x in range(1, 10): 
                # sub byte
                myhexstring = resultbv.get_bitvector_in_hex()
                temp1=subbyte(myhexstring)

                # shift rows
                temp2=shiftrow(temp1)

                # mix column
                bv3 = BitVector(hexstring=temp2)
                newbvashex=mixcolumn(bv3)
                newbv=BitVector(hexstring=newbvashex)

                #add roundkey for current round
                bv1 = BitVector(bitlist=newbv)
                bv2 = BitVector(hexstring=roundkeys[x-1])
                resultbv = bv1 ^ bv2
                myhexresult = resultbv.get_bitvector_in_hex()

            #start round 10
            # sub byte round 10
            myhexstring = resultbv.get_bitvector_in_hex()
            temp1=subbyte(myhexstring)

            # shift rows round 10
            temp2=shiftrow(temp1)

            # add round self.key round 10
            newbv = BitVector(hexstring=temp2)
            bv1 = BitVector(bitlist=newbv)
            bv2 = BitVector(hexstring=roundkeys[9])
            resultbv = bv1 ^ bv2
            myhexstring = resultbv.get_bitvector_in_hex()

            #set encrypted hex segement of message to output string
            outputhextemp = resultbv.get_hex_string_from_bitvector()
            start = start + 16 #increment start pointer
            end = end + 16 #increment end pointer
            self.Y = outputhextemp
        self.textEdit_2.setText(self.Y)

    def decrypt(self):
        message_two = self.textEdit_3.toPlainText()
        self.key = self.K
        start=0
        end=32
        length=len(message_two)
        loopmsg=0.00
        loopmsg=math.ceil(length/32)+1
        outputhex=""
        asciioutput=""

        #need to setup roundkeys here
        self.key=BitVector(textstring=self.key)
        roundkey1=findroundkey(self.key.get_bitvector_in_hex(),1)
        roundkey2=findroundkey(roundkey1,2)
        roundkey3=findroundkey(roundkey2,3)
        roundkey4=findroundkey(roundkey3,4)
        roundkey5=findroundkey(roundkey4,5)
        roundkey6=findroundkey(roundkey5,6)
        roundkey7=findroundkey(roundkey6,7)
        roundkey8=findroundkey(roundkey7,8)
        roundkey9=findroundkey(roundkey8,9)
        roundkey10=findroundkey(roundkey9,10)
        roundkeys=[roundkey1,roundkey2,roundkey3,roundkey4,roundkey5,roundkey6,roundkey7,roundkey8,roundkey9,roundkey10]


        # set up the segement message_two loop parameters
        for y in range(1, loopmsg): # loop to encrypt all segments of the message_two
            plaintextseg = message_two[start:end]

            # add round key
            bv1 = BitVector(hexstring=plaintextseg)
            bv2 = BitVector(hexstring=roundkeys[9])
            resultbv = bv1 ^ bv2
            myhexstring = resultbv.get_bitvector_in_hex()

            #inverse shift row
            myhexstring=invshiftrow(myhexstring)

            #inverse subbyte
            myhexstring=invsubbyte(myhexstring)

            for x in range(8, -1, -1):
                # add roundkey for current round
                bv1 = BitVector(hexstring=myhexstring)
                bv2 = BitVector(hexstring=roundkeys[x])
                resultbv = bv1 ^ bv2
                myhexstring = resultbv.get_bitvector_in_hex()

                # mix column
                bv3 = BitVector(hexstring=myhexstring)
                myhexstring=invmixcolumn(bv3)

                # shift rows
                myhexstring = invshiftrow(myhexstring)

                # sub byte
                myhexstring = invsubbyte(myhexstring)

            #add initial round key
            bv1 = BitVector(hexstring=myhexstring)
            bv2 = self.key
            resultbv = bv1 ^ bv2
            myhexstring = resultbv.get_bitvector_in_hex()

            start = start + 32 #increment start pointer
            end = end + 32 #increment end pointer

            replacementptr = 0
            while (replacementptr < len(myhexstring)):
                if (myhexstring[replacementptr:replacementptr + 2] == '0d'):
                    myhexstring = myhexstring[0:replacementptr] + myhexstring[replacementptr+2:len(myhexstring)]
                else:
                    replacementptr = replacementptr + 2

            outputhex = BitVector(hexstring=myhexstring)
            asciioutput = outputhex.get_bitvector_in_ascii()
            asciioutput = asciioutput.replace('\x00','')
        self.X = asciioutput
        self.textEdit_4.setText(self.X)

    def clear(self):
        self.textEdit.setText('')
        self.textEdit_2.setText('')
        self.textEdit_3.setText('')
        self.textEdit_4.setText('')

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'App'

    def initUIOpen(self):
        self.setWindowTitle(self.title)
        filename = self.openFileNameDialog()
        return filename
    
    def initUISave(self):
        self.setWindowTitle(self.title)
        filename = self.saveFileDialog()
        return filename
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"OpenFile", "","All Files (*);;Text Files (*.txt)", options=options)
        return fileName
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        return fileName      
          
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
