

#��ʾ��ʾ���׼����ļ����÷�
import sys
sys.stdout.write("hello world \n")

sys.stdout.close()

print("hello world!!!")

f = open("myprint.txt",'w')
print(1,2,3,4,file=f)   #д�����ݵ��ļ�myprint.txt��
print("hello world!!!!!!",file=f)


s=sys.stdin.readline()

# s= sys.stdin.read()
