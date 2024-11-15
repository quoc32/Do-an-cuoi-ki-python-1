{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu
# df = pd.read_csv('../../data/dataset/data.csv')

# # Vẽ biểu đồ tán xạ (scatter plot) giữa tuổi và mức cholesterol với đường xu hướng
# fig_age_chol =  plt.figure(figsize=(8, 6)) # <= fig object
# sns.regplot(data=df, x='AGE', y='Chol', scatter_kws={'color': 'teal'}, line_kws={'color': 'orange'})
# plt.title('Age vs. Cholesterol')
# plt.xlabel('Age')
# plt.ylabel('Cholesterol Level')
# plt.show()
}

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
df = pd.read_csv('../data/dataset/data.csv')
Age_And_Cholesterol__fig = Figure(figsize=(6, 4), dpi=90) # <= fig obj ở đây
ax = Age_And_Cholesterol__fig.add_subplot(111)
sns.regplot(data=df, x='AGE', y='Chol', scatter_kws={'color': 'teal'}, line_kws={'color': 'orange'}, ax=ax)
ax.set_title('Age vs. Cholesterol')
ax.set_xlabel('Age')
ax.set_ylabel('Cholesterol Level')

