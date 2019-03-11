

#此示例示意标准输出文件的用法
import sys
sys.stdout.write("hello world \n")

sys.stdout.close()

print("hello world!!!")

f = open("myprint.txt",'w')
print(1,2,3,4,file=f)   #写入内容到文件myprint.txt中
print("hello world!!!!!!",file=f)


s=sys.stdin.readline()

# s= sys.stdin.read()
