import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Ứng Dụng với Nhiều Trang")

        # Tạo một khung chứa các nút điều hướng
        self.navigation_frame = ttk.Frame(self)
        self.navigation_frame.pack(side=tk.TOP, fill=tk.X)

        # Tạo các nút điều hướng
        self.button1 = ttk.Button(self.navigation_frame, text="Trang 1", command=lambda: self.show_frame(Page1))
        self.button1.pack(side=tk.LEFT, padx=5, pady=5)

        self.button2 = ttk.Button(self.navigation_frame, text="Trang 2", command=lambda: self.show_frame(Page2))
        self.button2.pack(side=tk.LEFT, padx=5, pady=5)

        self.button3 = ttk.Button(self.navigation_frame, text="Trang 3", command=lambda: self.show_frame(Page3))
        self.button3.pack(side=tk.LEFT, padx=5, pady=5)

        # Tạo một khung để chứa các trang
        self.frames = {}
        for F in (Page1, Page2, Page3):  # Sửa đổi ở đây
            frame = F(self)
            self.frames[F] = frame
            frame.pack(fill=tk.BOTH, expand=True)

        # Hiển thị trang đầu tiên
        self.show_frame(Page1)

    def show_frame(self, page):
        # Ẩn tất cả các trang
        for frame in self.frames.values():
            frame.pack_forget()
        # Hiển thị trang được chọn
        self.frames[page].pack(fill=tk.BOTH, expand=True)

class Page1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="Đây là Trang 1", font=("Arial", 24))
        label.pack(pady=10)
        # Thêm các nút hoặc tiện ích khác ở đây

class Page2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="Đây là Trang 2", font=("Arial", 24))
        label.pack(pady=10)
        # Thêm các nút hoặc tiện ích khác ở đây

class Page3(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="Đây là Trang 3", font=("Arial", 24))
        label.pack(pady=10)
        # Thêm các nút hoặc tiện ích khác ở đây

# Chạy ứng dụng
if __name__ == "__main__":
    app = App()
    app.mainloop()
