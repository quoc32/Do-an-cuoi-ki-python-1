import tkinter as tk
from tkinter import ttk
from io import StringIO

from command import *

class Page(tk.Frame):
    def __init__(self, master, name):
        super().__init__(master, bd=5, relief=tk.RIDGE, width=799, height=450)
        self.name = name
        self.pack_propagate(False)
        self.configure(bg="black")

class DataInfoPage(Page):
    def __init__(self, master, name, df):
        super().__init__(master, name)
        # Text hiển thị thông tin
        DaInfoPa_text_box = tk.Text(master=self, height=100, width=150)
        buffer = StringIO()
        df.info(buf=buffer)
        info_buffer = buffer.getvalue()
        info_lines = info_buffer.splitlines()
        info_lines = info_lines[1:]
        info_buffer = "\n".join(info_lines)
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

        # Ô chọn đồ thị mặc định
        cacDoThiMacDinh = [
            "1. HbA1c_BMI_By_Health_Class", 
            "2. Triglycerides_LDL_By_Health_Class 1", 
            "3. Age_And_Cholesterol", 
            "4. Age_Distribution_Histogram",
            "5. Age_Distribution_By_Health_Class",
            "6. Cholesterol_Levels_Box_Plot",
            "7. Gender_Distribution_Donut_Chart",
            "8. HbA1c_Distribution_Histogram",
            "9. Health_Class_Distribution_Donut_Chart",
        ]
        doThiMacDinh = ttk.Combobox(master=self, values=cacDoThiMacDinh, width=30)
        doThiMacDinh.set("1. HbA1c_BMI_By_Health_Class")
        doThiMacDinh.place(x=5, y=5)

        # Tạo nút CREATE và xử lý khi nhấn
        def createHandle():
            clearHandle() # Clear trước
            if(doThiMacDinh.get() == "1. HbA1c_BMI_By_Health_Class"):
                veBieuDo_HbA1c_BMI_By_Health_Class(self)
            elif(doThiMacDinh.get() == "2. Triglycerides_LDL_By_Health_Class 1"):
                veBieuDo_veBieuDo_Triglycerides_LDL_By_Health_Class(self)
            elif(doThiMacDinh.get() == "3. Age_And_Cholesterol"):
                veBieuDo_Age_And_Cholesterol(self)
            elif(doThiMacDinh.get() == "4. Age_Distribution_Histogram"):
                veBieuDo_Age_Distribution_Histogram(self)
            elif(doThiMacDinh.get() == "5. Age_Distribution_By_Health_Class"):
                veBieuDo_Age_Distribution_By_Health_Class(self)
            elif(doThiMacDinh.get() == "6. Cholesterol_Levels_Box_Plot"):
                veBieuDo_Cholesterol_Levels_Box_Plot(self)
            elif(doThiMacDinh.get() == "6. Cholesterol_Levels_Box_Plot"):
                veBieuDo_Cholesterol_Levels_Box_Plot(self)
            elif(doThiMacDinh.get() == "7. Gender_Distribution_Donut_Chart"):
                veBieuDo_Gender_Distribution_Donut_Chart(self)
            elif(doThiMacDinh.get() == "7. Gender_Distribution_Donut_Chart"):
                veBieuDo_Gender_Distribution_Donut_Chart(self)
            elif(doThiMacDinh.get() == "8. HbA1c_Distribution_Histogram"):
                veBieuDo_HbA1c_Distribution_Histogram(self)
            elif(doThiMacDinh.get() == "9. Health_Class_Distribution_Donut_Chart"):
                veBieuDo_Health_Class_Distribution_Donut_Chart(self)            

        button = tk.Button(master=self, text="Create", command=createHandle)
        button.place(x=140, y=30, width=70, height=30)

        # Tạo nút CLEAR và xử lý khi nhấn
        def clearHandle():
            for wg in self.winfo_children():
                if isinstance(wg, tk.Canvas):
                    wg.destroy() # Xóa tk.Canvas

        button = tk.Button(master=self, text="Clear", command=clearHandle)
        button.place(x=65, y=30, width=70, height=30)

class ReadDataPage(Page):
    def __init__(self, master, name, df, filterInfo=None):
        super().__init__(master, name)
        self.filterInfo = filterInfo
        self.current_text_idx = 0
        self.total_sub_page = 0

        # Text hiển thị thông tin
        self.text_box = tk.Text(master=self, height=26, width=150)
        buffer = df.to_string()
        buffer = buffer.split('\n')
        self.header = buffer[0] + '\n'
        buffer = buffer[1:]
        
        # Biến cần thiết
        self.chunks = []
        chunk = []
        newline_count = 0
        # Tạo đoạn mỗi 25 dòng
        for line in buffer:
            chunk.append(line)
            newline_count += 1
            if newline_count == 25:
                self.chunks.append('\n'.join(chunk))
                chunk = []
                newline_count = 0
                self.total_sub_page += 1
        # Thêm lần cuối với trường hợp lỡ không đủ
        self.chunks.append('\n'.join(chunk))
        chunk = []
        newline_count = 0
        self.total_sub_page += 1

        # Pack lên Frame
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, self.header)
        self.text_box.insert(tk.END, self.chunks[self.current_text_idx])

        self.text_box.pack()
        self.text_box.config(state=tk.DISABLED)

        # Tạo nút next và xử lý khi nhấn
        button = tk.Button(master=self, text="Next", command=lambda : self.nextHandle())
        button.place(x=740, y=420, width=50, height=20)
        # Tạo nút pre và xử lý khi nhấn
        button = tk.Button(master=self, text="Pre", command=lambda : self.preHandle())
        button.place(x=690, y=420, width=50, height=20)

        # Tạo nhãn hiển thị số trang hiện tại và số trang tối đa
        self.current_label = tk.Label(master=self, text=f"{self.current_text_idx + 1}/{self.total_sub_page}", bg="black", fg="white")
        self.current_label.place(x=330, y=420, width=80, height=20)

        # Tạo nhãn cho go_to_idx input
        go_to_idx_label = tk.Label(master=self, text=f"Đến trang: ", bg="black", fg="white")
        go_to_idx_label.place(x=20, y=420, width=80, height=20)
        self.idx_input = tk.Entry(self, width=30)
        self.idx_input.place(x=100, y=420, width=40)
        button = tk.Button(master=self, text="go", command=lambda : self.goHandle(self.idx_input.get()))
        button.place(x=132, y=420, width=50, height=20)

    # Change filterInfo
    def setFilterInfo(self, newFilterInfo):
        self.filterInfo = newFilterInfo
    # Change text_box index
    def setFilterInfo(self, newIdx):
        self.current_text_idx = newIdx
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, self.header)
        self.text_box.insert(tk.END, self.chunks[self.current_text_idx])
    # Xử lý khi nhấn next
    def nextHandle(self):
        if self.current_text_idx >= self.total_sub_page - 1:
            return

        self.current_text_idx += 1
        self.text_box.destroy()
        self.current_label.destroy()

        # Đặt lại text_box
        self.text_box = tk.Text(master=self, height=26, width=150)
        self.text_box.insert(tk.END, self.header)
        self.text_box.insert(tk.END, self.chunks[self.current_text_idx])
        # Đặt lại nhãn
        self.current_label = tk.Label(master=self, text=f"{self.current_text_idx + 1}/{self.total_sub_page}", bg="black", fg="white")
        self.current_label.place(x=330, y=420, width=80, height=20)

        self.text_box.pack()
        self.text_box.config(state=tk.DISABLED)
    # Xử lý khi nhấn pre
    def preHandle(self):
        if self.current_text_idx <= 0:
            return

        self.current_text_idx -= 1
        self.text_box.destroy()
        self.current_label.destroy()

        # Đặt lại text_box
        self.text_box = tk.Text(master=self, height=26, width=150)
        self.text_box.insert(tk.END, self.header)
        self.text_box.insert(tk.END, self.chunks[self.current_text_idx])
        # Đặt lại nhãn
        self.current_label = tk.Label(master=self, text=f"{self.current_text_idx + 1}/{self.total_sub_page}", bg="black", fg="white")
        self.current_label.place(x=330, y=420, width=80, height=20)

        self.text_box.pack()
        self.text_box.config(state=tk.DISABLED)
    # Xử lý khi nhấn go
    def goHandle(self, idx):
        if not idx.isdigit():
            print("index không hợp lệ")
            self.idx_input.delete(0, tk.END)
            return
        
        idx = int(idx) - 1

        if idx < 0 or idx >= self.total_sub_page:
            print("index vượt ra khỏi range hợp lệ")
            self.idx_input.delete(0, tk.END)
            return
        
        self.idx_input.delete(0, tk.END)

        self.current_text_idx = idx
        self.text_box.destroy()
        self.current_label.destroy()

        # Đặt lại text_box
        self.text_box = tk.Text(master=self, height=26, width=150)
        self.text_box.insert(tk.END, self.header)
        self.text_box.insert(tk.END, self.chunks[self.current_text_idx])
        # Đặt lại nhãn
        self.current_label = tk.Label(master=self, text=f"{self.current_text_idx + 1}/{self.total_sub_page}", bg="black", fg="white")
        self.current_label.place(x=330, y=420, width=80, height=20)

        self.text_box.pack()
        self.text_box.config(state=tk.DISABLED)

class ChangeDataPage(Page):
    def __init__(self, master, name):
        super().__init__(master, name)

# Trang lọc
class FilterDataPage(Page):
    def __init__(self, master, name):
        super().__init__(master, name)



# Trang giới thiệu
from PIL import Image, ImageTk
class AboutUsPage(Page):
    def __init__(self, master, name):
        super().__init__(master, name)

        self.start_x = 20
        self.pict_w = 170
        self.pict_padding = 20

        # Them anh tv 1
        img_tv1 = Image.open("./image/quoc.png")
        img_tv1_w, img_tv1_h = img_tv1.size
        img_tv1 = img_tv1.resize((img_tv1_w // 2, img_tv1_h // 2))
        self.tk_img_tv1 = ImageTk.PhotoImage(img_tv1)

        label_tv1 = tk.Label(self, image=self.tk_img_tv1, text="Quốc: UI", compound='top')
        label_tv1.place(x=self.start_x, y=10)

        # Them anh tv 2
        img_tv2 = Image.open("./image/quoc.png")
        img_tv2_w, img_tv2_h = img_tv2.size
        img_tv2 = img_tv2.resize((img_tv2_w // 2, img_tv2_h // 2))
        self.tk_img_tv2 = ImageTk.PhotoImage(img_tv2)

        label_tv2 = tk.Label(self, image=self.tk_img_tv2, text="TV2: CV2", compound='top')
        label_tv2.place(x=self.start_x + 1 * (self.pict_w + self.pict_padding), y=10)
        
        # Them anh tv 3
        img_tv3 = Image.open("./image/quoc.png")
        img_tv3_w, img_tv3_h = img_tv3.size
        img_tv3 = img_tv3.resize((img_tv3_w // 2, img_tv3_h // 2))
        self.tk_img_tv3 = ImageTk.PhotoImage(img_tv3)

        label_tv3 = tk.Label(self, image=self.tk_img_tv3, text="TV3: CV3", compound='top')
        label_tv3.place(x=self.start_x + 2 * (self.pict_w + self.pict_padding), y=10)
