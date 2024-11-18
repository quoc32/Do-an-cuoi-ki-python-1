import pandas as pd
import plotly.express as px

# Đọc dữ liệu
df = pd.read_csv('clean.csv')

# Biểu đồ 3D: BMI, HbA1c, và Cholesterol
fig = px.scatter_3d(df, x='BMI', y='HbA1c', z='Chol',
                    color='CLASS',
                    title='Mối quan hệ 3D giữa BMI, HbA1c và Cholesterol')
fig.show() 