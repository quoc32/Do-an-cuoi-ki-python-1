
import tkinter as tk
import pandas as pd
from command import *
from Page import DataInfoPage, CreateChartPage, ChangeDataPage, FilterDataPage

class App:
    # root, df, columns
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Window")
        self.root.geometry("330x230")
        self.root.configure(bg="purple")
        # self.root.resizable(False, False) # resize able

        # Dữ liệu của App
        self.df = pd.read_csv('../data/dataset/data.csv')
        self.data_fields = self.df.columns.to_list() # Các TRƯỜNG thông tin
        self.data_fields.remove("ID")
        self.data_fields.remove("No_Pation")

        # Các Page của App
        # Trang chứa thông tin cơ bản của Data
        appDataInfoPage = DataInfoPage(master=self.root, name="Data Information", df=self.df)

        # Trang chứa các tiện ích tạo Đồ Thị
        appCreateChartPage = CreateChartPage(master=self.root, name="Create Chart", fields=self.data_fields, df=self.df)

        # Trang chứa tiện ích đổi Dữ liệu
        appChangeDataPage = ChangeDataPage(master=self.root, name="Change Data")

        # Trang chứa tiện ích lọc Dữ liệu
        appFilterDataPage = FilterDataPage(master=self.root, name="Filter Data")

        self.pages = {
            "DataInfo": appDataInfoPage,
            "CreateChart": appCreateChartPage,
            "ChangeData": appChangeDataPage,
            "FilterData": appFilterDataPage
        }

        # Tạo nút GIỚI THIỆU
        button = tk.Button(self.root, text="Giới Thiệu", command=lambda: introduce(self.root, self.pages))
        button.place(x=10, y=5, width=70, height=30)
        # Tạo nút TẠO BIỂU ĐỒ
        button = tk.Button(self.root, text="Tạo Biểu Đồ", command=lambda: go_to_create_chart(self.root, self.pages))
        button.place(x=90, y=5, width=70, height=30)
        # Tạo nút Đổi dữ liệu
        button = tk.Button(self.root, text="Đổi Dữ Liệu", command=lambda: go_to_change_data(self.root, self.pages))
        button.place(x=170, y=5, width=70, height=30)
        # Tạo nút Lọc dữ liệu
        button = tk.Button(self.root, text="Lọc Dữ Liệu", command=lambda: go_to_filter_data(self.root, self.pages))
        button.place(x=250, y=5, width=70, height=30)

    def turn_on(self):
        self.root.mainloop()


    


if __name__ == "__main__":
    print("App module.")
