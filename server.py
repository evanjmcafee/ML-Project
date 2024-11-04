import socket
import pickle
import pandas as pd

HOST = "10.242.13.10"
PORT = 5005
while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()
	print('Connected by', addr)
	data = conn.recv(4096)
	row = pickle.loads(data)

	logger = open("Log.csv", "a")
	logger.write("\n"+str(row)[1:-1])
	logger.close()
	conn.send(data)




conn.close()