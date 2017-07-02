from Tkinter import *

root = Tk()

lf1 = LabelFrame(root, text = 'Apple', width = 80, height = 60, relief = 'sunken', labelanchor = N)
lf2 = LabelFrame(root, text = 'Banana', width = 80, height = 60, relief = 'sunken', labelanchor = N)

lf1.pack(padx = 5, pady = 5, side = LEFT)
lf2.pack(padx = 5, pady = 5, side = LEFT)

root.mainloop()
