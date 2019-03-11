import tkinter as tk
import tkinter.messagebox
import pickle

window = tk.Tk()
window.title('Wellcome to 海贼王')
window.geometry('500x300')

#第四步，加载wellcome image
canvas = tk.Canvas(window,width=400,height=135,bg='green')
image_file = tk.PhotoImage(file='pic.gif')
image = canvas.create_image(200,0,anchor='n',image=image_file)
canvas.pack(side='top')
tk.Label(window,text='Wellcome',font=('Arial',16)).pack()

#第五步用户信息
tk.Label(window,text='用户名:',font=("Arial",14)).place(x=10,y=170)
tk.Label(window,text='密码:',font=('Arial',14)).place(x=10,y=210)

#第6步，用户登录输入框entry
#用户名
var_usr_name = tk.StringVar()
var_usr_name.set('')
entry_usr_name = tk.Entry(window,textvariable=var_usr_name,font=('Arial',14))
entry_usr_name.place(x=120,y=175)
#用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,font=('Arial',14),show='*')
entry_usr_pwd.place(x=120,y=215)


#第8步，定义用户登录功能
def usr_login():
    #获取用户输入的usr_name和usr_pwd
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    #捕获异常
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except OSError:
        #没有读取到usr_file的时候，程序回创建一个usr_file这个文件，并将管理员
        #的用户和密码写入，即用户名为admin密码为aimin
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
            usr_file.close()#必须先关闭，否则pickle.load()会出现EOFError: Ran out of input
    #如果用户名和密码文件中的匹配成功，则会登录成功，并跳出弹窗how are you？加上你的用户名
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(title='Welcome',message='How are you?'+usr_name)
        #如果用户名匹配成功，而密码输入错误，则会弹出'Error your password is wrong,try again.
        else:
            tkinter.messagebox.showerror(message='Error,your password is wrong,try again.')
    else:#如果发现用户名不存在
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ','你需要一个帐号，现在就去注册？')
        #提示需不需要注册新用户
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to():
        #获取注册时输入的信息
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        #这里是打开我们记录数据的文件，将注册信息读出
        with open('usrs_into.pickle','rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        #判断两次密码输入是否一致，
        
        if np != npf:
            tkinter.messagebox.showerror("两次密码不一致")
        #用户名已经在数据文件中
        elif nn in exist_usr_info:
            tkinter.messagebox.showerror("用户已经存在")
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tkinter.messagebox.showinfo("注册成功")
            #销毁窗口
            window_sign_up.destroy()



    
    #定义长在窗口上的窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('300x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()#将输入的注册名赋值给变量
    new_name.set('')
    tk.Label(window_sign_up,text='用户名: ').place(x=10,y=10)#将'User name:'放置坐标（10,10）
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)#创建一个注册名的’entry‘，变量为’new_name'
    entry_new_name.place(x=130,y=10)#放置在坐标(130,10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='密码: ').place(x=10,y=50)
    entry_usr_pwd = tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_usr_pwd.place(x=130,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text='再次输入密码: ').place(x=10,y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_usr_pwd_confirm.place(x=130,y=90)

    #下面的sign_to_海贼王
    btn_comfirm_sign_up = tk.Button(window_sign_up,text='注册',\
        command=sign_to)
    btn_comfirm_sign_up.place(x=180,y=120)




#第七步，longin and sign up按钮
btn_login = tk.Button(window,text='登录',command=usr_login)
btn_login.place(x=120,y=240)
btn_sign_up = tk.Button(window,text='注册',command=usr_sign_up)
btn_sign_up.place(x=200,y=240)

window.mainloop()


