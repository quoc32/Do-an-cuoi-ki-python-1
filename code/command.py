
import pandas as pd
import matplotlib.pyplot as plt

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



if __name__ == "__main__":
    print("command module.")
