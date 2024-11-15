{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu từ file CSV
# df = pd.read_csv('../../data/dataset/data.csv')

# # Tạo hình (canvas) với kích thước 8x6 inch
# plt.figure(figsize=(8, 6))

# # Vẽ biểu đồ histogram cho phân phối tuổi, thêm đường cong KDE để hiển thị mật độ
# sns.histplot(data=df, x='AGE', bins=10, kde=True, color="skyblue")

# # Thêm tiêu đề và nhãn cho các trục
# plt.title('Phân Phối Tuổi')
# plt.xlabel('Tuổi')
# plt.ylabel('Tần suất')

# # Hiển thị biểu đồ
# plt.show()
}

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
df = pd.read_csv('../data/dataset/data.csv')
Age_Distribution_Histogram__fig = Figure(figsize=(6, 4), dpi=90) # <= fig obj ở đây
ax = Age_Distribution_Histogram__fig.add_subplot(111)
sns.histplot(data=df, x='AGE', bins=10, kde=True, color="skyblue", ax=ax)
ax.set_title('Phân Phối Tuổi')
ax.set_xlabel('Tuổi')
ax.set_ylabel('Tần suất')
