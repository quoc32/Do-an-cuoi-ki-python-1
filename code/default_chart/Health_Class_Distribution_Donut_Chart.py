{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu
# df = pd.read_csv('../../data/dataset/data.csv')

# # Lấy dữ liệu phân phối theo lớp sức khỏe
# class_counts = df['CLASS'].value_counts()

# # Vẽ biểu đồ donut cho phân phối lớp sức khỏe
# plt.figure(figsize=(6, 6))
# plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff9999'])
# centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)
# plt.title('Health Class Distribution')
# plt.show()
}

import pandas as pd
from matplotlib.figure import Figure
from matplotlib.patches import Circle
df = pd.read_csv('../data/dataset/data.csv')
Health_Class_Distribution_Donut_Chart__fig = Figure(figsize=(6, 4), dpi=90)
ax = Health_Class_Distribution_Donut_Chart__fig.add_subplot(111)
class_counts = df['CLASS'].value_counts()
ax.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff', 'yellow'])
center_circle = Circle((0, 0), 0.70, fc='white')
ax.add_artist(center_circle)
ax.set_title('Health Class Distribution')
