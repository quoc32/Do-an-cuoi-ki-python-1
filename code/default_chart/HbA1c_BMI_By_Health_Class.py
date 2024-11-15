{
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Đọc dữ liệu
# df = pd.read_csv('../../data/dataset/data.csv')

# # Vẽ biểu đồ tán xạ giữa HbA1c và BMI, phân loại theo lớp sức khỏe
# HbA1c_BMI_By_Health_Class__fig = plt.figure(figsize=(8, 6)) # <= fig obj ở đây
# sns.scatterplot(data=df, x='HbA1c', y='BMI', hue='CLASS', palette='Set1', s=100, edgecolor='black')
# plt.title('HbA1c vs. BMI by Health Class')
# plt.xlabel('HbA1c Level')
# plt.ylabel('BMI')
# plt.legend(title='Class')
# plt.show()
}

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure
df = pd.read_csv('../data/dataset/data.csv')
HbA1c_BMI_By_Health_Class__fig = Figure(figsize=(6, 4), dpi=90) # <= fig obj ở đây
ax = HbA1c_BMI_By_Health_Class__fig.add_subplot(111)
sns.scatterplot(data=df, x='HbA1c', y='BMI', hue='CLASS', palette='Set1', s=100, edgecolor='black', ax=ax)
ax.set_title('HbA1c vs. BMI by Health Class')
ax.set_xlabel('HbA1c Level')
ax.set_ylabel('BMI')
ax.legend(title='Class')
