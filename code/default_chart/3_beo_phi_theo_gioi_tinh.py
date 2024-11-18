import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('clean.csv')

# Biểu đồ cột về tỷ lệ các nhóm béo phì theo giới tính
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='CLASS', hue='Gender')
plt.title('Phân bố các nhóm béo phì theo giới tính')
plt.xticks(rotation=45)
plt.show() 