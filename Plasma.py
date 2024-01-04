import tkinter as tk
from pyfastnoiselite.pyfastnoiselite import FastNoiseLite, NoiseType

root = tk.Tk()
width, height = 500, 500
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

# Flatten the noise_values list
flat_noise_values = [value for row in noise_values for value in row]

# Precompute color values
color_values = [
    color_format.format(*color) for color in colors
]

# Create a list of color indices based on noise values
color_indices = [
    0 if value > 130 else 1 if 50 < value <= 130 else 2
    for value in flat_noise_values
]

# Use the put method with color indices
for idx, color_index in enumerate(color_indices):
    x, y = divmod(idx, height)
    image.put(color_values[color_index], (x, y))

root.mainloop()
