import Tkinter 
from Tkinter import *

root = Tk()

c = Canvas(root, width = 1280 , height = 720)

c.pack()

ball = c.create_oval(25, 25, 75, 75,fill="#333")
root.mainloop()

