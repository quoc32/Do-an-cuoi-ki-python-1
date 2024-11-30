import tkinter as tk
from tkinter import font

root = tk.Tk()

# Lấy font mặc định
default_font = font.nametofont("TkDefaultFont")

# In thông tin về font mặc định
print(f"Font mặc định: {default_font.actual()}")

root.mainloop()
