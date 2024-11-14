import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('data.csv')

# Vẽ biểu đồ tán xạ (scatter plot) giữa tuổi và mức cholesterol với đường xu hướng
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x='AGE', y='Chol', scatter_kws={'color': 'teal'}, line_kws={'color': 'orange'})
plt.title('Age vs. Cholesterol')
plt.xlabel('Age')
plt.ylabel('Cholesterol Level')
plt.show()
