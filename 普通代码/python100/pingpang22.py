# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，
# 乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
# n1=['a','b','c']
# n2=['x','y','z']
'''
没做完的思路
for i in range(0,len(n1)):
    for j in range(0,len(n2)):

        if i!=j:
            if i=='c':
                j !='x' and j !='z'

        'c'!='x' and 'x'!='z'
'''
a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
c-=set(('x','z'))
a-=set('x')
for i in a:
    for j in b:
        for k in c:
            if len(set((i,j,k)))==3:
                print('a:%s,b:%s,c:%s'%(i,j,k))

