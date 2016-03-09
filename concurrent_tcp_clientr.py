import socket
import struct
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))

while True:
    value = int(255*random.random())
    sock.sendall(struct.pack('>H', value))
    print 'Sent', value,
    value = struct.unpack('>H', sock.recv(struct.calcsize('>H')))[0]
    print 'and_received', value
