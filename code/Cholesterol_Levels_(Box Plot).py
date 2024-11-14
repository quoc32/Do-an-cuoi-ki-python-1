import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data.csv')

# Tạo hình (canvas) với kích thước 6x8 inch
plt.figure(figsize=(6, 8))

# Vẽ biểu đồ boxplot cho mức độ cholesterol
sns.boxplot(data=df, y='Chol', color="lightgreen")

# Thêm tiêu đề và nhãn cho các trục
plt.title('Mức Độ Cholesterol')
plt.ylabel('Cholesterol')

# Hiển thị biểu đồ
plt.show()
