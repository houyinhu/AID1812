
Nos=[1001,1002,1005,1008]
names=['Tom','Jery','Spike','Tyke']
d=dict()
for x in range(0,len(Nos)):
    d[Nos[x]]=names[x]
print(d)
    
#推导式
d={Nos[i]:names[i] for i in range(0,len(Nos))}
print(d)

d={}
for n in Nos:
    d[n]=names[Nos.index(n)]
print(d)

d={n:names[Nos.index(n)] for n in Nos}
print(d)









