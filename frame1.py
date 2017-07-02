from tkinter import *

root = Tk()

f0 = Frame(root, width = 60, height = 40, relief = 'groove', borderwidth = 4, bg = 'gray')
f1 = Frame(root, width = 60, height = 40, relief = 'groove', borderwidth = 4, bg = 'gray')

f0.pack(padx = 5, pady = 5, side = 'left')
f1.pack(padx = 5, pady = 5, side = 'left')

root.mainloop()
