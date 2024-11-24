
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Vẽ biểu đồ hộp cho phân phối tuổi theo lớp sức khỏe
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='CLASS', y='AGE', palette='Set3')
plt.title('Age Distribution by Health Class')
plt.xlabel('Class')
plt.ylabel('Age')
plt.show()
