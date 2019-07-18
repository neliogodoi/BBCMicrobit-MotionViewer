
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MotionViewerBBC(object):
    def setupUi(self, MotionViewerBBC):
        MotionViewerBBC.setObjectName("MotionViewerBBC")
        MotionViewerBBC.resize(400, 272)
        MotionViewerBBC.setStyleSheet("QDialog{\n"
"    background-color: rgb(245, 245, 245);\n"
"}")
        self.textData = QtWidgets.QTextEdit(MotionViewerBBC)
        self.textData.setEnabled(False)
        self.textData.setGeometry(QtCore.QRect(20, 50, 361, 121))
        self.textData.setStyleSheet("QTextEdit{\n"
"    background: rgb(255,255,255);\n"
"    border: 1px solid rgb(250,250,250);\n"
"}")
        self.textData.setObjectName("textData")
        self.btnCriar = QtWidgets.QPushButton(MotionViewerBBC)
        self.btnCriar.setGeometry(QtCore.QRect(20, 180, 171, 31))
        self.btnCriar.setStyleSheet("QPushButton{\n"
"    background: rgb(194, 194, 194);\n"
"    border:none;\n"
"    color: black;\n"
"}")
        self.btnCriar.setObjectName("btnCriar")
        self.btnAnalisar = QtWidgets.QPushButton(MotionViewerBBC)
        self.btnAnalisar.setGeometry(QtCore.QRect(210, 180, 171, 31))
        self.btnAnalisar.setStyleSheet("QPushButton{\n"
"    background: rgb(194, 194, 194);\n"
"    border:none;\n"
"    color: black;\n"
"}")
        self.btnAnalisar.setObjectName("btnAnalisar")
        self.btnParar = QtWidgets.QPushButton(MotionViewerBBC)
        self.btnParar.setGeometry(QtCore.QRect(300, 220, 79, 31))
        self.btnParar.setStyleSheet("QPushButton{\n"
"    background: rgb(194, 194, 194);\n"
"    border:none;\n"
"    color: black;\n"
"}")
        self.btnParar.setObjectName("btnParar")
        self.comboBox = QtWidgets.QComboBox(MotionViewerBBC)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 361, 22))
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background: rgb(255, 255, 255);\n"
"    border: none;\n"
"}")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(MotionViewerBBC)
        QtCore.QMetaObject.connectSlotsByName(MotionViewerBBC)

    def retranslateUi(self, MotionViewerBBC):
        _translate = QtCore.QCoreApplication.translate
        MotionViewerBBC.setWindowTitle(_translate("MotionViewerBBC", "Motion Viewer BBC"))
        self.btnCriar.setText(_translate("MotionViewerBBC", "Criar arquivo de dados"))
        self.btnAnalisar.setText(_translate("MotionViewerBBC", "Analizar  dados"))
        self.btnParar.setText(_translate("MotionViewerBBC", "Parar"))

