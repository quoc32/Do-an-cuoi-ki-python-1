import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Đường dẫn file CSV (thay đổi đường dẫn nếu cần)
file_path = "../data/clean.csv"
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
    global current_page
    for row in tree.get_children():
        tree.delete(row)

    # Tính toán chỉ số bắt đầu và kết thúc cho trang hiện tại
    start_index = current_page * ROWS_PER_PAGE
    end_index = start_index + ROWS_PER_PAGE
    paginated_data = data.iloc[start_index:end_index]

    for _, row in paginated_data.iterrows():
        tree.insert("", "end", values=list(row))

    # Cập nhật thông tin trang
    update_page_info()

# Cập nhật thông tin cho các nút điều hướng
def update_page_info():
    total_pages = (len(data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE  # Tính toán tổng số trang
    lbl_page_info.config(text=f"Trang {current_page + 1} / {total_pages}")

# Khung cho các nút chức năng
frame_nut_chuc_nang = tk.Frame(window)
frame_nut_chuc_nang.pack(side=tk.TOP, padx=10, pady=10)

# Nút Tạo Dữ Liệu Mới
def show_create_page():
    frame_tao_du_lieu_moi.pack(pady=10)
    frame_cap_nhat_du_lieu.pack_forget()
    frame_tim_kiem.pack_forget()
    frame_sap_xep_du_lieu_theo_id.pack_forget()
    frame_trich_loc.pack_forget()
    frame_xoa_du_lieu.pack_forget()

    # Làm sạch các ô nhập liệu
    for col in cols:
        inputs[col].delete(0, tk.END)

    # Tự động điền ID
    if 'ID' in cols:
        max_id = data['ID'].astype(int).max()
        inputs['ID'].insert(0, str(max_id + 1))

btn_create_page = tk.Button(frame_nut_chuc_nang, text="Tạo dữ liệu mới", command=show_create_page)
btn_create_page.pack(side=tk.LEFT, padx=5)

# Nút Cập Nhật Dữ Liệu
def show_update_page():
    frame_cap_nhat_du_lieu.pack(pady=10)
    frame_tao_du_lieu_moi.pack_forget()
    frame_tim_kiem.pack_forget()
    frame_sap_xep_du_lieu_theo_id.pack_forget()
    frame_trich_loc.pack_forget()
    frame_xoa_du_lieu.pack_forget()

    # Lấy dòng được chọn
    selected_items = tree.selection()
    if selected_items:
        selected_item = selected_items[0]
        index = tree.index(selected_item)
        selected_data = data.iloc[index]

        # Điền dữ liệu vào các ô nhập liệu
        for col in cols:
            update_inputs[col].delete(0, tk.END)
            update_inputs[col].insert(0, selected_data[col])

btn_update_page = tk.Button(frame_nut_chuc_nang, text="Cập nhật dữ liệu", command=show_update_page)
btn_update_page.pack(side=tk.LEFT, padx=5)

# Nút Xóa Dữ Liệu
def show_delete_page():
    frame_cap_nhat_du_lieu.pack_forget()
    frame_tao_du_lieu_moi.pack_forget()
    frame_tim_kiem.pack_forget()
    frame_sap_xep_du_lieu_theo_id.pack_forget()
    frame_trich_loc.pack_forget()
    frame_xoa_du_lieu.pack(pady=10)

btn_delete_page = tk.Button(frame_nut_chuc_nang, text="Xóa dữ liệu", command=show_delete_page)
btn_delete_page.pack(side=tk.LEFT, padx=5)

# Khung cho Xóa Dữ Liệu
frame_xoa_du_lieu = tk.Frame(window)

# Nút "Xóa"
def xoa_du_lieu():
    try:
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để xóa!")
            return

        # Lưu lại các chỉ số của các dòng đã chọn để xóa sau
        indices_to_drop = [tree.index(item) for item in selected_items]

        # Xóa dữ liệu từ Treeview
        for item in selected_items:
            tree.delete(item)

        # Loại bỏ các chỉ số đã chọn từ DataFrame
        data.drop(data.index[indices_to_drop], inplace=True)

        # Đặt lại chỉ số cho DataFrame
        data.reset_index(drop=True, inplace=True)

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được xóa!")
        hien_thi_du_lieu()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xóa dữ liệu: {e}")

# Nút Xóa
btn_xoa_du_lieu = tk.Button(frame_xoa_du_lieu, text="Xóa", command=xoa_du_lieu)
btn_xoa_du_lieu.pack(padx=5)

# Nút Tìm Kiếm
def show_search_page():
    frame_tim_kiem.pack(pady=10)
    frame_tao_du_lieu_moi.pack_forget()
    frame_cap_nhat_du_lieu.pack_forget()
    frame_sap_xep_du_lieu_theo_id.pack_forget()
    frame_trich_loc.pack_forget()
    frame_xoa_du_lieu.pack_forget()

btn_search_page = tk.Button(frame_nut_chuc_nang, text="Tìm kiếm", command=show_search_page)
btn_search_page.pack(side=tk.LEFT, padx=5)

# Nút Sắp Xếp
def show_sort_page():
    frame_sap_xep_du_lieu_theo_id.pack(pady=10)
    frame_tao_du_lieu_moi.pack_forget()
    frame_cap_nhat_du_lieu.pack_forget()
    frame_tim_kiem.pack_forget()
    frame_trich_loc.pack_forget()
    frame_xoa_du_lieu.pack_forget()

btn_sort_page = tk.Button(frame_nut_chuc_nang, text="Sắp xếp", command=show_sort_page)
btn_sort_page.pack(side=tk.LEFT, padx=5)

# Nút chuyển đến trang lọc dữ liệu
def show_filter_page():
    frame_tao_du_lieu_moi.pack_forget()
    frame_cap_nhat_du_lieu.pack_forget()
    frame_tim_kiem.pack_forget()
    frame_sap_xep_du_lieu_theo_id.pack_forget()
    frame_xoa_du_lieu.pack_forget()
    frame_trich_loc.pack(pady=10)

btn_filter_page = tk.Button(frame_nut_chuc_nang, text="Lọc dữ liệu", command=show_filter_page)
btn_filter_page.pack(side=tk.LEFT, padx=5)

# Khung cho các nút điều hướng
frame_nut_chuyen_trang = tk.Frame(window)
frame_nut_chuyen_trang.pack(side=tk.BOTTOM, padx=10, pady=10)

# Nút Home
def go_home():
    global current_page
    current_page = 0
    hien_thi_du_lieu()

btn_home = tk.Button(frame_nut_chuyen_trang, text="Home", command=go_home)
btn_home.pack(side=tk.LEFT, padx=5)

# Hàm để chuyển đến trang trước
def page_previous():
    global current_page
    if current_page > 0:
        current_page -= 1
        hien_thi_du_lieu()

# Nút trang trước
btn_previous = tk.Button(frame_nut_chuyen_trang, text="Trang trước", command=page_previous)
btn_previous.pack(side=tk.LEFT, padx=5)

# Nhãn hiển thị thông tin trang
lbl_page_info = tk.Label(frame_nut_chuyen_trang)
lbl_page_info.pack(side=tk.LEFT, padx=5)

# Ô nhập số trang
entry_page_number = tk.Entry(frame_nut_chuyen_trang, width=5)
entry_page_number.pack(side=tk.LEFT, padx=5)

# Nút nhảy đến trang
def go_to_page():
    global current_page
    try:
        page = int(entry_page_number.get())
        total_pages = (len(data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE
        if 1 <= page <= total_pages:
            current_page = page - 1
            hien_thi_du_lieu()
        else:
            messagebox.showwarning("Cảnh báo", "Trang không hợp lệ!")
    except ValueError:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập số trang hợp lệ!")

btn_go_to_page = tk.Button(frame_nut_chuyen_trang, text="Đến trang", command=go_to_page)
btn_go_to_page.pack(side=tk.LEFT, padx=5)

# Hàm để chuyển đến trang sau
def page_next():
    global current_page
    total_pages = (len(data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE
    if (current_page + 1) < total_pages:
        current_page += 1
        hien_thi_du_lieu()

# Nút trang sau
btn_next = tk.Button(frame_nut_chuyen_trang, text="Trang sau", command=page_next)
btn_next.pack(side=tk.LEFT, padx=5)

# Khởi tạo khung cho Tạo Dữ Liệu Mới
frame_tao_du_lieu_moi = tk.Frame(window)

# Thêm tiêu đề cho các cột
header_frame_create = tk.Frame(frame_tao_du_lieu_moi)
header_frame_create.pack(side=tk.TOP)

inputs = {}
for col in cols:
    label = tk.Label(header_frame_create, text=col, width=10)
    label.pack(side=tk.LEFT)
    
    entry = tk.Entry(frame_tao_du_lieu_moi, width=10)
    entry.pack(side=tk.LEFT, padx=5)
    inputs[col] = entry

# Tự động điền ID
if 'ID' in cols:
    max_id = data['ID'].astype(int).max()
    inputs['ID'].insert(0, str(max_id + 1))

# Nút "Tạo dữ liệu mới"
def tao_du_lieu_moi():
    try:
        new_data = [inputs[col].get() for col in cols]
        
        if any(field == "" for field in new_data):
            messagebox.showwarning("Dữ liệu không hợp lệ", "Vui lòng điền đầy đủ thông tin!")
            return
        
        # Thêm dữ liệu vào DataFrame
        data.loc[len(data)] = new_data
        hien_thi_du_lieu()

        # Lưu lại dữ liệu vào file CSV
        data.to_csv(file_path, index=False)
        messagebox.showinfo("Thành công", "Dữ liệu đã được tạo mới!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tạo dữ liệu mới: {e}")

btn_tao_du_lieu = tk.Button(frame_tao_du_lieu_moi, text="Tạo", command=tao_du_lieu_moi)
btn_tao_du_lieu.pack(side=tk.LEFT, padx=10)

# Khung cho Cập Nhật Dữ Liệu
frame_cap_nhat_du_lieu = tk.Frame(window)

# Thêm tiêu đề cho các cột
header_frame_update = tk.Frame(frame_cap_nhat_du_lieu)
header_frame_update.pack(side=tk.TOP)

update_inputs = {}
for col in cols:
    label = tk.Label(header_frame_update, text=col, width=10)
    label.pack(side=tk.LEFT)
    
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
        messagebox.showerror("Lỗi", f"Dữ liệu đã không được cập nhật! {e}")

btn_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Nhập", command=cap_nhat_du_lieu)
btn_cap_nhat.pack(side=tk.LEFT, padx=10)

# Tìm kiếm
frame_tim_kiem = tk.Frame(window)

lbl_tim_kiem = tk.Label(frame_tim_kiem, text="Tìm kiếm theo ID: ")
lbl_tim_kiem.pack(side=tk.LEFT, padx=5)

entry_tim_kiem = tk.Entry(frame_tim_kiem, width=10)
entry_tim_kiem.pack(side=tk.LEFT, padx=5)

# Hàm tìm kiếm theo ID
def tim_kiem_theo_id():
    global current_page
    try:
        id_tra_cuu = entry_tim_kiem.get().strip()
        if id_tra_cuu == "":
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID cần tìm!")
            return

        # Kiểm tra xem ID có tồn tại trong DataFrame không
        ket_qua_tim_kiem = data[data['ID'].astype(str).str.strip() == id_tra_cuu]

        if ket_qua_tim_kiem.empty:
            messagebox.showinfo("Không tìm thấy", f"Không tìm thấy dữ liệu với ID = {id_tra_cuu}")
        else:
            # Hiển thị tất cả dữ liệu tìm được trong Treeview
            for row in tree.get_children():
                tree.delete(row)

            # Chỉ hiển thị dữ liệu của dòng có ID tìm được
            for _, row in ket_qua_tim_kiem.iterrows():
                tree.insert("", "end", values=list(row))

            # Đặt current_page về 0 để không bị ảnh hưởng khi quay lại
            current_page = 0  
            update_page_info()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi trong quá trình tìm kiếm: {e}")

btn_tim_kiem = tk.Button(frame_tim_kiem, text="Tìm kiếm", command=tim_kiem_theo_id)
btn_tim_kiem.pack(side=tk.LEFT, padx=5)

# Tạo frame sắp xếp dữ liệu theo ID
frame_sap_xep_du_lieu_theo_id = tk.Frame(window)

# Nút sắp xếp tăng dần
def sap_xep_tang_dan():
    global data
    try:
        data['ID'] = data['ID'].astype(int)
        data.sort_values(by='ID', inplace=True, ascending=True)
        data['ID'] = data['ID'].astype(str)
        data.reset_index(drop=True, inplace=True)
        hien_thi_du_lieu()
        messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp tăng dần!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

btn_sap_xep_tang_dan = tk.Button(frame_sap_xep_du_lieu_theo_id, text="Sắp xếp tăng dần", command=sap_xep_tang_dan)
btn_sap_xep_tang_dan.pack(side=tk.LEFT, padx=10)

# Nút sắp xếp giảm dần
def sap_xep_giam():
    global data
    try:
        data['ID'] = data['ID'].astype(int)
        data.sort_values(by='ID', inplace=True, ascending=False)
        data['ID'] = data['ID'].astype(str)
        data.reset_index(drop=True, inplace=True)
        hien_thi_du_lieu()
        messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp giảm dần!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

btn_sap_xep_giam = tk.Button(frame_sap_xep_du_lieu_theo_id, text="Sắp xếp giảm dần", command=sap_xep_giam)
btn_sap_xep_giam.pack(side=tk.LEFT, padx=10)

# Tạo frame cho Trang "Lọc dữ liệu"
frame_trich_loc = tk.Frame(window)

# Nhãn chọn loại trích lọc
lbl_trich_loc = tk.Label(frame_trich_loc, text="Lọc dữ liệu theo:")
lbl_trich_loc.pack(side=tk.TOP, padx=5)

# Khung cho bộ lọc
filter_frame = tk.Frame(frame_trich_loc)
filter_frame.pack(side=tk.TOP)

# Duyệt từng đặc tính để lấy dữ liệu cho combobox
gender_options = data['Gender'].unique().tolist()
class_options = data['CLASS'].unique().tolist()
bmi_category_options = data['BMI_CATEGORY'].unique().tolist()

# Nhãn và ô combobox cho giá trị lọc
lbl_gender = tk.Label(filter_frame, text="Gender:")
lbl_gender.pack(side=tk.LEFT, padx=5)
combo_gender = ttk.Combobox(filter_frame, values=gender_options, width=10)
combo_gender.pack(side=tk.LEFT, padx=5)

lbl_class = tk.Label(filter_frame, text="CLASS:")
lbl_class.pack(side=tk.LEFT, padx=5)
combo_class = ttk.Combobox(filter_frame, values=class_options, width=10)
combo_class.pack(side=tk.LEFT, padx=5)

lbl_bmi_category = tk.Label(filter_frame, text="BMI CATEGORY:")
lbl_bmi_category.pack(side=tk.LEFT, padx=5)
combo_bmi_category = ttk.Combobox(filter_frame, values=bmi_category_options, width=10)
combo_bmi_category.pack(side=tk.LEFT, padx=5)

# Nút Lọc dữ liệu
btn_trich_loc = tk.Button(filter_frame, text="Lọc dữ liệu", command=lambda: trich_loc(combo_gender.get(), combo_class.get(), combo_bmi_category.get()))
btn_trich_loc.pack(side=tk.LEFT, padx=10)

# Hàm lọc dữ liệu
def trich_loc(gender, class_val, bmi_category):
    global current_page
    try:
        # Lọc dữ liệu dựa trên các tiêu chí đã nhập
        filtered_data = data

        if gender:
            filtered_data = filtered_data[filtered_data['Gender'] == gender]

        if class_val:
            filtered_data = filtered_data[filtered_data['CLASS'] == class_val]

        if bmi_category:
            filtered_data = filtered_data[filtered_data['BMI_CATEGORY'] == bmi_category]

        # Hiển thị dữ liệu đã lọc trên Treeview
        for row in tree.get_children():
            tree.delete(row)

        if filtered_data.empty:
            messagebox.showinfo("Không tìm thấy", "Không có dữ liệu phù hợp với bộ lọc.")
        else:
            for _, row in filtered_data.iterrows():
                tree.insert("", "end", values=list(row))
            current_page = 0
            update_page_info()

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# Ẩn tất cả các khung trừ khung hiển thị dữ liệu
frame_tao_du_lieu_moi.pack_forget()
frame_cap_nhat_du_lieu.pack_forget()
frame_tim_kiem.pack_forget()
frame_sap_xep_du_lieu_theo_id.pack_forget()
frame_trich_loc.pack_forget()
frame_xoa_du_lieu.pack_forget()

# Hiển thị trang dữ liệu
hien_thi_du_lieu()

# Hiển thị cửa sổ
window.mainloop()