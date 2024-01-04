import tkinter as tk
from math import sin, cos, pi
from perlin_noise import PerlinNoise

root = tk.Tk()
width, height = 100, 100
image = tk.PhotoImage(width=width, height=height)

label = tk.Label(root, image=image)
label.pack()

clock = 0
noise = PerlinNoise()


def update():
    global clock
    clock += 1
    for x in range(width):
        for y in range(height):
            colorValue = abs(noise([x / width, y / height, clock]) * 255)
            rColor = int(colorValue + sin(clock / (8.0 * pi)) * 255) % 255
            gColor = int(colorValue + cos(clock / (16.0 * pi)) * 255) % 255
            bColor = int(colorValue + cos(clock / (32.0 * pi)) * 255) % 255
            image.put("#{0:02x}{1:02x}{2:02x}".format(rColor, gColor, bColor), (x, y))
    root.after(500, update)


update()
root.mainloop()
