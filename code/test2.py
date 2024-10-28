import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Đọc dữ liệu mẫu
data = {
    'AGE': [50, 26, 50, 34, 31, 55, 59],
    'BMI': [24, 23, 24, 23, 24, 27, 31],
    'CLASS': ['N', 'N', 'N', 'P', 'P', 'Y', 'Y']
}
df = pd.DataFrame(data)

# Tạo cửa sổ tkinter
root = tk.Tk()
root.title("Biểu đồ Matplotlib trong Tkinter")

# Tạo một Figure từ matplotlib
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

# Vẽ biểu đồ scatter
for class_label, color in zip(['N', 'P', 'Y'], ['blue', 'orange', 'green']):
    subset = df[df['CLASS'] == class_label]
    ax.scatter(subset['AGE'], subset['BMI'], label=class_label, color=color)

# Cấu hình biểu đồ
ax.set_xlabel('Age')
ax.set_ylabel('BMI')
ax.set_title('Scatter Plot of Age vs BMI by Class')
ax.legend(title="Class")
ax.grid(True)

# Thêm Figure vào giao diện tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Bắt đầu vòng lặp của tkinter
root.mainloop()
