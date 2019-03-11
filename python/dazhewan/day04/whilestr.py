w1=ord('a')
w2=ord('z')
w3=ord('A')
w4=ord('Z')
while w1<=w2:
    print(chr(w1),end='')
    w1+=1
print()
w5=ord('a')
w6=ord('z')
while w3<=w4:
    print(chr(w3),end='')
    if w5<=w6:
        print(chr(w5),end='')
    w5+=1
    w3+=1
print()