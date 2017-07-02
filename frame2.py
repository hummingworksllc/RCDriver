from tkinter import *

root = Tk()

f0 = Frame(root, width = 60, height = 40, relief = 'groove', borderwidth = 4, bg = 'gray')
f1 = Frame(root, width = 60, height = 40, relief = 'groove', borderwidth = 4, bg = 'gray')

btnApple = Button(f0, text = 'Apple')
btnApple.pack(side = LEFT)

btnBanana = Button(f0, text = 'Banana')
btnBanana.pack(side = LEFT)

btnCandy = Button(f0, text = 'Candy')
btnCandy.pack(side = LEFT)

btnDonut = Button(f1, text = 'Donut')
btnDonut.pack(fill = BOTH)

btnEgg = Button(f1, text = 'Egg')
btnEgg.pack(fill = BOTH)

btnFruit = Button(f1, text = 'Fruit')
btnFruit.pack(fill = BOTH)

f0.pack(padx = 5, pady = 5)
f1.pack(padx = 5, pady = 5, fill = BOTH)

root.mainloop()
