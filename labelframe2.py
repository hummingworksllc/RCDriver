from tkinter import *

root = Tk()

lf1 = LabelFrame(root, text = 'Store A', relief = 'sunken', labelanchor = N)
lf2 = LabelFrame(root, text = 'Store B', relief = 'sunken', labelanchor = N)

btnApple = Button(lf1, text = 'Apple')
btnApple.pack(side = LEFT)

btnBanana = Button(lf1, text = 'Banana')
btnBanana.pack(side = LEFT)

btnCandy = Button(lf1, text = 'Candy')
btnCandy.pack(side = LEFT)

btnDonut = Button(lf2, text = 'Donut')
btnDonut.pack(fill = BOTH)

btnEgg = Button(lf2, text = 'Egg')
btnEgg.pack(fill = BOTH)

btnFruit = Button(lf2, text = 'Fruit')
btnFruit.pack(fill = BOTH)

lf1.pack(padx = 5, pady = 5, side = LEFT)
lf2.pack(padx = 5, pady = 5, side = LEFT)

root.mainloop()
