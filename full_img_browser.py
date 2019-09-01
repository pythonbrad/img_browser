from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from tkinter.ttk import Progressbar
import glob

screen = (1280,1024)
image = []

fen = Tk()
fen.geometry('%sx%s+0+0'%screen)
fen.resizable(False,False)
fen.overrideredirect(True)
fen.bind('<Button-1>', lambda x:fen.destroy())
label = Label(text='dir',font=('Comic Sans MS', 10),compound=CENTER)
label.pack()
showinfo(message='Mouse Button 1 to exit.')

def tree(a):
   for b in a:
      if b.split('.')[-1] in ['png','jpg','gif','ico','bmp']:
         try:
            img = Image.open(b).resize(screen)
            img = ImageTk.PhotoImage(image=img)
            label.config(image=img,text=b)
         except Exception as error:
            print(error, b)
         fen.update()
      c = glob.glob(b+'/*')
      tree(c)
      
tree(glob.glob('c:\*'))

fen.mainloop()
