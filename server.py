import socket
import pickle
import numpy as np
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

	logger = pd.read_csv("Log.csv")
	appending = pd.Series([row])

	S = logger.loc[len(logger)] = appending
	l = pd.concat([logger, S])
	l.to_csv('Log.csv')
	conn.send(data)
	print (row)
	print (logger)
	print (S)
	print (l)
conn.close()