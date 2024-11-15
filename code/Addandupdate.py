import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Đường dẫn file CSV
file_path = '../data/dataset/data.csv'
data = pd.read_csv(file_path)

# Khởi tạo cửa sổ tkinter
window = tk.Tk()
window.title("Quản lý Dữ Liệu")

# Số dòng trên mỗi trang
ROWS_PER_PAGE = 30
current_page = 0

# Khởi tạo Treeview
cols = list(data.columns)
tree = ttk.Treeview(window, columns=cols, show='headings', height=ROWS_PER_PAGE)

# Cập nhật độ rộng cho các cột
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=80, anchor='center', minwidth=60)

tree.pack(expand=True, fill=tk.BOTH)

# Hàm hiển thị dữ liệu trong Treeview dựa trên trang hiện tại
def hien_thi_du_lieu():
    for row in tree.get_children():
        tree.delete(row)

    # Tính toán chỉ số bắt đầu và kết thúc cho trang hiện tại
    start_index = current_page * ROWS_PER_PAGE
    end_index = start_index + ROWS_PER_PAGE
    paginated_data = data.iloc[start_index:end_index]

    for _, row in paginated_data.iterrows():
        tree.insert("", "end", values=list(row))

    # Cập nhật nút để điều hướng
    update_page_info()

# Cập nhật thông tin cho các nút điều hướng
def update_page_info():
    total_pages = (len(data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE  # Tính toán tổng số trang
    lbl_page_info.config(text=f"Trang {current_page + 1} / {total_pages}")

# Chuyển đến trang trước
def page_previous():
    global current_page
    if current_page > 0:
        current_page -= 1
        hien_thi_du_lieu()

# Chuyển đến trang sau
def page_next():
    global current_page
    if current_page < (len(data) // ROWS_PER_PAGE):
        current_page += 1
        hien_thi_du_lieu()

# Chuyển đến trang cụ thể
def go_to_page():
    global current_page
    try:
        page_num = int(entry_page.get()) - 1  # Chuyển đổi từ 1-indexed sang 0-indexed
        if page_num < 0 or page_num > (len(data) // ROWS_PER_PAGE):
            messagebox.showerror("Cảnh báo", "Số trang không hợp lệ!")
        else:
            current_page = page_num
            hien_thi_du_lieu()
    except ValueError:
        messagebox.showerror("Cảnh báo", "Vui lòng nhập một số hợp lệ!")

# Nút điều hướng
frame_navigation = tk.Frame(window)
frame_navigation.pack(pady=10)

btn_previous = tk.Button(frame_navigation, text="Trang trước", command=page_previous)
btn_previous.pack(side=tk.LEFT, padx=5)

lbl_page_info = tk.Label(frame_navigation, text="")
lbl_page_info.pack(side=tk.LEFT, padx=5)

entry_page = tk.Entry(frame_navigation, width=5)
entry_page.pack(side=tk.LEFT, padx=5)

btn_go = tk.Button(frame_navigation, text="Đến trang", command=go_to_page)
btn_go.pack(side=tk.LEFT, padx=5)

btn_next = tk.Button(frame_navigation, text="Trang sau", command=page_next)
btn_next.pack(side=tk.LEFT, padx=5)

# Tạo các ô nhập liệu cho Trang "Tạo dữ liệu mới"
frame_tao_du_lieu_moi = tk.Frame(window)
frame_tao_du_lieu_moi.pack(pady=10)

inputs = {}
for col in cols:
    entry = tk.Entry(frame_tao_du_lieu_moi, width=10)
    entry.pack(side=tk.LEFT, padx=5)
    inputs[col] = entry

# Nút "Tạo dữ liệu mới"
def tao_du_lieu_moi():
    try:
        new_data = [inputs[col].get() for col in cols]

        if any(field == "" for field in new_data):
            messagebox.showwarning("Dữ liệu không hợp lệ", "Vui lòng điền đầy đủ thông tin!")
            return

        # Thêm dữ liệu vào DataFrame
        data.loc[len(data)] = new_data
        hien_thi_du_lieu()  # Cập nhật Treeview

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được tạo mới!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tạo dữ liệu mới: {e}")

btn_tao_du_lieu = tk.Button(frame_tao_du_lieu_moi, text="Tạo dữ liệu mới", command=tao_du_lieu_moi)
btn_tao_du_lieu.pack(side=tk.LEFT, padx=10)

# Nút "Xóa dữ liệu"
def xoa_du_lieu_moi():
    try:
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để xóa!")
            return

        for item in selected_items:
            tree.delete(item)

        # Cập nhật DataFrame bằng cách loại bỏ các dòng đã chọn
        indices_to_drop = [tree.index(item) for item in selected_items]
        data.drop(indices_to_drop, inplace=True)

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được xóa!")
        hien_thi_du_lieu()  # Cập nhật Treeview
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xóa dữ liệu: {e}")

btn_xoa_du_lieu_moi = tk.Button(frame_tao_du_lieu_moi, text="Xóa dữ liệu", command=xoa_du_lieu_moi)
btn_xoa_du_lieu_moi.pack(side=tk.LEFT, padx=10)

# Tạo các ô nhập liệu cho Trang "Cập nhật dữ liệu được chọn"
frame_cap_nhat_du_lieu = tk.Frame(window)

update_inputs = {}
for col in cols:
    entry = tk.Entry(frame_cap_nhat_du_lieu, width=10)
    entry.pack(side=tk.LEFT, padx=5)
    update_inputs[col] = entry

# Nút "Cập nhật"
def cap_nhat_du_lieu():
    try:
        updated_data = [update_inputs[col].get() for col in cols]

        if any(field == "" for field in updated_data):
            messagebox.showwarning("Dữ liệu không hợp lệ", "Vui lòng điền đầy đủ thông tin!")
            return

        # Lấy dòng được chọn trong Treeview
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để cập nhật!")
            return

        # Cập nhật dữ liệu cho từng dòng được chọn
        for selected_item in selected_items:
            index = tree.index(selected_item)
            for j in range(len(cols)):
                data.at[index, cols[j]] = updated_data[j]
                tree.item(selected_item, values=list(updated_data))

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được cập nhật!")
    except Exception as e:
        messagebox.showerror("Thành công", f"Dữ liệu đã được cập nhật! {e}")

btn_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Cập nhật", command=cap_nhat_du_lieu)
btn_cap_nhat.pack(side=tk.LEFT, padx=10)

# Nút "Xóa dữ liệu" cho trang "Cập nhật dữ liệu"
def xoa_du_lieu_cap_nhat():
    try:
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để xóa!")
            return

        for item in selected_items:
            tree.delete(item)

        # Cập nhật DataFrame bằng cách loại bỏ các dòng đã chọn
        indices_to_drop = [tree.index(item) for item in selected_items]
        data.drop(indices_to_drop, inplace=True)

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được xóa!")
        hien_thi_du_lieu()  # Cập nhật Treeview
    except Exception as e:
        messagebox.showerror("Thành công", f"Dữ liệu đã được cập nhật! {e}")

btn_xoa_du_lieu_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Xóa dữ liệu", command=xoa_du_lieu_cap_nhat)
btn_xoa_du_lieu_cap_nhat.pack(side=tk.LEFT, padx=10)

# Tạo các nút chuyển trang nằm phía bên trái
frame_nut_chuyen_trang = tk.Frame(window)
frame_nut_chuyen_trang.pack(side=tk.LEFT, padx=10, pady=10)

btn_create_page = tk.Button(frame_nut_chuyen_trang, text="Tạo dữ liệu mới", command=lambda: show_page('create'))
btn_create_page.pack(side=tk.TOP, padx=10)

btn_update_page = tk.Button(frame_nut_chuyen_trang, text="Cập nhật dữ liệu", command=lambda: show_page('update'))
btn_update_page.pack(side=tk.BOTTOM, padx=10)

# Hiển thị trang dữ liệu
def show_page(page_type):
    if page_type == 'create':
        frame_tao_du_lieu_moi.pack(pady=10)
        frame_cap_nhat_du_lieu.pack_forget()
    elif page_type == 'update':
        frame_cap_nhat_du_lieu.pack(pady=10)
        frame_tao_du_lieu_moi.pack_forget()

# Hiển thị dữ liệu ban đầu
hien_thi_du_lieu()

# Hiển thị cửa sổ
window.mainloop()
