import tkinter as tk
from tkinter import ttk
from io import StringIO

from command import drawCustomHandle, drawDefaultHandle

class Page(tk.Frame):
    def __init__(self, master, name):
        super().__init__(master, bd=5, relief=tk.RIDGE, width=330, height=190)
        self.name = name
        self.pack_propagate(False)
        self.configure(bg="black")
        

class DataInfoPage(Page):
    def __init__(self, master, name, df):
        super().__init__(master, name)
        DaInfoPa_label = tk.Label(master=self, text="Thông tin cơ bản")
        DaInfoPa_label.pack()
        # Text hiển thị thông tin
        DaInfoPa_text_box = tk.Text(master=self)
        buffer = StringIO()
        df.info(buf=buffer)
        info_buffer = buffer.getvalue()
        DaInfoPa_text_box.delete(1.0, tk.END)
        DaInfoPa_text_box.insert(tk.END, info_buffer)

        DaInfoPa_text_box.insert(tk.END, "\n=====================\n- NGUỒN DỮ LIỆU: Bộ dữ liệu được xây dựng từ hồ sơ y tế của bệnh nhân được lấy từ các bệnh viện ở Iraq, bao gồm: \n  + Bệnh viện Thành phố Y tế \n  + Trung tâm Chuyên ngành Nội tiết và Tiểu đường \n  + Bệnh viện Giảng dạy Al-Kindy")
        DaInfoPa_text_box.insert(tk.END, "\n- PHƯƠNG PHÁP THU THẬP DỮ LIỆU: \n  + Hồ sơ bệnh nhân đã được xem xét, và các thông tin y tế liên quan đã được trích xuất và nhập vào cơ sở dữ liệu để tạo ra bộ dữ liệu tiểu đường.")
        DaInfoPa_text_box.insert(tk.END, "\n- CÁC THUỘC TÍNH CỦA DỮ LIỆU:")
        DaInfoPa_text_box.insert(tk.END, "\n  + ID: Mã số định danh duy nhất của người bệnh.")
        DaInfoPa_text_box.insert(tk.END, "\n  + No_Pation: Số thứ tự trong một danh sách cơ sở dữ liệu.")
        DaInfoPa_text_box.insert(tk.END, "\n  + Gender: M -> Nam, F -> Nữ")
        DaInfoPa_text_box.insert(tk.END, "\n  + Age: Tuổi bệnh nhân")
        DaInfoPa_text_box.insert(tk.END, "\n  + Urea: Nồng độ Urea trong máu (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + Cr: Nồng độ Creatinine trong máu (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + HbA1C: Mức glucose trung bình trong máu trong vòng 2 đến 3 tháng qua (%)")
        DaInfoPa_text_box.insert(tk.END, "\n  + Chol: Mức cholesterol tổng trong máu (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + TG(Triglycerides): Một loại chất béo có trong máu (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + TG(Triglycerides): Một loại chất béo có trong máu (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + HDL(High-Density Lipoprotein): Một loại lipoprotein có trong máu và thường được biết đến là cholesterol tốt (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + LDL(Low-Density Lipoprotein): Một loại lipoprotein trong máu, thường được gọi là cholesterol xấu (mg/dL)")
        DaInfoPa_text_box.insert(tk.END, "\n  + VLDL(Very Low-Density Lipoprotein): Một loại lipoprotein khác có trong máu")
        DaInfoPa_text_box.insert(tk.END, "\n  + BMI(Body Mass Index): Chỉ số khối cơ thể (kg/m^2)")
        DaInfoPa_text_box.insert(tk.END, "\n  + CLASS: Y -> Tiểu đường; N -> Không tiểu đường; P -> Tiền tiểu đường")

        DaInfoPa_text_box.pack()
        DaInfoPa_text_box.config(state=tk.DISABLED)


class CreateChartPage(Page):
    def __init__(self, master, name, fields, df):
        super().__init__(master, name)
        self.fields = fields
        self.df = df
        CreCharPa_label = tk.Label(master=self, text="Đây là trang tạo đồ thị")
        CreCharPa_label.pack()

        # Ô chọn đồ thị mặc định
        cacDoThiMacDinh = ["1. Đồ thị 1", "2. Đồ thị 2", "3. Biểu đồ 3", "0. Custom"]
        doThiMacDinh = ttk.Combobox(master=self, values=cacDoThiMacDinh, state="readonly")
        doThiMacDinh.set("1. Đồ thị 1")
        doThiMacDinh.place(x=170, y=30)

        # Ô chọn loại đồ thị
        cacloaiDoThi = ["Đồ thị đường", "Đồ thị phân tán", "Đồ thị cột", "Biểu đồ tròn"]
        loaiDoThi = ttk.Combobox(master=self, values=cacloaiDoThi, state="disabled")
        loaiDoThi.set("Chọn loại đồ thị")
        loaiDoThi.place(x=5, y=30)

        # Ô chọn loại đồ thị giá trị cho trục X
        cac_truc_x = self.fields
        truc_x = ttk.Combobox(master=self, values=cac_truc_x, state="disabled")
        truc_x.set("Trục X")
        truc_x.place(x=5, y=55)

        # Ô chọn loại đồ thị giá trị cho trục X
        cac_truc_y = self.fields
        truc_y = ttk.Combobox(master=self, values=cac_truc_y, state="disabled")
        truc_y.set("Trục Y")
        truc_y.place(x=5, y=80)

        # Tạo nút CREATE
        def createHandle():
            isCustom = (doThiMacDinh.get() == "0. Custom")
            if isCustom:
                plot_tyle = loaiDoThi.get()
                x_field = truc_x.get()
                y_field = truc_y.get()
                drawCustomHandle(plot_type=plot_tyle, x_field=x_field, y_field=y_field, df=self.df)
            else:
                default_chart_name = doThiMacDinh.get()
                drawDefaultHandle(default_chart_name)

        button = tk.Button(master=self, text="Create", command=createHandle)
        button.place(x=240, y=140, width=70, height=30)

        # Thêm mở chọn và đóng chọn cho các combobox khác
        def on_custom_select(event):
            # Bật các combobox khác nếu "0. Custom" được chọn
            if doThiMacDinh.get() == "0. Custom":
                loaiDoThi.config(state="normal")
                truc_x.config(state="normal")
                truc_y.config(state="normal")
            # Tắt các combobox khác nếu giá trị khác "0. Custom" được chọn
            else:
                loaiDoThi.config(state="disabled")
                truc_x.config(state="disabled")
                truc_y.config(state="disabled")

        doThiMacDinh.bind("<<ComboboxSelected>>", on_custom_select)

class ChangeDataPage(Page):
    def __init__(self, master, name):
        super().__init__(master, name)
        ChanDaPa_label = tk.Label(master=self, text="Đây là trang thay đổi data")
        ChanDaPa_label.pack()


class FilterDataPage(Page):
    def __init__(self, master, name):
        super().__init__(master, name)
        FilDaPa_label = tk.Label(master=self, text="Đây là trang lọc data")
        FilDaPa_label.pack()
