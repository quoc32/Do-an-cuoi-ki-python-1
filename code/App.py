
import tkinter as tk
import pandas as pd
from command import *
from Page import *

class App:
    # root, df, columns
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data App")
        self.root.iconbitmap("./image/icon.ico")
        self.root.geometry("880x450")
        self.root.resizable(False, False) # resize able

        # Dữ liệu của App
        self.df = pd.read_csv('../data/dataset/root_data.csv')
        self.data_fields = self.df.columns.to_list() # Các TRƯỜNG thông tin
        self.data_fields.remove("ID")
        self.data_fields.remove("No_Pation")
        
        # Filter Data Info
        self.filterInfo = {
            "isAll": True
        }

        # Các Page của App
        # Trang chứa thông tin cơ bản của Data
        appDataInfoPage = DataInfoPage(master=self.root, name="Data Information", df=self.df)
        # Trang chứa các tiện ích tạo Đồ Thị
        appCreateChartPage = CreateChartPage(master=self.root, name="Create Chart", fields=self.data_fields, df=self.df)
        # Trang chứa tiện ích đổi Dữ liệu
        appChangeDataPage = CRUDDataPage(master=self.root, name="Change Data")
        # Trang chứa tiện ích đọc Dữ liệu goc
        appReadDataPage = ReadDataPage(master=self.root, name="Read Data", df=self.df, filterInfo=self.filterInfo)
        # Trang chứa tiện ích đọc Dữ liệu Clean
        appReadCleanDataPage = ReadCleanDataPage(master=self.root, name="Read Data", clean_path="../data/clean.csv", filterInfo=self.filterInfo)
        # Trang chứa tiện clean Dữ liệu 
        appFilterDataPage = CleanDataPage(master=self.root, name="Clean Data")

        # Trang chứa tiện ích About Us, giới thiệu nhóm
        appAboutUsPage = AboutUsPage(master=self.root, name="About Us")

        self.pages = {
            "DataInfo": appDataInfoPage,
            "CreateChart": appCreateChartPage,
            "CRUDData": appChangeDataPage,
            "CleanData": appFilterDataPage,
            "ReadData": appReadDataPage,
            "ReadCleanData": appReadCleanDataPage,
            "AboutUs": appAboutUsPage,
        }

        # Tạo nút GIỚI THIỆU
        button = tk.Button(self.root, text="Data Info", command=lambda: introduce(self.root, self.pages))
        button.place(x=0, y=0, width=80, height=30)
        # Tạo nút Đọc dữ liệu gốc
        button = tk.Button(self.root, text="Dữ Liệu Gốc", command=lambda: go_to_read_data(self.root, self.pages))
        button.place(x=0, y=30, width=80, height=30)
        # Tạo nút Đọc dữ liệu clean
        button = tk.Button(self.root, text="Dữ Liệu Clean", command=lambda: go_to_read_clean_data(self.root, self.pages))
        button.place(x=0, y=60, width=80, height=30)
        # Tạo nút TẠO BIỂU ĐỒ
        button = tk.Button(self.root, text="Tạo Biểu Đồ", command=lambda: go_to_create_chart(self.root, self.pages))
        button.place(x=0, y=90, width=80, height=30)
        # Tạo nút Đổi dữ liệu
        button = tk.Button(self.root, text="CRUD", command=lambda: go_to_CRUD_data(self.root, self.pages))
        button.place(x=0, y=120, width=80, height=30)
        # Tạo nút Lọc dữ liệu (bổ trợ cho đọc dữ liệu)
        button = tk.Button(self.root, text="Làm Sạch DL", command=lambda: go_to_clean_data(self.root, self.pages))
        button.place(x=0, y=150, width=80, height=30)

        # Tạo nút About Us
        button = tk.Button(self.root, text="About Us", command=lambda: go_to_about_us(self.root, self.pages))
        button.place(x=0, y=420, width=80, height=30)


        # go_to_about_us ban đầu
        go_to_about_us(self.root, self.pages)

    def turn_on(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    print("App module.")
