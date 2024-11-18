import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Đường dẫn file CSV
file_path = 'CLEAN.csv'
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
        hien_thi_du_lieu()  # Cập nhật Treeview với dữ liệu mới
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể xóa dữ liệu: {e}")

btn_xoa_du_lieu_moi = tk.Button(frame_tao_du_lieu_moi, text="Xóa dữ liệu", command=xoa_du_lieu_moi)
btn_xoa_du_lieu_moi.pack(side=tk.LEFT, padx=10)

# Tạo Frame tìm kiếm 
frame_tim_kiem = tk.Frame(window)
frame_tim_kiem.pack(pady=10)

lbl_tim_kiem = tk.Label(frame_tim_kiem, text="Tìm kiếm theo ID: ")
lbl_tim_kiem.pack(side=tk.LEFT, padx=5)

entry_tim_kiem = tk.Entry(frame_tim_kiem, width=10)
entry_tim_kiem.pack(side=tk.LEFT, padx=5)
# Hàm tìm kiếm theo ID
def tim_kiem_theo_id():
    data['ID'] = data['ID'].astype(str)
    data['ID'] = data['ID'].str.strip()
    try:
        id_tra_cuu = entry_tim_kiem.get().strip()  # Lấy giá trị ID từ ô nhập liệu
        if id_tra_cuu == "":
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập ID cần tìm!")
            return

        # Kiểm tra xem ID có tồn tại trong DataFrame không
        ket_qua_tim_kiem = data[data['ID'] == id_tra_cuu]

        if ket_qua_tim_kiem.empty:
            messagebox.showinfo("Không tìm thấy", f"Không tìm thấy dữ liệu với ID = {id_tra_cuu}")
        else:
            # Hiển thị kết quả tìm kiếm trong Treeview
            for row in tree.get_children():
                tree.delete(row)

            # Chỉ hiển thị dữ liệu của dòng có ID tìm được
            for _, row in ket_qua_tim_kiem.iterrows():
                tree.insert("", "end", values=list(row))

            messagebox.showinfo("Tìm thấy", f"Tìm thấy dữ liệu với ID = {id_tra_cuu}")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi trong quá trình tìm kiếm: {e}")

btn_tim_kiem = tk.Button(frame_tim_kiem, text="Tìm kiếm", command=lambda: tim_kiem_theo_id())
btn_tim_kiem.pack(side=tk.LEFT, padx=5)



# Tao frame sắp xếp dữ liệu theo ID
frame_sap_xep_du_lieu_theo_id = tk.Frame(window)
frame_sap_xep_du_lieu_theo_id.pack(pady=10)
# Nut sap xep tang dan
def sap_xep_tang_dan():
    global data
    try:
        data['ID'] = data['ID'].astype(int) # chuyển tạm về int để sort
        data.sort_values(by='ID', inplace=True, ascending=True)  # Sắp xếp tăng dần theo cột 'ID'
        data['ID'] = data['ID'].astype(str)
        data.reset_index(drop=True, inplace=True)  # Đặt lại chỉ số sau khi sắp xếp
        hien_thi_du_lieu()  # Hiển thị dữ liệu đã sắp xếp
        messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp tăng dần!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")
btn_sap_xep_tang_dan = tk.Button(frame_sap_xep_du_lieu_theo_id, text="Sắp xếp tăng dần", command=sap_xep_tang_dan)
btn_sap_xep_tang_dan.pack(side=tk.LEFT, padx=10)
# Nut sap xep giam dan
def sap_xep_giam():
    global data
    try:
        data['ID'] = data['ID'].astype(int) # Chuyển tạm về float để sort
        data.sort_values(by='ID', inplace=True, ascending=False)  # Sắp xếp giảm dần theo cột 'ID'
        data['ID'] = data['ID'].astype(str) # chuyển ngc lại str
        data.reset_index(drop=True, inplace=True)  # Đặt lại chỉ số sau khi sắp xếp
        hien_thi_du_lieu()  # Hiển thị dữ liệu đã sắp xếp
        messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp giảm dần!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

btn_sap_xep_giam = tk.Button(frame_sap_xep_du_lieu_theo_id, text="Sắp xếp giảm dần", command=sap_xep_giam)
btn_sap_xep_giam.pack(side=tk.LEFT, padx=5)
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
        messagebox.showerror("lỗi", f"Dữ liệu đã không được cập nhật! {e}")

btn_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Cập nhật", command=cap_nhat_du_lieu)
btn_cap_nhat.pack(side=tk.LEFT, padx=10)

# Nút "Xóa dữ liệu" cho trang "Cập nhật dữ liệu"
def xoa_du_lieu_cap_nhat():
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
        hien_thi_du_lieu()  # Cập nhật Treeview với dữ liệu mới
    except Exception as e:
        messagebox.showerror("Thành công", f"Dữ liệu đã không được cập nhật! {e}")

btn_xoa_du_lieu_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Xóa dữ liệu", command=xoa_du_lieu_cap_nhat)
btn_xoa_du_lieu_cap_nhat.pack(side=tk.LEFT, padx=10)

# Tạo các nút chuyển trang nằm phía bên trái
frame_nut_chuyen_trang = tk.Frame(window)
frame_nut_chuyen_trang.pack(side=tk.LEFT, padx=10, pady=10)

btn_create_page = tk.Button(frame_nut_chuyen_trang, text="Tạo dữ liệu mới", command=lambda: show_page('create'))
btn_create_page.pack(side=tk.LEFT, pady=5, padx=5)  # Khoảng cách đều trên-dưới và trái-phải

btn_sort_page = tk.Button(frame_nut_chuyen_trang, text="Sắp xếp dữ liệu", command=lambda: show_page('sort'))
btn_sort_page.pack(side=tk.LEFT, pady=5, padx=5)  # Cùng cách xếp trên-dưới

btn_update_page = tk.Button(frame_nut_chuyen_trang, text="Cập nhật dữ liệu", command=lambda: show_page('update'))
btn_update_page.pack(side=tk.LEFT, pady=5, padx=5)

btn_tim_kiem = tk.Button(frame_nut_chuyen_trang,text="Tìm kiếm dữ liệu",command=lambda: show_page('search'))
btn_tim_kiem.pack(side=tk.LEFT,pady=5,padx=5)

# Tạo Frame cho trích lọc
frame_trich_loc = tk.Frame(window)

# Nhãn chọn loại trích lọc
lbl_trich_loc = tk.Label(frame_trich_loc, text="Chọn loại trích lọc: ")
lbl_trich_loc.pack(side=tk.LEFT, padx=5)

# Biến lưu lựa chọn loại trích lọc
trich_loc_option = tk.StringVar(value="Gender")  # Giá trị mặc định là Gender

# Radiobutton cho Gender
radio_gender = tk.Radiobutton(frame_trich_loc, text="Gender", variable=trich_loc_option, value="Gender")
radio_gender.pack(side=tk.LEFT, padx=5)

# Radiobutton cho CLASS
radio_class = tk.Radiobutton(frame_trich_loc, text="CLASS", variable=trich_loc_option, value="CLASS")
radio_class.pack(side=tk.LEFT, padx=5)

# Nhãn và ô nhập giá trị lọc
lbl_value = tk.Label(frame_trich_loc, text="Nhập giá trị: ")
lbl_value.pack(side=tk.LEFT, padx=5)

entry_value = tk.Entry(frame_trich_loc, width=10)
entry_value.pack(side=tk.LEFT, padx=5)

# Hàm trích lọc
def trich_loc():
    global data
    try:
        # Lấy loại trích lọc và giá trị nhập vào
        selected_filter = trich_loc_option.get()  # "Gender" hoặc "CLASS"
        filter_value = entry_value.get().strip().lower()

        if not filter_value:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập giá trị để lọc!")
            return

        # Kiểm tra giá trị hợp lệ dựa trên loại trích lọc
        valid_values = {"Gender": ["m", "f"], "CLASS": ["n", "y", "p"]}
        if filter_value not in valid_values[selected_filter]:
            messagebox.showwarning("Cảnh báo", f"Giá trị {filter_value} không hợp lệ cho {selected_filter}!")
            return

        # Lọc dữ liệu
        filtered_data = data[data[selected_filter].str.lower() == filter_value]

        # Hiển thị dữ liệu đã lọc trên Treeview
        if filtered_data.empty:
            messagebox.showinfo("Không tìm thấy", "Không có dữ liệu phù hợp với bộ lọc.")
        else:
            # Cập nhật Treeview với dữ liệu đã lọc
            update_filtered_data(filtered_data)
            messagebox.showinfo("Thành công", f"Đã lọc dữ liệu theo {selected_filter} = {filter_value}!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# Nút Lọc
btn_trich_loc = tk.Button(frame_trich_loc, text="Lọc dữ liệu", command=trich_loc)
btn_trich_loc.pack(side=tk.LEFT, padx=10)

# Hàm hiển thị dữ liệu lọc với hỗ trợ phân trang
filtered_data = pd.DataFrame()  # DataFrame để lưu dữ liệu đã lọc
filtered_page = 0  # Trang hiện tại cho dữ liệu lọc

def update_filtered_data(new_data):
    global filtered_data, filtered_page
    filtered_data = new_data.reset_index(drop=True)  # Cập nhật dữ liệu đã lọc
    filtered_page = 0  # Đặt lại trang về 0
    hien_thi_du_lieu_loc()

def hien_thi_du_lieu_loc():
    global filtered_data, filtered_page
    for row in tree.get_children():
        tree.delete(row)

    # Tính toán chỉ số bắt đầu và kết thúc cho trang hiện tại
    start_index = filtered_page * ROWS_PER_PAGE
    end_index = start_index + ROWS_PER_PAGE
    paginated_data = filtered_data.iloc[start_index:end_index]

    for _, row in paginated_data.iterrows():
        tree.insert("", "end", values=list(row))

    update_filtered_page_info()

def update_filtered_page_info():
    total_pages = (len(filtered_data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE
    lbl_page_info.config(text=f"Trang {filtered_page + 1} / {total_pages}")

# Nút điều hướng cho dữ liệu lọc
def filtered_page_previous():
    global filtered_page
    if filtered_page > 0:
        filtered_page -= 1
        hien_thi_du_lieu_loc()

def filtered_page_next():
    global filtered_page
    if filtered_page < (len(filtered_data) // ROWS_PER_PAGE):
        filtered_page += 1
        hien_thi_du_lieu_loc()

btn_previous.config(command=filtered_page_previous)
btn_next.config(command=filtered_page_next)


btn_trich_loc = tk.Button(frame_nut_chuyen_trang,text="Trích lọc",command=lambda :show_page('filter'))
btn_trich_loc.pack(side=tk.LEFT,pady=5,padx=5)


frame_tim_kiem.pack_forget()
frame_tao_du_lieu_moi.pack_forget()
frame_cap_nhat_du_lieu.pack_forget()
frame_sap_xep_du_lieu_theo_id.pack_forget()
frame_trich_loc.pack_forget()

#Hiển thị trang dữ liệu
def show_page(page_type):
    frame_cap_nhat_du_lieu.pack_forget()
    frame_sap_xep_du_lieu_theo_id.pack_forget()
    frame_tao_du_lieu_moi.pack_forget()
    frame_tim_kiem.pack_forget()
    frame_trich_loc.pack_forget()


    if page_type == 'create':
        frame_tao_du_lieu_moi.pack(pady=10)
    elif page_type == 'update':
        frame_cap_nhat_du_lieu.pack(pady=10)
    elif page_type == 'sort':
        frame_sap_xep_du_lieu_theo_id.pack(pady=10)
    elif page_type == 'search':
        frame_tim_kiem.pack(pady= 10)
    elif page_type == 'filter':
        frame_trich_loc.pack(pady=10)
# Hiển thị dữ liệu ban đầu
hien_thi_du_lieu()

# Hiển thị cửa sổ
window.mainloop()
