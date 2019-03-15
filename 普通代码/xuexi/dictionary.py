# a=[]
# for i in range(1,11):
#         a.append(i)

# b=[i for i in range(1,11)]
# print(b)

# import time
# a=[]
# t0=time.clock()
# for i in range(1,20000):
#         a.append(i)
# print(time.clock()-t0,"seconds process time")
# t0=time.clock()
# b=[i for i in range(1,20000)]
# print(time.clock()-t0,"seconds process time")
'''
NASDAQ_code = {
        'BIDU':'Baidu',
        'SINA':'Sina',
        'YOKU':'Youku'
}
print(NASDAQ_code)

key_test={'a':'a Test'}
print(key_test)
'''
class Song(object):
        def __init__(self,lyrics):
                self.lyrics = lyrics
        def sing_me_a_song(self):
                for line in self.lyrics:
                        print(line)
happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
bulls_on_parade = Song(["They tally around the family",
"With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

