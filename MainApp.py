import sys
import threading
from GraphController import GraphDataBBC
from SerialController import SerialController
from MotionViewer import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainApp(QMainWindow):

	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.ui = Ui_MotionView()
		self.ui.setupUi(self)
		self.bbc = SerialController()
		self.saving = False
		self.file_data = "motionviewer_data.csv"
		self.graph = GraphDataBBC(self.file_data)
		self.set_view()
		self.sequence = 0

	def set_view(self):
		self.set_port_on_view()
		self.ui.btnGravarDados.clicked.connect(self.save_csv_file)
		self.ui.btnParar.clicked.connect(self.stop_save_csv)
		self.ui.btnAtualizar.clicked.connect(self.set_port_on_view)
		self.ui.btnAnalisar.clicked.connect(self.graph.plot)
		self.ui.btnDiretorios.clicked.connect(self.get_file_path)
		self.ui.btnParar.setDisabled(False)
		self.ui.btnGravarDados.setDisabled(False)
		self.set_preview_data()

	def set_preview_data(self):
		try:
			arquivo = open(self.file_data, 'r')
			self.ui.listView.clear()
			for line in arquivo:
				self.ui.listView.append(line.replace('\n',''))
			self.ui.btnAnalisar.setDisabled(False)
		except:
			self.ui.btnAnalisar.setDisabled(True)
		self.saving = False

	def set_port_on_view(self):
		item = self.ui.comboBox.count()
		if item > 1:
			while item > 1:
				self.ui.comboBox.removeItem(item-1)
				item -= 1

		self.bbc.set_list_ports()
		list = self.bbc.get_list_ports()
		if len(list) > 0:
			for x in list:
				self.ui.comboBox.addItem(str(x))
			self.ui.comboBox.setCurrentIndex(1)
		else:
			self.ui.comboBox.setCurrentIndex(0)

	def get_file_path(self):
		file = QFileDialog.getOpenFileName(self, "Abrir arquivo de dados", "~/", "Arquivo de dados (*.csv)")
		self.file_data = file[0].replace(' ','\ ')
		self.ui.txtFilePath.setText(self.file_data)
		self.graph.set_file_data(self.file_data)
		self.set_preview_data()

	def define_port(self):
		index_port = self.ui.combobox.currentIndex()
		self.bbc.set_port(index_port)

	def stop_save_csv(self):
		self.saving = False
		self.ui.btnParar.setDisabled(True)
		self.ui.btnAnalisar.setDisabled(False)
		self.set_preview_data()

	def save_file(self):
		arquivo = open("motionviewer_data.csv", 'w')
		while self.saving:
			data = self.bbc.get_data()
			try:
				x,y,z,t = data.split(',')
				if int(t) > self.sequence:
					line = '{},{},{},{}'.format(x,y,z,t)
					arquivo.write(line)
					self.sequence = int(t)
			except:
				continue
		arquivo.close()

	def save_csv_file(self):
		self.saving = True
		self.ui.btnParar.setDisabled(False)
		self.ui.btnGravarDados.setDisabled(True)
		t = threading.Thread(target=self.save_file)
		t.start()


if __name__=="__main__":
	app = QApplication(sys.argv)
	w = MainApp()
	w.show()
	sys.exit(app.exec_())
