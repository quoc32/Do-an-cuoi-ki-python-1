{
# import matplotlib.pyplot as plt
# import pandas as pd

# # Đọc dữ liệu từ file CSV
# df = pd.read_csv('../../data/dataset/data.csv')

# # Tạo hình (canvas) với kích thước 6x6 inch
# plt.figure(figsize=(6, 6))

# # Vẽ biểu đồ donut với phân phối giới tính
# plt.pie(df['Gender'].value_counts(), labels=df['Gender'].value_counts().index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
# plt.gca().add_artist(plt.Circle((0, 0), 0.70, fc='white'))  # Tạo phần trung tâm rỗng để tạo hiệu ứng donut

# # Thêm tiêu đề cho biểu đồ
# plt.title('Phân Phối Giới Tính')

# # Hiển thị biểu đồ
# plt.show()
}

import pandas as pd
from matplotlib.figure import Figure
from matplotlib.patches import Circle
df = pd.read_csv('../data/dataset/data.csv')
Gender_Distribution_Donut_Chart__fig = Figure(figsize=(6, 4), dpi=90)
ax = Gender_Distribution_Donut_Chart__fig.add_subplot(111)
gender_counts = df['Gender'].value_counts()
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
center_circle = Circle((0, 0), 0.70, fc='white')
ax.add_artist(center_circle)
ax.set_title('Phân Phối Giới Tính')
