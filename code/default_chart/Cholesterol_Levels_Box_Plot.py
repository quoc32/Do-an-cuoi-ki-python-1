{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu từ file CSV
# df = pd.read_csv('../../data/dataset/data.csv')

# # Tạo hình (canvas) với kích thước 6x8 inch
# plt.figure(figsize=(6, 8))

# # Vẽ biểu đồ boxplot cho mức độ cholesterol
# sns.boxplot(data=df, y='Chol', color="lightgreen")

# # Thêm tiêu đề và nhãn cho các trục
# plt.title('Mức Độ Cholesterol')
# plt.ylabel('Cholesterol')

# # Hiển thị biểu đồ
# plt.show()
}

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
df = pd.read_csv('../data/dataset/data.csv')
Cholesterol_Levels_Box_Plot__fig = Figure(figsize=(6, 4), dpi=90) # <= fig obj ở đây
ax = Cholesterol_Levels_Box_Plot__fig.add_subplot(111)
sns.boxplot(data=df, y='Chol', color="lightgreen", ax=ax)
ax.set_title('Mức Độ Cholesterol')
ax.set_ylabel('Cholesterol')
