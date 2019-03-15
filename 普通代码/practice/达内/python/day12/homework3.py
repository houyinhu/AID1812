import time
# 3，编写一个闹钟程序，启动时设置定时时间，到时间后打印一句"时间到！"然后程序退出


def alarmclock():
    print("请在下面输入你要设置的时间")
    tm_hour=int(input("请输入几时"))
    tm_min=int(input("请输入几分"))
    tm_sec=int(input("请输入几秒"))
    while True:
        t=time.localtime()
        print("\r%02d:%02d:%02d"%t[3:6])
        time.sleep(1)
        # if  t[3]==tm_hour and t[4]==tm_min and t[5]==tm_sec:
        #     print("主人，你的时间到了")
        #     break
        if t[3:6] == (tm_hour,tm_min,tm_sec):
            print("主人，你的时间到了")
            break

alarmclock()











