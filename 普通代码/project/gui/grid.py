import tkinter as tk
window = tk.Tk()
window.title("啊虎")
window.geometry("500x300")


for i in range(3):
    for j in range(3):
        tk.Label(window,text=1).grid(row=i,column=j,\
            padx=10,pady=10,ipadx=10,ipady=10)


window.mainloop()







