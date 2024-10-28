import tkinter as tk
from tkinter import ttk
from io import StringIO

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
    def __init__(self, master, name):
        super().__init__(master, name)
        CreCharPa_label = tk.Label(master=self, text="Đây là trang tạo đồ thị")
        CreCharPa_label.pack()
        

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
