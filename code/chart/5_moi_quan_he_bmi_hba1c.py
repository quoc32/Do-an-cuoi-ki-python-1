import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Mối quan hệ giữa BMI và HbA1c
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='HbA1c', y='BMI', hue='CLASS')
plt.title('Mối quan hệ giữa BMI và HbA1c')
plt.show() 