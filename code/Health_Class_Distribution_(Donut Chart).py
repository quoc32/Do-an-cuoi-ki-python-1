import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('data.csv')

# Đếm số lượng theo lớp sức khỏe
class_counts = df['CLASS'].value_counts()

# Vẽ đồ thị tròn cho phân phối lớp sức khỏe
plt.figure(figsize=(6, 6))
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Health Class Distribution')
plt.show()
