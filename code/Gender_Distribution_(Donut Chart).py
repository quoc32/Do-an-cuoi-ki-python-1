import matplotlib.pyplot as plt
import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data.csv')

# Tạo hình (canvas) với kích thước 6x6 inch
plt.figure(figsize=(6, 6))

# Vẽ biểu đồ donut với phân phối giới tính
plt.pie(df['Gender'].value_counts(), labels=df['Gender'].value_counts().index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.gca().add_artist(plt.Circle((0, 0), 0.70, fc='white'))  # Tạo phần trung tâm rỗng để tạo hiệu ứng donut

# Thêm tiêu đề cho biểu đồ
plt.title('Phân Phối Giới Tính')

# Hiển thị biểu đồ
plt.show()
