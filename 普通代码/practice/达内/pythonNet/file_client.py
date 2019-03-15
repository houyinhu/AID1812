from socket import *
import signal
import os,sys

def main():
    sockfd = socket()
    while True:
        sockfd.connect(('172.88.2.247',8888))
        sockfd.send(b'lai')
        data = sockfd.recv(1024)





