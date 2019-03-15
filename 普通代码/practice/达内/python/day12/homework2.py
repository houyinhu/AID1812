import time
# 2，写一个程序，以电子时钟格式打印时间
#     格式为：
#         HH:MM:SS

def time_format():
    while True:
        time_localtime=time.localtime()
        tm_hour=time_localtime[3]
        tm_min = time_localtime[4]
        tm_sec = time_localtime[5]
        # print("%s:%s:%s"%(tm_hour,tm_min,tm_sec),end='\r')
        print("\r%s:%s:%s"%(tm_hour,tm_min,tm_sec),end='')
        time.sleep(1)

        # print("%s:%s:%s"%time_localtime[3:6])

time_format()








