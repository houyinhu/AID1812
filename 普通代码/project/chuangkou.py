
import tkinter as tk
 
class APP:
    def __init__(self, master):
        frame = tk.Frame(master)  #Frame框架是放在顶层窗口里的。框架一般用于在复杂的布局里面将这些组件分组的是
        frame.pack(side=tk.LEFT, padx=200, pady=500) #side共有四个参数：Right，LEFT，TOP，BOTTOM
        #padx, pady设置框架距离顶层窗口x轴，y轴的距离
        
        #注意要加上command参数，参数值为函数名。当按钮被按下时，就会调用该方法
        self.hi_there = tk.Button(frame, text='打招呼', bg='black', fg='blue', command=self.say_hi)  
        #创建一个按钮组件，放在Frame框架里。bg设置背景色的颜色。fg是前景色的意思（英文没听清楚），把打招呼的颜色设置为蓝色.
        self.hi_there.pack()
        
    def say_hi(self):
        print('空朋们好，这是我的第二个GUI程序。')
 
 
root = tk.Tk()   #先创建一个顶层窗口
app = APP(root)  #再实例化这个APP
 
root.mainloop()