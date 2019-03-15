# 题目 输入某年某月某日，判断这一天是这一年的第几天？
'''
是否是润年
1 3 5 7 8 10 12   /31
4 6 9 11  /30
2 / 29 or 28
'''
years=int(input("请输入年份"))
month=int(input("请输入月份"))
today=int(input("请输入天数"))
if years%400==0 or (years%4==0 and years%100!=0):
    print(years,"是润年")
month1=(1,3,5,7,8,10,12)
month2=(4,6,9,11)
day=0
count=1
for count in range(count,month+1):
    if count==month:
        day+=today
        continue
    elif count==2 and month!=2:
        if years%400==0 or (years%4==0 and years%100!=0):
            day+=28
            continue
        day+=29
        count+=1
    elif count in month1:
        day+=31
        count+=1
    elif count in month2:
        day+=30
        count+=1
print("%s年%s月%s日"%(years,month,today),"是这一年的第",day,'天')
    







