
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def introduce(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["DataInfo"].place(x=81, y=0)

def go_to_create_chart(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["CreateChart"].place(x=81, y=0)
    
def go_to_clean_data(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["CleanData"].place(x=81, y=0)

def go_to_read_data(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["ReadData"].place(x=81, y=0)

def go_to_CRUD_data(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["CRUDData"].place(x=81, y=0)

def go_to_about_us(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["AboutUs"].place(x=81, y=0)

###############################

from PIL import Image, ImageTk

def veBieuDo_1(page):
    img1 = Image.open("./chart_img/AgeDistributionByHealthClass.png")
    img1 = img1.resize((550, 350))
    page.tk_img1 = ImageTk.PhotoImage(img1)

    label1 = tk.Label(page, image=page.tk_img1)
    label1.place(x=10, y=70)

def veBieuDo_2(page):
    img2 = Image.open("./chart_img/beo_phi_theo_gioi_tinh.png")
    img2 = img2.resize((550, 330))
    page.tk_img2 = ImageTk.PhotoImage(img2)

    label2 = tk.Label(page, image=page.tk_img2)
    label2.place(x=10, y=70)

def veBieuDo_3(page):
    img3 = Image.open("./chart_img/bmi_vs_lipit.png")
    img3 = img3.resize((700, 350))
    page.tk_img3 = ImageTk.PhotoImage(img3)

    label3 = tk.Label(page, image=page.tk_img3)
    label3.place(x=10, y=70)

def veBieuDo_4(page):
    img4 = Image.open("./chart_img/bmi_vs_HbA1c.png")
    img4 = img4.resize((550, 340))
    page.tk_img4 = ImageTk.PhotoImage(img4)

    label4 = tk.Label(page, image=page.tk_img4)
    label4.place(x=10, y=70)

def veBieuDo_5(page):
    img5 = Image.open("./chart_img/chi_so_than.png")
    img5 = img5.resize((700, 330))
    page.tk_img5 = ImageTk.PhotoImage(img5)

    label5 = tk.Label(page, image=page.tk_img5)
    label5.place(x=10, y=70)

def veBieuDo_6(page):
    img6 = Image.open("./chart_img/ma_tran_tuong_quan.png")
    img6 = img6.resize((600, 340))
    page.tk_img6 = ImageTk.PhotoImage(img6)

    label6 = tk.Label(page, image=page.tk_img6)
    label6.place(x=10, y=70)

def veBieuDo_7(page):
    img7 = Image.open("./chart_img/mat_do_bmi.png")
    img7 = img7.resize((550, 340))
    page.tk_img7 = ImageTk.PhotoImage(img7)

    label7 = tk.Label(page, image=page.tk_img7)
    label7.place(x=10, y=70)
    
def veBieuDo_8(page):
    img8 = Image.open("./chart_img/phan_bo_bmi.png")
    img8 = img8.resize((550, 340))
    page.tk_img8 = ImageTk.PhotoImage(img8)

    label8 = tk.Label(page, image=page.tk_img8)
    label8.place(x=10, y=70)

def veBieuDo_9(page):
    img9 = Image.open("./chart_img/phan_bo_chi_so_lipit.png")
    img9 = img9.resize((700, 350))
    page.tk_img9 = ImageTk.PhotoImage(img9)

    label9 = tk.Label(page, image=page.tk_img9)
    label9.place(x=10, y=70)

def veBieuDo_10(page):
    img10 = Image.open("./chart_img/phan_bo_hba1c.png")
    img10 = img10.resize((550, 340))
    page.tk_img10 = ImageTk.PhotoImage(img10)

    label10 = tk.Label(page, image=page.tk_img10)
    label10.place(x=10, y=70)
    
def veBieuDo_11(page):
    img11 = Image.open("./chart_img/phan_bo_tuoi.png")
    img11 = img11.resize((550, 330))
    page.tk_img11 = ImageTk.PhotoImage(img11)

    label11 = tk.Label(page, image=page.tk_img11)
    label11.place(x=10, y=70)

###############################

# Vẽ đồ thị đường thẳng
def drawPlot(df, x_label, y_label):
    # Kiểm tra xem x_label và y_label có trong DataFrame không
    if x_label not in df.columns or y_label not in df.columns:
        raise ValueError("x_label hoặc y_label không tồn tại trong DataFrame.")
    
    # Vẽ đồ thị
    plt.figure(figsize=(8, 6))
    plt.plot(df[x_label], df[y_label], marker='o', linestyle='-', color='b')  # Sử dụng marker và line style tùy chọn
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'{y_label} vs {x_label}')
    plt.grid(True)
    plt.show()

# Vẽ đồ thị phân tán
def drawScatter(df, x_label, y_label):
    # plt.scatter(....
    pass

# Vẽ đồ thị cột
def drawBar(df, x_label, y_label):
    # plt.bar(....
    pass

# Vẽ đồ thị tròn
def drawPieChart(df, label):
    pass
###############################
def drawCustomHandle(plot_type, x_field, y_field, df):
    if plot_type == "Chọn loại đồ thị" or x_field == "Trục X" or y_field == "Trục Y":
        print("Đồ thị custom không hợp lệ!")
        return

    print("draw custom")
    print("plot_type:", plot_type)
    print("x_field:", x_field)
    print("y_field:", y_field)

    # Vẽ đồ thị
    # drawPlot(df, x_label=x_field, y_label=y_field) # Ví dụ gọi vẽ đồ thị scatter ở đây

def drawDefaultHandle(default_chart_name):
    print("draw default", default_chart_name)


if __name__ == "__main__":
    print("command module.")
