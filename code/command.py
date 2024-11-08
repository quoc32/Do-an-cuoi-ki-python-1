
import pandas as pd
import matplotlib.pyplot as plt
import default_chart.IMB_class

def on_button_click():
    print("Nút đã được nhấn!")
    # Đọc dữ liệu
    df = pd.read_csv('../data/data.csv')

    # Vẽ biểu đồ scatter
    plt.figure(figsize=(10, 6))
    for class_label, color in zip(['N', 'P', 'Y'], ['blue', 'orange', 'green']):
        subset = df[df['CLASS'] == class_label]
        plt.scatter(subset['AGE'], subset['BMI'], label=class_label, color=color)

    # Thêm các chi tiết cho biểu đồ
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.title('Scatter Plot of Age vs BMI by Class')
    plt.legend(title="Class")
    plt.grid(True)
    plt.show()

def introduce(root, pages):
    print("Đây là ứng dụng phân tích dữ liệu.")
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["DataInfo"].place(x=0, y=40)

def go_to_create_chart(root, pages):
    print("Đến trang Tạo biểu đồ")
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["CreateChart"].place(x=0, y=40)
    
def go_to_filter_data(root, pages):
    print("Đến trang Lọc dữ liệu")
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["FilterData"].place(x=0, y=40)

def go_to_change_data(root, pages):
    print("Đến trang Tạo biểu đồ")
    # Ẩn tất cả các page
    for page_key in pages:
        pages[page_key].place_forget()
    # Hiện Page "CreateChart"
    pages["ChangeData"].place(x=0, y=40)

###############################
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
