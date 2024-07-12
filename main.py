import tkinter as tk
from tkinter import ttk

def update_color():
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()

    hex_code = "#{:02X}{:02X}{:02X}".format(r, g, b)
    color_label.config(text="RGB Color: ({}, {}, {})".format(r, g, b))
    canvas.config(bg=hex_code)
    hex_label.config(text="Hex Code: {}".format(hex_code))

# Create the main window
root = tk.Tk()
root.title("RGB Color Generator")

# Configure window background color
root.configure(bg="white")

# Create sliders
red_label = tk.Label(root, text="Red:")
green_label = tk.Label(root, text="Green:")
blue_label = tk.Label(root, text="Blue:")

red_slider = tk.Scale(root, from_=0, to=255, length=300, orient="horizontal")
green_slider = tk.Scale(root, from_=0, to=255, length=300, orient="horizontal")
blue_slider = tk.Scale(root, from_=0, to=255, length=300, orient="horizontal")

# Create color label
color_label = tk.Label(root, text="RGB Color:", font=("Helvetica", 16))

# Create canvas to display color
canvas = tk.Canvas(root, width=200, height=200)

# Create hex code label
hex_label = tk.Label(root, text="Hex Code:", font=("Helvetica", 12))

# Create update button
update_button = ttk.Button(root, text="Update Color", command=update_color)

# Grid layout
red_label.grid(row=0, column=0, padx=10, pady=10)
red_slider.grid(row=0, column=1, padx=10, pady=10)
green_label.grid(row=1, column=0, padx=10, pady=10)
green_slider.grid(row=1, column=1, padx=10, pady=10)
blue_label.grid(row=2, column=0, padx=10, pady=10)
blue_slider.grid(row=2, column=1, padx=10, pady=10)
color_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
canvas.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
hex_label.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
update_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
