import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Đọc dữ liệu với đường dẫn tương đối
    df = pd.read_csv('../../data/clean.csv')

    # Thiết lập style cho biểu đồ
    plt.style.use('classic')
    
    # Tạo biểu đồ violin plot
    plt.figure(figsize=(12, 7))
    sns.violinplot(x='CLASS', y='HbA1c', data=df, palette='Set3')
    
    # Thiết lập tiêu đề và nhãn
    plt.title('Phân bố HbA1c theo phân loại béo phì', fontsize=14, pad=15)
    plt.xlabel('Phân loại béo phì', fontsize=12)
    plt.ylabel('Chỉ số HbA1c (%)', fontsize=12)
    
    # Xoay nhãn trục x và điều chỉnh layout
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Hiển thị biểu đồ
    plt.show()

except FileNotFoundError:
    print("Không tìm thấy file dữ liệu. Vui lòng kiểm tra lại đường dẫn.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {str(e)}") 