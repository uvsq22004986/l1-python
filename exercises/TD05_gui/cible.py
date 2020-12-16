import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
racine = tk.Tk()
racine.title("DESSIN")
canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg ="black", relief = tk.GROOVE, bd = 1)

def draw_circles(x, y, ray, color) :
    canvas.create_oval(x-ray, y-ray, x+ray, y+ray, fill=color)

cx = CANVAS_WIDTH/2
cy = CANVAS_HEIGHT/2

color = ["bleu", "green", "black", "yellow", "magenta", "red"]

def draw_circles(n):
    ray = CANVAS_HEIGHT/2/n
    for i in range(n, 0, -1):
        draw_circle(cx, cy, ray*i, colors[i%len(color)])

draw_circles(200)

canvas.pack()
racine.mainloop()