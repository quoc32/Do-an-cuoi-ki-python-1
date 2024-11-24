import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Biểu đồ KDE về phân bố BMI theo giới tính và CLASS
plt.figure(figsize=(10,6))
sns.kdeplot(data=df, x='BMI', hue='CLASS', multiple="layer")
plt.title('Phân bố mật độ BMI theo phân loại béo phì')
plt.show() 