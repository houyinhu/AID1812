import tkinter as tk
window = tk.Tk()
window.title("啊虎")
window.geometry("500x300")

#创建一个标签label用以显示并放置
var = tk.StringVar()
l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

#定义选项触发函数功能
def print_selection():
    l.config(text='you have selected ' + var.get())


#创建三个radiobutton选项
r1 = tk.Radiobutton(window,text='Option A',variable=var,\
    value='A',command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window,text='Option B',variable=var,\
    value='B',command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window,text='Option C',variable=var,\
    value='C',command=print_selection)
r3.pack()


window.mainloop()










