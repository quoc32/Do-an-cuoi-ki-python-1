
import pandas as pd
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
    
def go_to_filter_data(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["FilterData"].place(x=81, y=0)

def go_to_read_data(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["ReadData"].place(x=81, y=0)

def go_to_change_data(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["ChangeData"].place(x=81, y=0)

def go_to_about_us(root, pages):
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["AboutUs"].place(x=81, y=0)

###############################
from default_chart.bieuDo1 import fig1
def veBieuDo1(frame):
    canvas = FigureCanvasTkAgg(fig1, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.HbA1c_BMI_By_Health_Class import HbA1c_BMI_By_Health_Class__fig
def veBieuDo_HbA1c_BMI_By_Health_Class(frame):
    canvas = FigureCanvasTkAgg(HbA1c_BMI_By_Health_Class__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Age_And_Cholesterol import Age_And_Cholesterol__fig
def veBieuDo_Age_And_Cholesterol(frame):
    canvas = FigureCanvasTkAgg(Age_And_Cholesterol__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Age_Distribution_Histogram import Age_Distribution_Histogram__fig
def veBieuDo_Age_Distribution_Histogram(frame):
    canvas = FigureCanvasTkAgg(Age_Distribution_Histogram__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Age_Distribution_By_Health_Class import Age_Distribution_By_Health_Class__fig
def veBieuDo_Age_Distribution_By_Health_Class(frame):
    canvas = FigureCanvasTkAgg(Age_Distribution_By_Health_Class__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Cholesterol_Levels_Box_Plot import Cholesterol_Levels_Box_Plot__fig
def veBieuDo_Cholesterol_Levels_Box_Plot(frame):
    canvas = FigureCanvasTkAgg(Cholesterol_Levels_Box_Plot__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Gender_Distribution_Donut_Chart import Gender_Distribution_Donut_Chart__fig
def veBieuDo_Gender_Distribution_Donut_Chart(frame):
    canvas = FigureCanvasTkAgg(Gender_Distribution_Donut_Chart__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.HbA1c_Distribution_Histogram import HbA1c_Distribution_Histogram__fig
def veBieuDo_HbA1c_Distribution_Histogram(frame):
    canvas = FigureCanvasTkAgg(HbA1c_Distribution_Histogram__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Health_Class_Distribution_Donut_Chart import Health_Class_Distribution_Donut_Chart__fig
def veBieuDo_Health_Class_Distribution_Donut_Chart(frame):
    canvas = FigureCanvasTkAgg(Health_Class_Distribution_Donut_Chart__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

from default_chart.Triglycerides_LDL_By_Health_Class import Triglycerides_LDL_By_Health_Class__fig
def veBieuDo_veBieuDo_Triglycerides_LDL_By_Health_Class(frame):
    canvas = FigureCanvasTkAgg(Triglycerides_LDL_By_Health_Class__fig, master=frame)
    canvas.draw()
    tk_canvas = canvas.get_tk_widget()
    tk_canvas.place(x=12, y=72)

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
