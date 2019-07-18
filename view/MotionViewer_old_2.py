# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MotionViewer.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MotionView(object):
    def setupUi(self, MotionView):
        MotionView.setObjectName("MotionView")
        MotionView.resize(400, 425)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../g845.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MotionView.setWindowIcon(icon)
        self.textData = QtWidgets.QTextEdit(MotionView)
        self.textData.setEnabled(False)
        self.textData.setGeometry(QtCore.QRect(20, 170, 361, 121))
        self.textData.setObjectName("textData")
        self.btnCriar = QtWidgets.QPushButton(MotionView)
        self.btnCriar.setGeometry(QtCore.QRect(20, 310, 171, 41))
        self.btnCriar.setObjectName("btnCriar")
        self.btnAnalisar = QtWidgets.QPushButton(MotionView)
        self.btnAnalisar.setGeometry(QtCore.QRect(210, 310, 171, 41))
        self.btnAnalisar.setObjectName("btnAnalisar")
        self.btnParar = QtWidgets.QPushButton(MotionView)
        self.btnParar.setGeometry(QtCore.QRect(20, 360, 171, 41))
        self.btnParar.setObjectName("btnParar")
        self.comboBox = QtWidgets.QComboBox(MotionView)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 271, 31))
        self.comboBox.setBaseSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(MotionView)
        self.pushButton.setGeometry(QtCore.QRect(300, 30, 81, 31))
        self.pushButton.setBaseSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.txtArquivoCSV = QtWidgets.QLineEdit(MotionView)
        self.txtArquivoCSV.setGeometry(QtCore.QRect(20, 100, 271, 31))
        self.txtArquivoCSV.setObjectName("txtArquivoCSV")
        self.btnBuscarArquivoCSV = QtWidgets.QPushButton(MotionView)
        self.btnBuscarArquivoCSV.setGeometry(QtCore.QRect(300, 100, 81, 31))
        self.btnBuscarArquivoCSV.setObjectName("btnBuscarArquivoCSV")
        self.label = QtWidgets.QLabel(MotionView)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MotionView)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MotionView)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MotionView)
        QtCore.QMetaObject.connectSlotsByName(MotionView)

    def retranslateUi(self, MotionView):
        _translate = QtCore.QCoreApplication.translate
        MotionView.setWindowTitle(_translate("MotionView", "Motion Viewer BBC"))
        self.btnCriar.setText(_translate("MotionView", "Criar arquivo de dados"))
        self.btnAnalisar.setText(_translate("MotionView", "Analizar  dados"))
        self.btnParar.setText(_translate("MotionView", "Parar"))
        self.comboBox.setItemText(0, _translate("MotionView", "Nenhum dispositivo localizado!"))
        self.pushButton.setText(_translate("MotionView", "Atualizar"))
        self.txtArquivoCSV.setText(_translate("MotionView", "motionviewer_data.csv"))
        self.btnBuscarArquivoCSV.setText(_translate("MotionView", "Buscar"))
        self.label.setText(_translate("MotionView", "Dispositivo:"))
        self.label_2.setText(_translate("MotionView", "Arquivo de dados:"))
        self.label_3.setText(_translate("MotionView", "Previa dos dados:"))
