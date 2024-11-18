import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('clean.csv')

# Phân bố tuổi theo CLASS
plt.figure(figsize=(10,6))
sns.violinplot(x='CLASS', y='AGE', data=df)
plt.title('Phân bố tuổi theo phân loại béo phì')
plt.xticks(rotation=45)
plt.show() 