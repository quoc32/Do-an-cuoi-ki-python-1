import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Đường dẫn file CSV (thay đổi đường dẫn nếu cần)
file_path = "../data/clean.csv"

# Số dòng trên mỗi trang
ROWS_PER_PAGE = 30
current_page = 0

# Khởi tạo DataFrame toàn cục
data = pd.read_csv(file_path)  # Đọc dữ liệu từ file CSV ngay khi bắt đầu

def main(frame=None):
    if frame:
        frame.toggleOnImg()

    # Khởi tạo cửa sổ tkinter
    window = tk.Tk()
    window.title("Quản lý Dữ Liệu")

    # Hàm xử lý khi đóng cửa sổ (Ẩn hình đi)
    def on_closing():
        if frame:
            frame.toggleOffImg()
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Khởi tạo Treeview
    global data
    cols = list(data.columns)
    tree = ttk.Treeview(window, columns=cols, show='headings', height=ROWS_PER_PAGE)

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=80, anchor='center', minwidth=60)

    tree.pack(expand=True, fill=tk.BOTH)

    # Hàm hiển thị dữ liệu trong Treeview dựa trên trang hiện tại
    def hien_thi_du_lieu():
        global current_page
        for row in tree.get_children():
            tree.delete(row)

        start_index = current_page * ROWS_PER_PAGE
        end_index = start_index + ROWS_PER_PAGE
        paginated_data = data.iloc[start_index:end_index]

        for _, row in paginated_data.iterrows():
            tree.insert("", "end", values=list(row))

        update_page_info()

    def update_page_info():
        total_pages = (len(data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE
        lbl_page_info.config(text=f"Trang {current_page + 1} / {total_pages}")

    frame_nut_chuc_nang = tk.Frame(window)
    frame_nut_chuc_nang.pack(side=tk.TOP, padx=10, pady=10)

    def show_create_page():
        frame_tao_du_lieu_moi.pack(pady=10)
        frame_cap_nhat_du_lieu.pack_forget()
        frame_tim_kiem.pack_forget()
        frame_sap_xep_du_lieu_theo_id.pack_forget()
        frame_trich_loc.pack_forget()
        frame_xoa_du_lieu.pack_forget()

        for col in cols:
            inputs[col].delete(0, tk.END)

        if 'ID' in cols:
            max_id = data['ID'].astype(int).max() if not data['ID'].isnull().all() else 0
            inputs['ID'].insert(0, str(max_id + 1))

    btn_create_page = tk.Button(frame_nut_chuc_nang, text="Tạo dữ liệu mới", command=show_create_page)
    btn_create_page.pack(side=tk.LEFT, padx=5)

    def show_update_page(event=None):
        frame_cap_nhat_du_lieu.pack(pady=10)
        frame_tao_du_lieu_moi.pack_forget()
        frame_tim_kiem.pack_forget()
        frame_sap_xep_du_lieu_theo_id.pack_forget()
        frame_trich_loc.pack_forget()
        frame_xoa_du_lieu.pack_forget()

        selected_items = tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            selected_data = tree.item(selected_item)['values']
            selected_id = selected_data[0]
            selected_row = data.loc[data['ID'] == selected_id].iloc[0]  # Lấy row tương ứng trong dataframe

            for col in cols:
                if col in ['Gender', 'CLASS', 'BMI_CATEGORY']:
                    update_inputs[col].set(selected_row[col])
                else:
                    update_inputs[col].delete(0, tk.END)
                    update_inputs[col].insert(0, selected_row[col])

    btn_update_page = tk.Button(frame_nut_chuc_nang, text="Cập nhật dữ liệu", command=show_update_page)
    btn_update_page.pack(side=tk.LEFT, padx=5)

    # Thêm sự kiện chọn hàng
    tree.bind("<<TreeviewSelect>>", show_update_page)

    def show_delete_page():
        frame_cap_nhat_du_lieu.pack_forget()
        frame_tao_du_lieu_moi.pack_forget()
        frame_tim_kiem.pack_forget()
        frame_sap_xep_du_lieu_theo_id.pack_forget()
        frame_trich_loc.pack_forget()
        frame_xoa_du_lieu.pack(pady=10)

    btn_delete_page = tk.Button(frame_nut_chuc_nang, text="Xóa dữ liệu", command=show_delete_page)
    btn_delete_page.pack(side=tk.LEFT, padx=5)

    frame_xoa_du_lieu = tk.Frame(window)

    def xoa_du_lieu():
        global data
        try:
            selected_items = tree.selection()
            if not selected_items:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để xóa!")
                return

            ids_to_delete = [tree.item(item)['values'][0] for item in selected_items]
            
            for item in selected_items:
                tree.delete(item)

            # Cập nhật DataFrame để xóa các dòng tương ứng
            data = data[~data['ID'].isin(ids_to_delete)]
            
            # Lưu dữ liệu vào file CSV sau khi xóa
            data.to_csv(file_path, index=False)
            
            messagebox.showinfo("Thành công", "Dữ liệu đã được xóa!")
            hien_thi_du_lieu()  # Cập nhật lại Treeview
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa dữ liệu: {e}")

    btn_xoa_du_lieu = tk.Button(frame_xoa_du_lieu, text="Xóa", command=xoa_du_lieu)
    btn_xoa_du_lieu.pack(padx=5)

    def show_search_page():
        frame_tim_kiem.pack(pady=10)
        frame_tao_du_lieu_moi.pack_forget()
        frame_cap_nhat_du_lieu.pack_forget()
        frame_sap_xep_du_lieu_theo_id.pack_forget()
        frame_xoa_du_lieu.pack_forget()
        frame_trich_loc.pack_forget()

    btn_search_page = tk.Button(frame_nut_chuc_nang, text="Tìm kiếm", command=show_search_page)
    btn_search_page.pack(side=tk.LEFT, padx=5)

    def show_sort_page():
        frame_sap_xep_du_lieu_theo_id.pack(pady=10)
        frame_tao_du_lieu_moi.pack_forget()
        frame_cap_nhat_du_lieu.pack_forget()
        frame_tim_kiem.pack_forget()
        frame_trich_loc.pack_forget()
        frame_xoa_du_lieu.pack_forget()

    btn_sort_page = tk.Button(frame_nut_chuc_nang, text="Sắp xếp", command=show_sort_page)
    btn_sort_page.pack(side=tk.LEFT, padx=5)

    def show_filter_page():
        frame_tao_du_lieu_moi.pack_forget()
        frame_cap_nhat_du_lieu.pack_forget()
        frame_tim_kiem.pack_forget()
        frame_sap_xep_du_lieu_theo_id.pack_forget()
        frame_xoa_du_lieu.pack_forget()
        frame_trich_loc.pack(pady=10)

    btn_filter_page = tk.Button(frame_nut_chuc_nang, text="Lọc dữ liệu", command=show_filter_page)
    btn_filter_page.pack(side=tk.LEFT, padx=5)

    frame_nut_chuyen_trang = tk.Frame(window)
    frame_nut_chuyen_trang.pack(side=tk.BOTTOM, padx=10, pady=10)

    def go_home():
        global current_page
        current_page = 0
        hien_thi_du_lieu()

    btn_home = tk.Button(frame_nut_chuyen_trang, text="Home", command=go_home)
    btn_home.pack(side=tk.LEFT, padx=5)

    def page_previous():
        global current_page
        if current_page > 0:
            current_page -= 1
            hien_thi_du_lieu()

    btn_previous = tk.Button(frame_nut_chuyen_trang, text="Trang trước", command=page_previous)
    btn_previous.pack(side=tk.LEFT, padx=5)

    lbl_page_info = tk.Label(frame_nut_chuyen_trang)
    lbl_page_info.pack(side=tk.LEFT, padx=5)

    entry_page_number = tk.Entry(frame_nut_chuyen_trang, width=5)
    entry_page_number.pack(side=tk.LEFT, padx=5)

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

    def page_next():
        global current_page
        total_pages = (len(data) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE
        if (current_page + 1) < total_pages:
            current_page += 1
            hien_thi_du_lieu()

    btn_next = tk.Button(frame_nut_chuyen_trang, text="Trang sau", command=page_next)
    btn_next.pack(side=tk.LEFT, padx=5)

    frame_tao_du_lieu_moi = tk.Frame(window)

    header_frame_create = tk.Frame(frame_tao_du_lieu_moi)
    header_frame_create.pack(side=tk.TOP)

    inputs = {}
    for col in cols:
        label = tk.Label(header_frame_create, text=col, width=10)
        label.pack(side=tk.LEFT)

        if col in ['Gender', 'CLASS', 'BMI_CATEGORY']:
            entry = ttk.Combobox(frame_tao_du_lieu_moi, width=10)
            unique_values = ['None'] + data[col].unique().tolist()
            entry['values'] = unique_values
            entry.set('None')
        else:
            entry = tk.Entry(frame_tao_du_lieu_moi, width=10)

        entry.pack(side=tk.LEFT, padx=5)
        inputs[col] = entry

    if 'ID' in cols:
        max_id = data['ID'].astype(int).max() if not data['ID'].isnull().all() else 0
        inputs['ID'].insert(0, str(max_id + 1))

    def tao_du_lieu_moi():
        global data  # Đánh dấu data là biến toàn cục
        try:
            new_data = []
            for col in cols:
                if col == 'ID' or col == 'No_Patients':
                    new_data.append(int(inputs[col].get()))
                elif col == 'AGE':
                    value = inputs[col].get()
                    if not value.isdigit() or int(value) <= 0 or int(value) >= 120:
                        raise ValueError(f"{col} phải là kiểu int và lớn hơn 0 và bé hơn 120!")
                    new_data.append(int(value))
                else:
                    value = inputs[col].get()
                    new_data.append(value)

            # Thêm dữ liệu vào DataFrame
            data.loc[len(data)] = new_data
            hien_thi_du_lieu()

            # Lưu lại dữ liệu vào file CSV
            data.to_csv(file_path, index=False)
            messagebox.showinfo("Thành công", "Dữ liệu đã được tạo mới!")
        except ValueError as ve:
            messagebox.showwarning("Giá trị không hợp lệ", str(ve))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo dữ liệu mới: {e}")

    btn_tao_du_lieu = tk.Button(frame_tao_du_lieu_moi, text="Tạo", command=tao_du_lieu_moi)
    btn_tao_du_lieu.pack(side=tk.LEFT, padx=10)

    frame_cap_nhat_du_lieu = tk.Frame(window)

    header_frame_update = tk.Frame(frame_cap_nhat_du_lieu)
    header_frame_update.pack(side=tk.TOP)

    update_inputs = {}
    for col in cols:
        label = tk.Label(header_frame_update, text=col, width=10)
        label.pack(side=tk.LEFT)

        if col in ['Gender', 'CLASS', 'BMI_CATEGORY']:
            entry = ttk.Combobox(frame_cap_nhat_du_lieu, width=10)
            unique_values = ['None'] + data[col].unique().tolist()
            entry['values'] = unique_values
            entry.set('None')
        else:
            entry = tk.Entry(frame_cap_nhat_du_lieu, width=10)

        entry.pack(side=tk.LEFT, padx=5)
        update_inputs[col] = entry

    def cap_nhat_du_lieu():
        global data  # Đánh dấu data là biến toàn cục
        try:
            updated_data = []
            for col in cols:
                if col == 'ID' or col == 'No_Patients':
                    updated_data.append(int(update_inputs[col].get()))
                elif col == 'AGE':
                    value = update_inputs[col].get()
                    if not value.isdigit() or int(value) <= 0 or int(value) >= 120:
                        raise ValueError(f"{col} phải là kiểu int và lớn hơn 0 và bé hơn 120!")
                    updated_data.append(int(value))
                else:
                    updated_data.append(update_inputs[col].get())

            selected_items = tree.selection()
            if not selected_items:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một dòng để cập nhật!")
                return

            for selected_item in selected_items:
                index = tree.index(selected_item)
                for j in range(len(cols)):
                    data.at[index, cols[j]] = updated_data[j]
                    tree.item(selected_item, values=list(updated_data))

            # Lưu lại dữ liệu vào file CSV sau khi cập nhật
            data.to_csv(file_path, index=False)
            messagebox.showinfo("Thành công", "Dữ liệu đã được cập nhật!")
        except ValueError as ve:
            messagebox.showwarning("Giá trị không hợp lệ", str(ve))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Dữ liệu đã không được cập nhật! {e}")

    btn_cap_nhat = tk.Button(frame_cap_nhat_du_lieu, text="Nhập", command=cap_nhat_du_lieu)
    btn_cap_nhat.pack(side=tk.LEFT, padx=10)

    frame_tim_kiem = tk.Frame(window)

    lbl_tim_kiem = tk.Label(frame_tim_kiem, text="Tìm kiếm theo:")
    lbl_tim_kiem.pack(side=tk.LEFT, padx=5)

    searchable_columns = [col for col in cols if col not in ['Gender', 'CLASS', 'BMI_CATEGORY']]

    combo_search_column = ttk.Combobox(frame_tim_kiem, values=searchable_columns, width=15)
    combo_search_column.set(searchable_columns[0])
    combo_search_column.pack(side=tk.LEFT, padx=5)

    entry_tim_kiem_value = tk.Entry(frame_tim_kiem, width=10)
    entry_tim_kiem_value.pack(side=tk.LEFT, padx=5)

    def tim_kiem():
        global current_page
        try:
            column_to_search = combo_search_column.get()
            search_value = entry_tim_kiem_value.get().strip()
            if search_value == "":
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập giá trị cần tìm!")
                return

            ket_qua_tim_kiem = data[data[column_to_search].astype(str).str.contains(search_value, case=False, na=False)]

            for row in tree.get_children():
                tree.delete(row)

            if ket_qua_tim_kiem.empty:
                messagebox.showinfo("Không tìm thấy", f"Không tìm thấy dữ liệu với giá trị = {search_value} trong cột {column_to_search}")
            else:
                for _, row in ket_qua_tim_kiem.iterrows():
                    tree.insert("", "end", values=list(row))

                current_page = 0  
                update_page_info()

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi trong quá trình tìm kiếm: {e}")

    btn_tim_kiem = tk.Button(frame_tim_kiem, text="Tìm kiếm", command=tim_kiem)
    btn_tim_kiem.pack(side=tk.LEFT, padx=5)

    frame_sap_xep_du_lieu_theo_id = tk.Frame(window)

    sortable_columns = [col for col in cols if col not in ['Gender', 'CLASS', 'BMI_CATEGORY']]

    lbl_sort_column = tk.Label(frame_sap_xep_du_lieu_theo_id, text="Chọn cột để sắp xếp:")
    lbl_sort_column.pack(side=tk.LEFT, padx=5)

    combo_sort_column = ttk.Combobox(frame_sap_xep_du_lieu_theo_id, values=sortable_columns, width=15)
    combo_sort_column.set(sortable_columns[0])
    combo_sort_column.pack(side=tk.LEFT, padx=5)

    def sap_xep_tang_dan():
        global data  # Đánh dấu data là biến toàn cục
        try:
            column_to_sort = combo_sort_column.get()
            if column_to_sort not in sortable_columns:
                messagebox.showwarning("Cảnh báo", "Cột không hợp lệ!")
                return
            
            data.sort_values(by=column_to_sort, inplace=True, ascending=True)
            hien_thi_du_lieu()

            data.to_csv(file_path, index=False)
            messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp tăng dần!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

    btn_sap_xep_tang_dan = tk.Button(frame_sap_xep_du_lieu_theo_id, text="Sắp xếp tăng dần", command=sap_xep_tang_dan)
    btn_sap_xep_tang_dan.pack(side=tk.LEFT, padx=10)

    def sap_xep_giam():
        global data  # Đánh dấu data là biến toàn cục
        try:
            column_to_sort = combo_sort_column.get()
            if column_to_sort not in sortable_columns:
                messagebox.showwarning("Cảnh báo", "Cột không hợp lệ!")
                return
            
            data.sort_values(by=column_to_sort, inplace=True, ascending=False)
            hien_thi_du_lieu()

            data.to_csv(file_path, index=False)
            messagebox.showinfo("Thành công", "Dữ liệu đã được sắp xếp giảm dần!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể sắp xếp dữ liệu: {e}")

    btn_sap_xep_giam = tk.Button(frame_sap_xep_du_lieu_theo_id, text="Sắp xếp giảm dần", command=sap_xep_giam)
    btn_sap_xep_giam.pack(side=tk.LEFT, padx=10)

    frame_trich_loc = tk.Frame(window)

    lbl_trich_loc = tk.Label(frame_trich_loc, text="Lọc dữ liệu theo:")
    lbl_trich_loc.pack(side=tk.TOP, padx=5)

    filter_frame = tk.Frame(frame_trich_loc)
    filter_frame.pack(side=tk.TOP)

    gender_options = ['None'] + data['Gender'].unique().tolist()
    class_options = ['None'] + data['CLASS'].unique().tolist()
    bmi_category_options = ['None'] + data['BMI_CATEGORY'].unique().tolist()

    lbl_gender = tk.Label(filter_frame, text="Gender:")
    lbl_gender.pack(side=tk.LEFT, padx=5)
    combo_gender = ttk.Combobox(filter_frame, values=gender_options, width=10)
    combo_gender.set('None')
    combo_gender.pack(side=tk.LEFT, padx=5)

    lbl_class = tk.Label(filter_frame, text="CLASS:")
    lbl_class.pack(side=tk.LEFT, padx=5)
    combo_class = ttk.Combobox(filter_frame, values=class_options, width=10)
    combo_class.set('None')
    combo_class.pack(side=tk.LEFT, padx=5)

    lbl_bmi_category = tk.Label(filter_frame, text="BMI CATEGORY:")
    lbl_bmi_category.pack(side=tk.LEFT, padx=5)
    combo_bmi_category = ttk.Combobox(filter_frame, values=bmi_category_options, width=10)
    combo_bmi_category.set('None')
    combo_bmi_category.pack(side=tk.LEFT, padx=5)

    btn_trich_loc = tk.Button(filter_frame, text="Lọc dữ liệu", command=lambda: trich_loc(combo_gender.get(), combo_class.get(), combo_bmi_category.get()))
    btn_trich_loc.pack(side=tk.LEFT, padx=10)

    def trich_loc(gender, class_val, bmi_category):
        global current_page
        try:
            filtered_data = data

            if gender != 'None':
                filtered_data = filtered_data[filtered_data['Gender'] == gender]

            if class_val != 'None':
                filtered_data = filtered_data[filtered_data['CLASS'] == class_val]

            if bmi_category != 'None':
                filtered_data = filtered_data[filtered_data['BMI_CATEGORY'] == bmi_category]

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

if __name__ == "__main__":
    main()
