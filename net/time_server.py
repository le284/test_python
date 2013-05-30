#! /usr/bin/python
#coding:utf-8
from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print 'waiting for connection...'
	tcpCliSock, addr = tcpSerSock.accept()
	print '...connected from:', addr

	while True:
		data = tcpCliSock.recv(BUFSIZE)
		print [ctime()], ':', data
		if not data:
			break
		data = raw_input(">")
		if not data:
			break
		tcpCliSock.send('[%s] : %s' % (ctime(), data))
tcpCliSock.close()
tcpSerSock.close()
