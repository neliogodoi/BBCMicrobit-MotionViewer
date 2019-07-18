import matplotlib.pyplot as plt


class GraphDataBBC():

	def __init__(self, file="motionviewer_data.csv"):
		self.file = file
		self.fig1 = plt.figure()
		self.axl = self.fig1.add_subplot(1, 1, 1)
		self.bbc = None
		self.sequence = 0
		self.to_save = False
		self.x = []
		self.y = []
		self.z = []
		self.t = []

	def set_file_data(self, file):
		self.file = file

	def get_data_in_file(self):
		try:
			print(self.file)
			arquivo = open(self.file, 'r')
			for line in arquivo:
				data = line.split(',')
				self.t.append(int(data[3])/1000)
				self.x.append(int(data[0]))
				self.y.append(int(data[1]))
				self.z.append(int(data[2]))
		except:
			print("Except: file not found!")


	def plot(self):
		self.get_data_in_file()
		self.axl.plot(self.t, self.x, 'b', self.t, self.y, 'r', self.t, self.z, 'y')
		plt.show()