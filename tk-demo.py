
import os
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title('Windows Demo')

# width x height ±x ±y
#root.geometry('600x400+50+50')

#Resizing behavior
#root.resizable(False, False)

#windows Transparency
#root.attributes('-alpha', 0.9)

try:
    root.iconbitmap('./assets/pythontutorial.ico')
except tk.TclError:
    print("ICO icon file not found.")

# Load and resize PNG to 50x50
icon_path = './assets/python-icon.png'
if os.path.exists(icon_path):
    try:
        image = Image.open(icon_path)
        image = image.resize((50, 50), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        root.iconphoto(False, photo)  # Optional: window icon
        img_label = tk.Label(root, image=photo)
        img_label.image = photo  # Prevent garbage collection
        img_label.pack(pady=20)

    except Exception as e:
        print("Error loading image:", e)
else:
    print("PNG icon file not found.")

root.mainloop()