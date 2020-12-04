import tkinter as tk
racine = tk.Tk()
racine.title("tk")
import random
def cercle(x1=random.randint(0, 300), y1=random.randint(0, 300)):
    canvas.create_oval((x1, y1, x1 + 100, y1 + 100), fill="red")
print(cercle)
canvas = tk.Canvas(racine, bg = "black", height = 500, width = 500)
canvas.grid(column = 1, row = 1, rowspan = 3)
racine.mainloop()
