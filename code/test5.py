import pandas as pd
import tkinter as tk
from tkinter import ttk
from io import StringIO

def show_info():
    # Tạo một StringIO để lưu trữ thông tin
    buffer = StringIO()
    
    # Ghi thông tin tổng quan vào buffer
    df.info(buf=buffer)
    info_buffer = buffer.getvalue()

    # Thêm thống kê mô tả
    stats = df.describe().to_string()

    # Xóa nội dung cũ trong ô văn bản
    text_box.delete(1.0, tk.END)  # Xóa nội dung cũ
    # Thêm thông tin mới vào ô văn bản
    text_box.insert(tk.END, info_buffer + "\n\n" + stats)  # Thêm thông tin mới
    text_box.config(state=tk.DISABLED)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin Dữ liệu")
root.geometry("400x300")

# Đọc dữ liệu từ file CSV
df = pd.read_csv('../data/data.csv')

# Tạo nút để hiển thị thông tin
button = ttk.Button(root, text="Hiển thị Thông tin", command=show_info)
button.pack(pady=10)

# Tạo ô văn bản để hiển thị thông tin
text_box = tk.Text(root, width=80, height=20)
text_box.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
