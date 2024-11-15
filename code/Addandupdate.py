import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Đường dẫn file CSV
file_path = '../data/dataset/data.csv'
data = pd.read_csv(file_path)

# Khởi tạo cửa sổ tkinter
window = tk.Tk()
window.title("Quản lý Dữ Liệu")

# Khởi tạo Treeview
cols = list(data.columns)
tree = ttk.Treeview(window, columns=cols, show='headings', height=15)

# Cập nhật độ rộng cho các cột sao cho phù hợp
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=80, anchor='center', minwidth=60)

tree.pack(expand=True, fill=tk.BOTH)

# Hàm hiển thị dữ liệu trong Treeview
def hien_thi_du_lieu():
    for row in tree.get_children():
        tree.delete(row)
    
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

hien_thi_du_lieu()

# Tạo các ô nhập liệu cho Trang "Tạo dữ liệu mới"
frame_tao_du_lieu_moi = tk.Frame(window)
frame_tao_du_lieu_moi.pack(pady=10)

entry_id_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_id_create.pack(side=tk.LEFT, padx=5)

entry_no_pation_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_no_pation_create.pack(side=tk.LEFT, padx=5)

entry_gender_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_gender_create.pack(side=tk.LEFT, padx=5)

entry_age_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_age_create.pack(side=tk.LEFT, padx=5)

entry_urea_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_urea_create.pack(side=tk.LEFT, padx=5)

entry_cr_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_cr_create.pack(side=tk.LEFT, padx=5)

entry_hba1c_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_hba1c_create.pack(side=tk.LEFT, padx=5)

entry_chol_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_chol_create.pack(side=tk.LEFT, padx=5)

entry_tg_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_tg_create.pack(side=tk.LEFT, padx=5)

entry_hdl_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_hdl_create.pack(side=tk.LEFT, padx=5)

entry_ldl_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_ldl_create.pack(side=tk.LEFT, padx=5)

entry_vldl_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_vldl_create.pack(side=tk.LEFT, padx=5)

entry_bmi_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_bmi_create.pack(side=tk.LEFT, padx=5)

entry_class_create = tk.Entry(frame_tao_du_lieu_moi, width=10)
entry_class_create.pack(side=tk.LEFT, padx=5)

# Nút "Tạo dữ liệu mới"
def tao_du_lieu_moi():
    try:
        new_data = [
            entry_id_create.get(), entry_no_pation_create.get(), entry_gender_create.get(), entry_age_create.get(),
            entry_urea_create.get(), entry_cr_create.get(), entry_hba1c_create.get(), entry_chol_create.get(),
            entry_tg_create.get(), entry_hdl_create.get(), entry_ldl_create.get(), entry_vldl_create.get(),
            entry_bmi_create.get(), entry_class_create.get()
        ]
        
        if any(field == "" for field in new_data):
            messagebox.showwarning("Dữ liệu không hợp lệ", "Vui lòng điền đầy đủ thông tin!")
            return
        
        # Thêm dữ liệu vào DataFrame
        data.loc[len(data)] = new_data
        tree.insert("", "end", values=new_data)

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được tạo mới!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tạo dữ liệu mới: {e}")

btn_tao_du_lieu = tk.Button(frame_tao_du_lieu_moi, text="Tạo dữ liệu mới", command=tao_du_lieu_moi)
btn_tao_du_lieu.pack(side=tk.LEFT, padx=10)

# Tạo các ô nhập liệu cho Trang "Cập nhật dữ liệu được chọn"
frame_cap_nhat_du_lieu = tk.Frame(window)

entry_id_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_id_update.pack(side=tk.LEFT, padx=5)

entry_no_pation_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_no_pation_update.pack(side=tk.LEFT, padx=5)

entry_gender_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_gender_update.pack(side=tk.LEFT, padx=5)

entry_age_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_age_update.pack(side=tk.LEFT, padx=5)

entry_urea_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_urea_update.pack(side=tk.LEFT, padx=5)

entry_cr_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_cr_update.pack(side=tk.LEFT, padx=5)

entry_hba1c_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_hba1c_update.pack(side=tk.LEFT, padx=5)

entry_chol_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_chol_update.pack(side=tk.LEFT, padx=5)

entry_tg_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_tg_update.pack(side=tk.LEFT, padx=5)

entry_hdl_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_hdl_update.pack(side=tk.LEFT, padx=5)

entry_ldl_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_ldl_update.pack(side=tk.LEFT, padx=5)

entry_vldl_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_vldl_update.pack(side=tk.LEFT, padx=5)

entry_bmi_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_bmi_update.pack(side=tk.LEFT, padx=5)

entry_class_update = tk.Entry(frame_cap_nhat_du_lieu, width=10)
entry_class_update.pack(side=tk.LEFT, padx=5)

# Nút "Cập nhật"
def cap_nhat_du_lieu():
    try:
        updated_data = [
            entry_id_update.get(), entry_no_pation_update.get(), entry_gender_update.get(), entry_age_update.get(),
            entry_urea_update.get(), entry_cr_update.get(), entry_hba1c_update.get(), entry_chol_update.get(),
            entry_tg_update.get(), entry_hdl_update.get(), entry_ldl_update.get(), entry_vldl_update.get(),
            entry_bmi_update.get(), entry_class_update.get()
        ]
        
        if any(field == "" for field in updated_data):
            messagebox.showwarning("Dữ liệu không hợp lệ", "Vui lòng điền đầy đủ thông tin!")
            return
        
        # Lấy dòng được chọn trong Treeview
        selected_item = tree.selection()[0]
        index = tree.index(selected_item)

        # Cập nhật dữ liệu vào DataFrame
        for i, value in enumerate(updated_data):
            data.iloc[index, i] = value

        # Cập nhật Treeview
        tree.item(selected_item, values=updated_data)

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được cập nhật!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể cập nhật dữ liệu: {e}")

btn_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Cập nhật", command=cap_nhat_du_lieu)
btn_cap_nhat.pack(side=tk.LEFT, padx=10)

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

# Hiển thị cửa sổ
window.mainloop()
