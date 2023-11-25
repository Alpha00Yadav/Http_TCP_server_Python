import socket
class TCP:
	port=8080
	host="127.0.0.1"
	socketo=""
	ex=""
	def __init__(self,ip,port):
		self.host=ip
		self.port=port
		self.arambh()
		self.Connector()
	def arambh(self):
		self.socketo=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.socketo.bind((self.host,self.port))
		self.socketo.listen(7)
		print("Server Runing at ",self.host,self.port)
	def Connector(self):	
		ex,add=self.socketo.accept()
		print(add,"Connected")
		self.ex=ex
	def exchange(self,reply,byte=1024):
			self.ex.sendall(reply)
			request=self.ex.recv(byte)
			return request
	def exclose(self):
			self.ex.close()
	def close(self):
		self.socketo.close()
class HTTP(TCP):
	def __init__(self,ip,port):
		self.host=ip
		self.port=port
		self.arambh()
	def exchange(self,reply='',byte=1024):
		self.Connector()
		request=self.ex.recv(byte)
		self.ex.sendall(self.sender(reply))
		self.exclose()
		request=self.saprate(request.decode())
		return request
	def sender(self,rep):
		header=b"HTTP/1.1 200 OK\r\nServer: Crude Server\r\nContent-Type: text/html\r\n\r\n"
		reply=header+rep
		return reply
	def saprate(self,req):
		d={}
		x=req.split("\r\n")
		y=x[0].split(" ")
		z=y[1].split("?")
		d["method"]=y[0]
		d["path"]=z[0]
		d["query"]={}
		if(len(z)>1):
			z=z[1].split("&")
			for c in z:
				i=c.split("=")
				d["query"][i[0]]=i[1]
		if(y[0]=="POST"):
			z=x[-1].split("&")
			for c in z:
				i=c.split("=")
				d["query"][i[0]]=i[1]
		return d	
x=HTTP("127.0.0.1",8000)
while True:
	c=open("C:\\Users\\Aditya\\Pictures\\asp.png",'rb')
	reply=c.read()
	#reply=b'Socket.py'
	request=x.exchange(reply)
	print(request)
	x.exclose()
x.close()