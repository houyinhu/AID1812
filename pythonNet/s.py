
from select import select
from socket import *
from sys import stdin



rlist = [stdin]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for i in rs:
        if i is stdin:
            name = stdin.readline()
            print(name)
            print(type(i))
            print(type(stdin))
        else:
            print("asd")
    for w in ws:
        pass
    for x in xs:
        pass

