import pandas as pd
import tkinter as tk
from tkinter import ttk

file_path = '../data/dataset/data.csv'
data = pd.read_csv(file_path)

# Thiết lập kích thước trang
so_dong_tren_trang = 30
tong_so_dong = len(data)
tong_so_trang = (tong_so_dong // so_dong_tren_trang) + (tong_so_dong % so_dong_tren_trang > 0)

# Khởi tạo cửa sổ tkinter và Treeview
window = tk.Tk()
window.title("Hiển thị dữ liệu")
cols = list(data.columns)
tree = ttk.Treeview(window, columns=cols, show='headings', height=so_dong_tren_trang)  # Cập nhật số dòng hiển thị là 30

# Cập nhật độ rộng cho các cột sao cho phù hợp
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor='center')  # Thiết lập độ rộng cho cột

tree.pack(expand=True, fill=tk.BOTH)

# Khung chứa các nút và nhãn số trang
trang_hien_tai = 0
frame_trang = tk.Frame(window)
frame_trang.pack(fill=tk.X, pady=10)

# Hàm hiển thị dữ liệu theo trang
def hien_thi_du_lieu(trang):
    for row in tree.get_children():
        tree.delete(row)
    
    bat_dau = trang * so_dong_tren_trang
    ket_thuc = bat_dau + so_dong_tren_trang
    for _, row in data.iloc[bat_dau:ket_thuc].iterrows():
        tree.insert("", "end", values=list(row))
    
    # Cập nhật nhãn số trang
    label_trang.config(text=f"Trang {trang + 1}/{tong_so_trang}")

# Hàm chuyển sang trang trước
def trang_truoc():
    global trang_hien_tai
    if trang_hien_tai > 0:
        trang_hien_tai -= 1
        hien_thi_du_lieu(trang_hien_tai)

# Hàm chuyển sang trang sau
def trang_sau():
    global trang_hien_tai
    if trang_hien_tai < tong_so_trang - 1:
        trang_hien_tai += 1
        hien_thi_du_lieu(trang_hien_tai)

# Hàm chuyển đến trang theo số trang nhập vào
def den_trang():
    global trang_hien_tai
    try:
        trang_moi = int(entry_trang.get()) - 1  # Số trang bắt đầu từ 0
        if 0 <= trang_moi < tong_so_trang:
            trang_hien_tai = trang_moi
            hien_thi_du_lieu(trang_hien_tai)
        else:
            # Nếu trang nhập vào không hợp lệ
            label_trang.config(text="Trang không hợp lệ!")
    except ValueError:
        # Nếu người dùng không nhập vào số hợp lệ
        label_trang.config(text="Vui lòng nhập số hợp lệ!")

# Nút trang trước và sau
btn_truoc = tk.Button(frame_trang, text="Trang trước", command=trang_truoc)
btn_truoc.pack(side=tk.LEFT, padx=10)

# Nhãn số trang
label_trang = tk.Label(frame_trang, text=f"Trang {trang_hien_tai + 1}/{tong_so_trang}")
label_trang.pack(side=tk.LEFT, padx=10, expand=True)

btn_sau = tk.Button(frame_trang, text="Trang sau", command=trang_sau)
btn_sau.pack(side=tk.RIGHT, padx=10)

# Khung chứa ô nhập liệu và nút "Đi đến trang"
frame_nhap_trang = tk.Frame(window)
frame_nhap_trang.pack(pady=10)

# Ô nhập liệu cho số trang
entry_trang = tk.Entry(frame_nhap_trang)
entry_trang.pack(side=tk.LEFT, padx=10)

# Nút để chuyển đến trang nhập vào
btn_den_trang = tk.Button(frame_nhap_trang, text="Đi Đến", command=den_trang)
btn_den_trang.pack(side=tk.LEFT, padx=10)

# Hiển thị trang đầu tiên
hien_thi_du_lieu(trang_hien_tai)

# Thiết lập kích thước cửa sổ để đủ không gian cho Treeview
window.geometry("1200x800")  # Cập nhật kích thước cửa sổ lớn hơn nếu cần

window.mainloop()
