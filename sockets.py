import socket, select, string, sys
import threading
host = "127.0.0.1"
port = 1300
def worker(num):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(200000)
	s.bind(("127.0.0.{}".format(num), 0))
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print('Unable to connect')
	 
	print('Connected to remote host')
	
	s.send(b"\n")
	while 1:
		data = s.recv(4096)

threads = []
for i in range(1, 25):
	t = threading.Thread(target=worker, args=(i,))
	threads.append(t)
	t.start()
	 
	
	