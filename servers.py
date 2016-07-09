
import socket
from threading import *
import struct
from static_data import StaticData

class GeneralServer(Thread):
	def __init__(self, ip,port, source):
		Thread.__init__(self)
		self.source = source
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server_adress = (ip,port)
		self.serversocket.bind(server_adress)
		print("Serving to " +ip+ " and listening on: "+str(port))
		self.start()

	def run(self):
		while True:
			data, addr = self.serversocket.recvfrom(32)
			print("Received: %s"%str(data))
			if(self.source == "pi"):
				#returns the response
				resp = self.pi_request_process(data)
			if(self.source == "cosmos"):
				resp = self.cosmos_request_process(data)
			r = bytes(str(resp),'utf-8')
			self.serversocket.sendto(r,addr)

	def pi_request_process(self,resp):
		d = StaticData("","","","")
		answer = d.has_sensor(resp.decode('utf-8'))
		return answer

	def cosmos_request_process(self,resp):
		dataUnpacked = struct.unpack('>BBH',command) #unpacks two unsigned chars and one short
		print('Command Length: ',dataUnpacked[0])
		print('Command ID: ',dataUnpacked[1])
		print('Command Sensor_ID: ', dataUnpacked[2])
		#makes a query asking for the sensor_id
		d = StaticData("","","","")
		resp = d.has_sensor(dataUnpacked[2])
		package = make_tlm(resp)
		return package 

	#makes the telemetry packages
	def make_tlm(resp):
		return ""


if __name__ == "__main__":

	#two threads to deal with cosmos request and raspberry pi requests
	#server_cosmos = GeneralServer('10.0.102.104',8080,"cosmos")
	#server_pi = GeneralServer('10.0.102.104',8081,"pi")
	server_pi = GeneralServer('127.0.0.1',8081,"pi")




