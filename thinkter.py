#coding=utf-8
from tkinter import *
root = Tk()

li = ['C','python','java','html','javascript']
movie = ['css','bootstrap','jquery']
listb = Listbox(root)
listc = Listbox(root)


for item in li:
    listb.insert(0,item)
for item in movie:
    listc.insert(0,item)
listb.grid()
listc.grid()
root.mainloop()