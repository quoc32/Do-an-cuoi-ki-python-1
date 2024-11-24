import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('../../data/clean.csv')

# Mối quan hệ giữa BMI và các chỉ số lipid
lipids = ['Chol', 'TG', 'HDL', 'LDL', 'VLDL']
plt.figure(figsize=(15,10))
for i, lipid in enumerate(lipids, 1):
    plt.subplot(2,3,i)
    sns.scatterplot(data=df, x='BMI', y=lipid, hue='CLASS', alpha=0.6)
    plt.title(f'BMI vs {lipid}')
plt.tight_layout()
plt.show() 