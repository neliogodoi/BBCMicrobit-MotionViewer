# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MotionViewer_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MotionView(object):
    def setupUi(self, MotionView):
        MotionView.setObjectName("MotionView")
        MotionView.resize(551, 542)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../../g845.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MotionView.setWindowIcon(icon)
        MotionView.setStyleSheet("QDialog{\n"
"    background: linear-gradient( rgb(37, 106, 255), rgb(101, 255, 90));\n"
"}")
        self.btnAtualizar = QtWidgets.QPushButton(MotionView)
        self.btnAtualizar.setGeometry(QtCore.QRect(20, 40, 41, 41))
        self.btnAtualizar.setBaseSize(QtCore.QSize(0, 30))
        self.btnAtualizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAtualizar.setIcon(icon1)
        self.btnAtualizar.setIconSize(QtCore.QSize(30, 30))
        self.btnAtualizar.setObjectName("btnAtualizar")
        self.btnDefinir = QtWidgets.QPushButton(MotionView)
        self.btnDefinir.setGeometry(QtCore.QRect(420, 40, 111, 41))
        self.btnDefinir.setObjectName("btnDefinir")
        self.comboBox = QtWidgets.QComboBox(MotionView)
        self.comboBox.setGeometry(QtCore.QRect(60, 40, 351, 41))
        self.comboBox.setBaseSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(MotionView)
        self.label_2.setGeometry(QtCore.QRect(20, 16, 141, 21))
        self.label_2.setObjectName("label_2")
        self.txtFilePath = QtWidgets.QLineEdit(MotionView)
        self.txtFilePath.setGeometry(QtCore.QRect(20, 120, 481, 31))
        self.txtFilePath.setObjectName("txtFilePath")
        self.label_3 = QtWidgets.QLabel(MotionView)
        self.label_3.setGeometry(QtCore.QRect(20, 96, 211, 21))
        self.label_3.setObjectName("label_3")
        self.btnGravarDados = QtWidgets.QPushButton(MotionView)
        self.btnGravarDados.setGeometry(QtCore.QRect(20, 170, 391, 41))
        self.btnGravarDados.setObjectName("btnGravarDados")
        self.label_5 = QtWidgets.QLabel(MotionView)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 131, 17))
        self.label_5.setObjectName("label_5")
        self.btnAnalisar = QtWidgets.QPushButton(MotionView)
        self.btnAnalisar.setGeometry(QtCore.QRect(20, 480, 511, 41))
        self.btnAnalisar.setObjectName("btnAnalisar")
        self.btnParar = QtWidgets.QPushButton(MotionView)
        self.btnParar.setGeometry(QtCore.QRect(420, 170, 111, 41))
        self.btnParar.setObjectName("btnParar")
        self.btnDiretorios = QtWidgets.QPushButton(MotionView)
        self.btnDiretorios.setGeometry(QtCore.QRect(500, 120, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDiretorios.setFont(font)
        self.btnDiretorios.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDiretorios.setIcon(icon2)
        self.btnDiretorios.setIconSize(QtCore.QSize(25, 25))
        self.btnDiretorios.setObjectName("btnDiretorios")
        self.scrollArea = QtWidgets.QScrollArea(MotionView)
        self.scrollArea.setGeometry(QtCore.QRect(19, 250, 511, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listView = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.listView.setGeometry(QtCore.QRect(0, 0, 511, 211))
        self.listView.setObjectName("listView")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(MotionView)
        QtCore.QMetaObject.connectSlotsByName(MotionView)

    def retranslateUi(self, MotionView):
        _translate = QtCore.QCoreApplication.translate
        MotionView.setWindowTitle(_translate("MotionView", "Motion Viewer BBC"))
        self.btnDefinir.setText(_translate("MotionView", "Definir"))
        self.comboBox.setItemText(0, _translate("MotionView", "Nenhum dispositivo selecionado"))
        self.label_2.setText(_translate("MotionView", "Dispositivos conectados:"))
        self.txtFilePath.setText(_translate("MotionView", "/tmp/motionviewer_data.csv"))
        self.label_3.setText(_translate("MotionView", "Localização do arquivo de dados:"))
        self.btnGravarDados.setText(_translate("MotionView", "Gravar dados no arquivo"))
        self.label_5.setText(_translate("MotionView", "Prévia dos dados:"))
        self.btnAnalisar.setText(_translate("MotionView", "Analizar  dados"))
        self.btnParar.setText(_translate("MotionView", "Parar"))

