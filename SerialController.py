import serial
import os


class SerialController():

	def __init__(self):
		self.ser = ''
		self.list_ports = []
		if os.uname()[0] == 'Linux':
			self.nameport = '/dev/ttyACM{}'
		else:
			self.nameport = 'COM{}'

	def set_list_ports(self):
		for i in range(10):
			try:
				port = self.nameport.format(i)
				ser = serial.Serial(port, 115200)  # open serial port
				contem = False
				for j in range(len(self.list_ports)):
					if port in self.list_ports:
						contem = True
				if not contem:
					self.list_ports.append(port)
				ser.close()
			except:
				print('porta {} não localizada'.format(port))
		if len(self.list_ports) > 0:
			self.ser = serial.Serial(self.list_ports[0], 115200)

	def get_list_ports(self):
		return self.list_ports

	def set_port(self, port):
		self.ser = serial.Serial(self.list_ports[port], 115200)

	def get_data(self):
		return self.ser.readline().decode('utf-8')

	def close(self):
		self.ser.close()


