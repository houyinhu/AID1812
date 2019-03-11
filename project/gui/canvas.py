import tkinter as tk
window = tk.Tk()
window.title("啊虎")
window.geometry("500x300")

#在图形界面创建500×200大小的画布并放置各种元素
canvas = tk.Canvas(window,bg='green',height=200,width=500)
#说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(250,0,anchor='n',image=image_file) # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
#定义多边形参数，然后在画布上画出指定图形
x0,y0,x1,y1 = 100,100,150,150
line = canvas.create_line(x0-50,y0-50,x1-50,y1-50)  #画直线
ova1 = canvas.create_oval(x0+120,y0+40,x1+120,y1+50,fill='yellow')#画圆，黄色填充
arc = canvas.create_arc(x0,y0+50,x1,y1+50,start=0,extent=180)#画扇形，从0度打开到180度结束
rect = canvas.create_rectangle(330,30,330+20,30+20)#画矩形正方形
canvas.pack()

def moveit():
    canvas.move(arc,2,2)#移动正方形rect(也可以改成其他图形名字用以移动一起图形，元素)，按每次（x=2,y=2）步长金喜移动

#定义按钮用来移动指定图形在画布上的位置
b = tk.Button(window,text='move item',command=moveit).pack()



window.mainloop()








