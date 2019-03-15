
# 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为
# show_magicians()的函数，这个函数打印列表中每个魔术师的名字

mo=['li','wang','zhang','sun']
def show_magicians(mo):
    for x in mo:
        print(x)
show_magicians(mo)

# 8-10 了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为
# make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the
# Great”。调用函数 show_magicians()，确认魔术师列表确实变了

def make_great(mo):
    d = {}
    for x in mo:
        d[x]='the Great'
    print(d)
d = []
def make_great(mo):
    while mo:
        mo1 = mo.pop()
        d.append(mo1+' the Great')
    # for x in mo:
    #     d.append(x+' the Great')
    print(d)
make_great(mo[:])
print(mo)
show_magicians(mo)
show_magicians(d)

