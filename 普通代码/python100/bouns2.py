'''
题目 企业发放的奖金根据利润提成。利润(i)低于或等于10万元时
，奖金可提10%；利润高于10万元，低于20万元时，低于10万元
的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万
之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润i，求应发放奖金总数？
'''

i=int(input('请输入当月利润:'))
bouns=0
if i <=10:
    bouns=0.1*i
elif 10<= i <=20:
    bouns =1+0.075*(i-10)
elif 20<= i<=40:
    bouns=1+0.75+0.05*(i-20)
elif 40<=i<=60:
    bouns=2.75+0.03*(i-40)
elif 60<= i<=100:
    bouns=3.35+0.015*(i-60)
else:
    bouns=3.95+0.1*(i-100)
print("应发奖金：",bouns)
# profit=int(input('Show me the money: '))
# bonus=0
# thresholds=[100000,100000,200000,200000,400000]
# rates=[0.1,0.075,0.05,0.03,0.015,0.01]
# for i in range(len(thresholds)):
#     if profit<=thresholds[i]:
#         bonus+=profit*rates[i]
#         profit=0
#         break
#     else:
#         bonus+=thresholds[i]*rates[i]
#         profit-=thresholds[i]
# bonus+=profit*rates[-1]
# print(bonus)
