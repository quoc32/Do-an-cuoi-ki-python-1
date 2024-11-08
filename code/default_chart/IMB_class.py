import matplotlib.pyplot as plt

def plot_bmi_vs_class(df):
    classes = df['CLASS'].unique()
    colors = ['blue', 'orange', 'green', 'red']  # Màu cho từng lớp (có thể tùy chỉnh)
    
    plt.figure(figsize=(8, 6))
    for i, class_label in enumerate(classes):
        class_data = df[df['CLASS'] == class_label]
        plt.scatter(class_data['BMI'], [class_label] * len(class_data), 
                    color=colors[i % len(colors)], label=f'CLASS {class_label}')
    
    # Cài đặt nhãn và tiêu đề
    plt.xlabel('BMI')
    plt.ylabel('CLASS')
    plt.title('Relationship between BMI and CLASS')
    plt.legend(title='CLASS')
    plt.grid(True)
    plt.show()