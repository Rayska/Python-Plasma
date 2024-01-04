import tkinter as tk
from pyfastnoiselite.pyfastnoiselite import FastNoiseLite, NoiseType
from PIL import Image, ImageGrab


def save_image():
    label_id = label.winfo_id()
    x, y, w, h = label.winfo_rootx(), label.winfo_rooty(), label.winfo_width(), label.winfo_height()
    image_data = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    image_data.save("output_image.png")


root = tk.Tk()
width, height = 1650, 500
image = tk.PhotoImage(width=width, height=height)

label = tk.Label(root, image=image)
label.pack()

noise = FastNoiseLite()
noise.noise_type = NoiseType.NoiseType_Perlin

color_format = "#{0:02x}{1:02x}{2:02x}"
colors = [
    (238, 108, 77),
    (224, 251, 252),
    (41, 50, 65)
]

noise_values = [
    [255 * abs(noise.get_noise(x, y)) for y in range(height)]
    for x in range(width)
]

flat_noise_values = [value for row in noise_values for value in row]

color_values = [
    color_format.format(*color) for color in colors
]

color_indices = [
    0 if value > 130 else 1 if 50 < value <= 130 else 2
    for value in flat_noise_values
]

for idx, color_index in enumerate(color_indices):
    x, y = divmod(idx, height)
    image.put(color_values[color_index], (x, y))

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack()

root.mainloop()
