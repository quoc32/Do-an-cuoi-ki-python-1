import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Phân bố BMI theo CLASS
plt.figure(figsize=(10,6))
sns.boxplot(x='CLASS', y='BMI', data=df)
plt.title('Phân bố BMI theo phân loại béo phì')
plt.xticks(rotation=45)
plt.show() 