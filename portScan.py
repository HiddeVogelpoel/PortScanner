from threading import Thread
import socket

host = raw_input('Host > ')
from_port = input('Start scan from port > ')
to_port = input('Finish scan to port (Has to be smaller than 25535) > ')   
counting_open = []
service_open = []
counting_close = []
threads = []

def scan(port):
	s = socket.socket()
	result = s.connect_ex((host,port))
	#print('working on port > '+(str(port)))      
	if result == 0:
		counting_open.append(port)
		if port <= 25535:
			#service_open.append(socket.getservbyport(port))
			try:
				service = socket.getservbyport(port)
			except:
				service = 'Not found'
			print('PORT ' + str(port) + '\n  -' + service)
		else:
			print('Port not recognized')
		#print((str(port))+' -> open') 
		s.close()
	else:
		counting_close.append(port)
		#print((str(port))+' -> close') 
		s.close()

for i in range(from_port, to_port+1):
	t = Thread(target=scan, args=(i,))
	threads.append(t)
	t.start()
	
[x.join() for x in threads]

#print(counting_open)
#print(service_open)