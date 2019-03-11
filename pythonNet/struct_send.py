#struct_send.py
from socket import *
import struct

address = ('127.0.0.1',8888)
s = socket(AF_INET,SOCK_DGRAM)

while True :
    id = int(input("ID:"))
    name = input("name:")
    height = float(input("Height:"))
    lname = len(name)

    fmt = 'i16sf'
    data = struct.pack(fmt,id,name.encode(),height)
    s.sendto(data,address)

s.close()
