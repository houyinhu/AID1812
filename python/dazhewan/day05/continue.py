#continue.py
for x in range(5):
    if x==2:
        continue
    print(x)
print('--------')
y=0
while y<5:
    if y%2 != 0:
        y+=1
        continue
    print(y) 
    y+=1