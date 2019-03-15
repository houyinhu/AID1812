
def city_country(city,country):
    print("%s %s"%(city ,country))
city_country('santiago','chile')
city_country('beijing','china')
city_country('dongjign','japan')

def make_album(name,album,count=''):
    if count:
        d = {name: [album,count]}
    else:
        d={name:album}

    return d
print(make_album('zhoujielun','yinweiai'))
print(make_album('wangsulong','xiaoxingxing',2))
print(make_album('maobuyi','fan'))
while True:
    name=input("请输入歌手的名字")
    if  name == '' :
        break
    ablum=input("请输入专辑名字")
    if  ablum == '' :
        break
    print(make_album(name,ablum))

