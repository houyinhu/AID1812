#process_01.py
from multiprocessing import Process
from time import sleep
f = open('process.txt','rt')
f1 = f.read()
lenf = int(len(f1)/2)
print()

def f1():
    sleep(1)
    f.seek(0.0)
    line1 = f.read(lenf)
    f1 = open('text1.txt','wt')
    f1.write(line1)
    f1.close()

def f2():
    f2 = open('text2.txt','wt')
    f.seek(lenf,0)
    line2 = f.read()
    f2.write(line2)
    f2.close()

f2()
p = Process(target=f1)
p.start()
p.join()


