import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('clean.csv')

# Phân bố HbA1c theo CLASS
plt.figure(figsize=(10,6))
sns.violinplot(x='CLASS', y='HbA1c', data=df)
plt.title('Phân bố HbA1c theo phân loại béo phì')
plt.xticks(rotation=45)
plt.show() 