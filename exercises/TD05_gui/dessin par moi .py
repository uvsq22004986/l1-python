import tkinter as tk
racine = tk.Tk()
racine.title("Mon dessin")

import random
def cercle(x1=random.randint(0, 400), y1=random.randint(0, 400)):
    canvas.create_oval((x1, y1, x1 + 100, y1 + 100), fill="blue")

button1 = tk.Button(racine, text = "Cercle", font = ("helvetica", "26"),command=cercle)
button2 = tk.Button(racine, text = "Carré", font = ("helvetica", "26"))
button3 = tk.Button(racine, text = "Croix", font = ("helvetica", "26"))
button4 = tk.Button(racine, text = "Choisir une couleur", font = ("helvetica", "26")) 

button1.grid(column = 0 , row = 1)
button2.grid(column = 0, row = 2)
button3.grid(column = 0, row = 3)
button4.grid(column = 1, row = 0 )
canvas = tk.Canvas(racine, bg = "black", height = 500, width = 500)
canvas.grid(column = 1, row = 1, rowspan = 3)



racine.mainloop()