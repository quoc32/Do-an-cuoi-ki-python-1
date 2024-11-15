import tkinter as tk
from PIL import Image, ImageTk

# Khởi tạo cửa sổ Tkinter
window = tk.Tk()
window.title("Thêm ảnh vào Tkinter")

# Mở ảnh bằng PIL và chuyển đổi sang ImageTk
img = Image.open("./image/cachua.png")  # Thay thế bằng đường dẫn tới ảnh của bạn
img = img.resize((200, 200))  # Tùy chỉnh kích thước ảnh nếu cần
tk_img = ImageTk.PhotoImage(img)

# Thêm ảnh vào giao diện với widget Label
label = tk.Label(window, image=tk_img)
label.pack()

# Chạy vòng lặp giao diện
window.mainloop()
