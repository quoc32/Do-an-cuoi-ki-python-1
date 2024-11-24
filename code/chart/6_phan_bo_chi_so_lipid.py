import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Biểu đồ boxplot cho các chỉ số lipid
lipids = ['Chol', 'TG', 'HDL', 'LDL', 'VLDL']
plt.figure(figsize=(15,8))
for i, lipid in enumerate(lipids, 1):
    plt.subplot(2,3,i)
    sns.boxplot(x='CLASS', y=lipid, data=df)
    plt.xticks(rotation=45)
    plt.title(f'Phân bố {lipid} theo nhóm béo phì')
plt.tight_layout()
plt.show() 