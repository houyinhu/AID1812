# 2，模拟斗地主发牌，牌共54张
# 种类：
# 黑桃（'\u2660'）,梅花('\u2663'),方块('\u2665'),红桃('\u2666')
# 数字：
# A2-12JQK
# 王牌：大小王
# 三个人，没人发17张牌，底牌三张，
# 输入回车，打印第一人的17张牌
# 输入回车，打印第二人的17张牌
# 输入回车，打印第三人的17张牌
# 输入回车，打印3张底牌
'''
import random
pattern=['\u2660','\u2663','\u2665','\u2666']
number=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
wang=['大王','小王']
l=[]
for x in number:
    for y in pattern:
        l.append(x+y)
l.extend(wang)
while True:
    i=0
    l1=[]
    input("按回车请开始发牌")
    if len(l) == 3:
        print("底牌是：",l)
        break
    while i<17:
        pai = random.choice(l)
        l.remove(pai)
        l1.append(pai)
        i+=1
    print(l1)
'''
# random.shuffle(l)
# l1=l[0:17]
# l2=l[17:34]
# l3=l[34:51]
# l4=l[51:54]
# print(l1)
# print(l2)
# print(l3)
# print(l4)




poke = ['大王','小王']
kinds = ['\u2660','\u2663','\u2665','\u2666']
numbers = ['A']
numbers += [str(x) for x in range(2,11)]
numbers += list("JQK")

for k in kinds:
    for n in  numbers:
        poke.append(k + n)
# poke += [k +n for k in kinds for n in number]
print(poke)
assert  len(poke) == 54,'出错'
#打乱
poke2 = poke.copy()
import random
random.shuffle(poke2)
player1 = poke[:17]
player2 = poke[17:34]
player3 = poke[34:51]
base = poke2[51:]
input()
print("第一个人的17张牌：",player1)
input()
print("第二个人的17张牌：",player2)
input()
print("第三个人的17张牌：",player3)
input()
print("底牌是：",base)

