#struct_send.py
from socket import *
import struct

s = socket(AF_INET,SOCK_DGRAM)
s.bind(("0.0.0.0",8888))

#确定数据结构
st = struct.Struct('i16sf')
while True:
    data,addres = s.recvfrom(1024)
    #解析数据
    data1 = st.unpack(data)
    print(data1)
