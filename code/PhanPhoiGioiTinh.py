import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('/Users/coffat/Documents/Do_an_cuoi_ki_python/Do-an-cuoi-ki-python-1/data/data.csv')

# Đếm số lượng nam và nữ
gender_counts = df['Gender'].value_counts()

# Vẽ biểu đồ donut cho phân phối giới tính
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Gender Distribution')
plt.show()
