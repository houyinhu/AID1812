from tkinter import *

#实例化object，建立窗口window
window = Tk()

#给窗口可视化起名字
window.title("My window")

#设定窗口的大小（长*宽）
window.geometry('500x300')  #乘是小x

#在图形界面上设定标签
var = StringVar()#将label标签的内容设置为字符类型，用var接受hit_me函数的传出内容用以显示在标签上
l = Label(window,text='你好 this is Tkinter',bg='red',\
    font=('Arial',12),width=30,height=2)
#bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

#第五步，放置标签
l.pack()    #Label内容content区域放置位置，自动调节尺寸
#放置lable的方法有：    l.pack()    l.place();


#第定义一个函数功能，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me ')
    else:
        on_hit = False
        var.set('')
#在窗口界面设置放置Button按键
b = Button(window,text='hit me',font=('Arial',12),width=10,\
    heigh=1,command=hit_me)
b.pack()
#第六步 主窗口循环显示
window.mainloop()
#loop循环，window.mainloop就会让window不断的刷新，如果没有mainloop,
# 就是一个静态的window,传入进去的值就不会有循环，
# mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，


