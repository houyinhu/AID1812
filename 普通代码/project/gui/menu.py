import tkinter as tk
window = tk.Tk()
window.title("啊虎")
window.geometry("500x300")

#第四步，在图形界面上创建一个标签用以显示内容并放置
l = tk.Label(window,text='    ',bg='green')
l.pack()

#第十步，定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter +=1

#第五步，创建一个菜单栏，这里我们可以吧他理解称一个容器，在窗口的上方
menubar = tk.Menu(window)

#第六步，创建一个file菜单项（默认不下拉，下拉内容包括New,Open,Save,Exit功能项）
filemenu = tk.Menu(menubar,tearoff=0)
#将上面定义的空菜单命名为file，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File',menu=filemenu)

#在File中加入New、Open、Save、等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()#添加一条分割线
filemenu.add_command(label='Exit',command=window.quit)#用tkinter里面自带的quit()函数

#第七步,创建一个Edit菜单项（默认不下拉，)
editmenu = tk.Menu(menubar,tearoff=0,)
#将上面定义的空菜单命名为Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Edit',menu=editmenu)

#同样的在Edit中加入Cut、Copy、Paste等功能单元，如果点击这些单元，触发do_job功能）
editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

#第八步，创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu)#和上面定义菜单一样，不过此处书在File上创建一个空的菜单
filemenu.add_cascade(label='Import',menu=submenu,underline = 0)#给放入的惨淡submenu命名为Import

#第九步，创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令
submenu.add_command(label='Submenu_1',command=do_job)#在Import菜单项中加入一个小菜单命令Submenu_1

第11步创建菜单栏完成后，配置让菜单栏menubar显示出来
window.config(menu=menubar)



window.mainloop()











