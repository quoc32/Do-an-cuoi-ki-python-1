import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('data.csv')

# Vẽ biểu đồ tán xạ giữa Triglycerides (TG) và LDL, phân loại theo lớp sức khỏe
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='TG', y='LDL', hue='CLASS', palette='coolwarm', s=100, edgecolor='black')
plt.title('Triglycerides vs. LDL by Health Class')
plt.xlabel('Triglycerides (TG)')
plt.ylabel('LDL')
plt.legend(title='Class')
plt.show()
