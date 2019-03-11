# from multiprocessing import Pool

# p = Pool()

# f = open('a2.txt','wt',encoding='utf8')

# f.write('aasf')
# f.close()

from multiprocessing import Process
import time

def myfn1(n):

    print("Hello,Mr Green.")

if __name__ == '__main__':
    p = Process(target=myfn1,args=(1,))

    p.start()
    p.join()
 
    
    print("I am Lucy.")
