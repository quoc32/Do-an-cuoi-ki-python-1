import tkinter as tk
from tkinter import ttk

def on_select(event):
    # Lấy giá trị đã chọn từ combobox đầu tiên
    selected_value = combo1.get()
    
    # Cập nhật danh sách giá trị cho combobox thứ hai
    # Xóa giá trị đã chọn khỏi danh sách các giá trị trong combobox thứ hai
    combo2['values'] = [val for val in original_values if val != selected_value]
    
    # Đặt lại giá trị của combobox thứ hai
    combo2.set('')

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Khóa giá trị trong Combobox")

# Danh sách các giá trị
original_values = ["Giá trị 1", "Giá trị 2", "Giá trị 3", "Giá trị 4"]

# Tạo Combobox đầu tiên
combo1 = ttk.Combobox(root, values=original_values)
combo1.pack(pady=10)
combo1.bind("<<ComboboxSelected>>", on_select)  # Gán hàm xử lý sự kiện

# Tạo Combobox thứ hai
combo2 = ttk.Combobox(root, values=original_values)
combo2.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
