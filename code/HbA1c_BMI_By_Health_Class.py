import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('data.csv')

# Vẽ biểu đồ tán xạ giữa HbA1c và BMI, phân loại theo lớp sức khỏe
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='HbA1c', y='BMI', hue='CLASS', palette='Set1', s=100, edgecolor='black')
plt.title('HbA1c vs. BMI by Health Class')
plt.xlabel('HbA1c Level')
plt.ylabel('BMI')
plt.legend(title='Class')
plt.show()
