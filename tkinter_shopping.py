#coding:utf-8
import sys
from Tkinter import *
root=Tk()
root.title("Shopping")   #窗口标题设置
root.geometry("600x600") #窗口大小设置，注意x
#标题设置
l=Label(root,text="消费能力计算",bg="blue",font=("Arial",16))
l.pack(side=TOP,pady=20)  #pack取值不同，可以采用padx/pady来修改x或y轴的距离


root.mainloop()