import tkinter as tk
window = tk.Tk()
window.title("啊虎")
window.geometry("500x300")

l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() ==1 ) & (var2.get() == 1):
        l.config(text='I love bogy')
    elif (var1.get() == 0 ) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0 ) & (var2.get() == 0):
        l.config(text='I do not love either')

#定义两个checkbutton选项
var1 = tk.IntVar()#定义var1和var2整型变量
var2 = tk.IntVar()
c1 = tk.Checkbutton(window,text='Python',variable=var1,\
    onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window,text='C++',variable=var2,\
    onvalue=1,offvalue=0,command=print_selection)
c2.pack()
window.mainloop()





