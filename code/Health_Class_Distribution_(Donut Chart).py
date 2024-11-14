import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('/Users/coffat/Documents/Do_an_cuoi_ki_python/Do-an-cuoi-ki-python-1/data/data.csv')

# Lấy dữ liệu phân phối theo lớp sức khỏe
class_counts = df['CLASS'].value_counts()

# Vẽ biểu đồ donut cho phân phối lớp sức khỏe
plt.figure(figsize=(6, 6))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#ff9999'])
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Health Class Distribution')
plt.show()
