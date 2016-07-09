import socket

class ClientPi():
	def __init__(self, ip,port):
		self.sock = ip
		self.addr = port
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#sends a query(sensor id) to another pi
	def make_query(self,query):
		self.serversocket.sendto(query,(self.sock,self.addr))
		data, server = self.serversocket.recvfrom(32)
		return data


if __name__ == "__main__":

	#two threads to deal with cosmos request and raspberry pi requests
	#server_cosmos = GeneralServer('10.0.102.104',8080,"cosmos")
	#client = ClientPi('10.0.102.104',8081)
	client = ClientPi('127.0.0.1',8081)
	query = b'1' 
	print("Sending %s" % query)
	print(client.make_query(query))



