import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data.csv')

# Tạo hình (canvas) với kích thước 8x6 inch
plt.figure(figsize=(8, 6))

# Vẽ biểu đồ histogram cho phân phối HbA1c
sns.histplot(data=df, x='HbA1c', bins=10, kde=True, color="slateblue")

# Thêm tiêu đề và nhãn cho các trục
plt.title('Phân Phối HbA1c')
plt.xlabel('Mức độ HbA1c')
plt.ylabel('Tần suất')

# Hiển thị biểu đồ
plt.show()
