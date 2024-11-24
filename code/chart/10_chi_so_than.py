import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Phân bố Urea và Creatinine theo CLASS
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
sns.boxplot(x='CLASS', y='Urea', data=df)
plt.title('Phân bố Urea theo CLASS')
plt.xticks(rotation=45)

plt.subplot(1,2,2)
sns.boxplot(x='CLASS', y='Cr', data=df)
plt.title('Phân bố Creatinine theo CLASS')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 