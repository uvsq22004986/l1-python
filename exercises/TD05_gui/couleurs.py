import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    """ Colorie le pixel de coordonnées (i,j) de la couleur color """
    canvas.create_line((i, j), (i+1, j), fill=color)

def ecran_aleatoire():
    pass

def degrade_gris():
    pass

def degrade_2D():
    pass

racine = tk.Tk()
# création des widgets
bouton_cercle = tk.Button(racine, text="Aléatoire", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=ecran_aleatoire)
bouton_carre = tk.Button(racine, text="Dégradé gris", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_gris)
bouton_croix = tk.Button(racine, text="Dégradé 2D", bg="grey100", fg="blue", padx=20, font=("Times", "20"), command=degrade_2D)
canvas = tk.Canvas(racine, width=256, height=256, bg="black")
# placement des widgets
bouton_cercle.grid(column=0, row=1)
bouton_carre.grid(column=0, row=2)
bouton_croix.grid(column=0, row=3)
canvas.grid(column=1, row=1, rowspan=3)
racine.mainloop()