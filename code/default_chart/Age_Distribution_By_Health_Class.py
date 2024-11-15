{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu
# df = pd.read_csv('../../data/dataset/data.csv')

# # Vẽ biểu đồ hộp cho phân phối tuổi theo lớp sức khỏe
# plt.figure(figsize=(8, 6))
# sns.boxplot(data=df, x='CLASS', y='AGE', palette='Set3')
# plt.title('Age Distribution by Health Class')
# plt.xlabel('Class')
# plt.ylabel('Age')
# plt.show()
}

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
df = pd.read_csv('../data/dataset/data.csv')
Age_Distribution_By_Health_Class__fig = Figure(figsize=(6, 4), dpi=90) # <= fig obj ở đây
ax = Age_Distribution_By_Health_Class__fig.add_subplot(111)
sns.boxplot(data=df, x='CLASS', y='AGE', hue='CLASS', palette='Set3', ax=ax, dodge=False, legend=False)
ax.set_title('Age Distribution by Health Class')
ax.set_xlabel('Class')
ax.set_ylabel('Age')
