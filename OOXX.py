try:
  import Tkinter as tk
except ImportError:
  import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox

from functools import partial

win = tk.Tk()
count=1
text2=[]
listbtn=[]

def event1(num):
    #print("event1",num)
    global count
    global text2
    #if text2="":

    if count%2!=0 and count<=9:
        text2[num].set("O")
        text2[num]="O"
    elif count<=9:
        text2[num].set("X")
        text2[num]="X"
    listbtn[num].config(state=tk.DISABLED)
    count+=1

    if (text2[0]=="O" and text2[1]=="O" and text2[2]=="O") or (text2[3]=="O" and text2[4]=="O" and text2[5]=="O") or (text2[6] == "O" and text2[7] == "O" and text2[8] == "O") or (text2[0]=="O" and text2[3]=="O" and text2[6]=="O") or (text2[1]=="O" and text2[4]=="O" and text2[7]=="O") or (text2[2] == "O" and text2[5] == "O" and text2[8] == "O") or (text2[0] == "O" and text2[4] == "O" and text2[8] == "O") or (text2[2] == "O" and text2[4] == "O" and text2[6] == "O"):
        messagebox.showinfo("OOXX", "O win")
        exit()
    elif (text2[0]=="X" and text2[1]=="X" and text2[2]=="X") or (text2[3]=="X" and text2[4]=="X" and text2[5]=="X") or (text2[6] == "X" and text2[7] == "X" and text2[8] == "X") or (text2[0]=="X" and text2[3]=="X" and text2[6]=="X") or (text2[1]=="X" and text2[4]=="X" and text2[7]=="X") or (text2[2] == "X" and text2[5] == "X" and text2[8] == "X") or (text2[0] == "X" and text2[4] == "X" and text2[8] == "X") or (text2[2] == "X" and text2[4] == "X" and text2[6] == "X"):
        messagebox.showinfo("OOXX", "X win")
        exit()
    elif count==10:
        messagebox.showinfo("OOXX", "draw")
        exit()


win.title("OOXX")
win.minsize(width=900, height=900)
win.maxsize(width=900, height=900)
win.resizable(width=False, height=False)

canvas=tk.Canvas(win)
canvas.place(x=0,y=0)
canvas.config(width=900, height=900)
canvas.create_line(300, 0, 300, 900)
canvas.create_line(600, 0, 600, 900)
canvas.create_line(0, 300, 900, 300)
canvas.create_line(0, 600, 900, 600)


list1=[[0,0],[300,0],[600,0],[0,300],[300,300],[600,300],[0,600],[300,600],[600,600]]
#print(list1[8][0])
for x in range(9):
    t1 = tk.StringVar()
    text2.append(t1)
    #text2=list(text2)
    btn1 = tk.Button(win, command=partial(event1, x), textvariable=text2[x])
    myFont = font.Font(size=50)
    btn1['font'] = myFont
    btn1.place(x=list1[x][0],y=list1[x][1],height=300,width=300)
    listbtn.append(btn1)
    #listbtn[x]=btn1
"""
text2[x] = tk.StringVar()
btn1=tk.Button(win,command=partial(event1, 0), textvariable=text2[x])   
btn1.place(x=100,y=100,height=100,width=100)
text2[x] = tk.StringVar()
btn2=tk.Button(win,command=partial(event1, 1), textvariable=text2[x])
btn2.place(x=400,y=100,height=100,width=100)
text2[x] = tk.StringVar()
btn3=tk.Button(win,command=partial(event1, 2), textvariable=text2[x])
btn3.place(x=700,y=100,height=100,width=100)
btn4=tk.Button(win,command=event1)
btn4.place(x=100,y=400,height=100,width=100)
btn5=tk.Button(win,command=event1)
btn5.place(x=400,y=400,height=100,width=100)
btn6=tk.Button(win,command=event1)
btn6.place(x=700,y=400,height=100,width=100)
btn7=tk.Button(win,command=event1)
btn7.place(x=100,y=700,height=100,width=100)
btn8=tk.Button(win,command=event1)
btn8.place(x=400,y=700,height=100,width=100)
btn9=tk.Button(win,command=event1)
btn9.place(x=700,y=700,height=100,width=100)
"""






win.mainloop()