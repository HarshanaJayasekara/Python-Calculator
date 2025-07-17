from tkinter import *
from PIL import Image, ImageTk

# 🪟 Create and configure main window
window = Tk()
window.title("Awesome GUI")
window.geometry("520x620")
window.config(bg="#1b4332")

# 🌄 Load and resize header image
icon = Image.open("assets/python-icon.png")
icon = icon.resize((120, 120))
icon_photo = ImageTk.PhotoImage(icon)

# 🏷️ Styled Header Label
header = Label(window,
               text="Hello World",
               image=icon_photo,
               compound='bottom',
               font=('Arial', 36, 'bold'),
               bg='#1b4332',
               fg='#fefae0',
               bd=8,
               relief=RIDGE,
               padx=20,
               pady=20)
header.pack(pady=15)

# 🔢 Counter setup
count = 0

def increment():
    global count
    count += 1
    counter_label.config(text=str(count))

# 🖼️ Load and style button icon
btn_icon = PhotoImage(file='assets/icons8.png')

# 🎯 Button with Icon and Click Logic
click_button = Button(window,
                      text="Click Me",
                      image=btn_icon,
                      compound='top',
                      command=increment,
                      font=('Ink Free', 28, 'bold'),
                      bg='#d00000',
                      fg='white',
                      activebackground='#6a040f',
                      activeforeground='white',
                      bd=5,
                      relief=RAISED)
click_button.pack(pady=10)

# 📊 Counter Display Label
counter_label = Label(window,
                      text=str(count),
                      font=('Consolas', 42, 'bold'),
                      bg='#1b4332',
                      fg='#ffd60a')
counter_label.pack(pady=5)

# ⌨️ Entry Field with Styling
entry = Entry(window,
              font=('Consolas', 28),
              bg='#f0efeb',
              fg='#003049',
              bd=4,
              relief=SUNKEN,
              justify='center')
entry.pack(pady=20)

# 🏁 Launch the GUI
window.mainloop()
