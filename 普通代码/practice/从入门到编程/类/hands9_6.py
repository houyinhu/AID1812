from hands9_1 import Restaurant

class IceCreanStand(Restaurant):
    def __init__(self,flavors):
        self.flavors = flavors
    def ice(self):
        i1=''
        for i in  self.flavors:
            i1+=i+' '
        print("ice的口味有："+i1)

icekou=['1','2','3']
icecrea=IceCreanStand(icekou)
icecrea.ice()
















