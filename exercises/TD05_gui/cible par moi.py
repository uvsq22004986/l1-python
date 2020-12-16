import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
root = tk.Tk()
root.title("tk")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief = tk.GROOVE, bd = 1)

def draw_circle(x, y , ray, color):
    canvas.create_oval(x-ray, y-ray, x+ray, y+ray, fill = color)

cx = CANVAS_WIDTH/2
cy = CANVAS_HEIGHT/2
colors = ["bleu", "green", "black", "yellow", "magenta", "red"]

def draw_circle(n):
    ray = CANVAS_HEIGHT/2/n
    for i in range(n, 0, -1):
        draw_circle(cx, cy, ray*1, colors[i%len(colors)])

draw_circle(200)

canvas.pack()
root.mainloop()
