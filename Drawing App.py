from PIL import Image , ImageDraw
from tkinter import *
root = Tk()
root.geometry("1200x1200")
root.title("Draw")
Canvas = Canvas( width=900 , height=900 , bg="WHITE")
Canvas.place(relx = 0.5 , rely=0.5 , anchor="center")
Canvas.pack(side="top", expand=True)
def mouse_click(event):
   Canvas.bind("<Button-1>", mouse_click )
   Canvas.focus_set()
   global last_x , last_y
   last_x , last_y = event.x , event.y
def mouse_motion(event):
   Canvas.bind("<B1-Motion>", mouse_motion)
   Canvas.focus_set()
   global last_x , last_y
   Canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=2)
   last_x , last_y = event.x , event.y
Canvas.bind("<Button-1>", mouse_click )
Canvas.bind("<B1-Motion>", mouse_motion)
Canvas.focus_set()
Current_color = "black"
#continue with colors
root.mainloop()