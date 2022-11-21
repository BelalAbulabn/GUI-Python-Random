from tkinter import *
from tkinter import ttk
import random

root = Tk()
frm = ttk.Frame(root, padding=300)
frm.grid()
n = random.randint(5, 50)


def Random_Positions():
  randomlist = []
  for i in range(0, n):
    o = random.randrange(10, 290, 10)
    randomlist.append(o)
  print(randomlist)

  return randomlist


Array = []
Array = Random_Positions()
x = random.randint(5, 300)
p = random.randrange(-20, 100, 20)
#root.geometry('250x200+250+200')
Label(root, text="Position 1").place(x=n, y=x)
print("the x postion 1 is ", n, "the y postion 1 is", x)
for i in range(0, 10):
  Button(root, text="Button ", height=5, width=10).place(x=Array[i+3],
                                                         y=Array[i + 4])
for i in range(0, 5):
  Label(root, text="Label ").place(x=Array[i],
                                                         y=Array[i + 1])
Label(root, text="Position 2 ").place(x=n + p, y=x + p)
p = random.randrange(-20, 100, 20)
print("the x postion 2 is ", n + p, "the y postion 2 is", x + p)

Label(root, text="Position 3 ").place(x=n + p, y=x + p)
print("the x postion 3 is ", n + p, "the y postion 3 is", x + p)
ttk.Label(frm).grid(column=2, row=2)
print(Array)

#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
