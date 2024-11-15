{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu
# df = pd.read_csv('../../data/dataset/data.csv')

# # Vẽ biểu đồ tán xạ giữa Triglycerides (TG) và LDL, phân loại theo lớp sức khỏe
# plt.figure(figsize=(8, 6))
# sns.scatterplot(data=df, x='TG', y='LDL', hue='CLASS', palette='coolwarm', s=100, edgecolor='black')
# plt.title('Triglycerides vs. LDL by Health Class')
# plt.xlabel('Triglycerides (TG)')
# plt.ylabel('LDL')
# plt.legend(title='Class')
# plt.show()
}

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
df = pd.read_csv('../data/dataset/data.csv')
Triglycerides_LDL_By_Health_Class__fig = Figure(figsize=(6, 4), dpi=90) # <= fig obj ở đây
ax = Triglycerides_LDL_By_Health_Class__fig.add_subplot(111)
sns.scatterplot(data=df, x='TG', y='LDL', hue='CLASS', palette='coolwarm', s=100, edgecolor='black', ax=ax)
ax.set_title('Triglycerides vs. LDL by Health Class')
ax.set_xlabel('Triglycerides (TG)')
ax.set_ylabel('LDL')
ax.legend(title='Class')
