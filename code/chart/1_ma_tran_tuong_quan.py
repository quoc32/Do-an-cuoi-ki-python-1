import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Ma trận tương quan giữa các chỉ số sinh hóa
plt.figure(figsize=(12,8))
correlation_cols = ['Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']
sns.heatmap(df[correlation_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Ma trận tương quan giữa các chỉ số sinh hóa')
plt.show() 