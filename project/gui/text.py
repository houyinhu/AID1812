import tkinter as tk

window = tk.Tk()
window.title("啊虎")
window.geometry("500x300")#这里的乘是小x

#设置输入框控件entry框并放置
e = tk.Entry(window,show ='***')
e.pack()

#定义两个触发函数
def insert_point():#在鼠标焦点出输入内容
    var = e.get()
    t.insert('insert',var)
def insert_end():#在文本框内容最后接着输入内容
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(window,text='insert point',width=10,\
    height=2,command=insert_point)
b1.pack()

b2 = tk.Button(window,text='insert end',width=10,\
    height=2,command=insert_end)
b2.pack()

t = tk.Text(window,height=3)
t.pack()

window.mainloop()







