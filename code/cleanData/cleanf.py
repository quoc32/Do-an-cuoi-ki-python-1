import pandas as pd

FILE_PATH = '../data/dataset/data.csv'
OUTFILE_PATH = '../data/clean.csv'

def main(frame=None):
    # Bật nhãn thông báo đang Cleaning...
    if frame:
        frame.toggleOnLoading()

    data = pd.read_csv(FILE_PATH)

    data = data.drop_duplicates()

    missing_counts = data.isnull().sum(axis=1)
    numeric_cols = data.select_dtypes(include=['number']).columns
    for index, count in missing_counts.items():
        if count < 4:
            data.loc[index, numeric_cols] = data.loc[index, numeric_cols].fillna(0)
        else:
            data = data.drop(index)


    def normalize_string_char(text):
        if isinstance(text, str):
            return text.strip().lower()


    for col in data.columns:
        if data[col].dtype == object:
            data[col] = data[col].apply(normalize_string_char)

    text_columns = data.select_dtypes(include=['object']).columns
    data[text_columns] = data[text_columns].fillna('')

    data = data[(data['AGE'] > 0) & (data['AGE'] <= 120)]
    data['CLASS'] = data['CLASS'].apply(lambda x: x.replace('d', ''))
    data = data[(data['BMI'] >= 10) & (data['BMI'] <= 50)]

    data['ID'] = data['ID'].astype(int)
    data['No_Pation'] = data['No_Pation'].astype(int)
    data['AGE'] = data['AGE'].astype(int)
    data['BMI'] = data['BMI'].astype(float)

    data = data.sort_values(by='ID')
    data = data.reset_index(drop=True)

    for col in numeric_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]


    def move_duplicate_ids_to_end(data, id_col='ID'):
        max_id = data[id_col].max()
        duplicated_ids = data[data.duplicated(subset=[id_col], keep='first')]
        data = data.drop(duplicated_ids.index)

        # Gán ID mới cho các hàng bị di chuyển (ID bằng max_id + 1, max_id + 2, ...)
        for i in range(len(duplicated_ids)):
            max_id += 1
            duplicated_ids.iloc[i, duplicated_ids.columns.get_loc(id_col)] = max_id
        # Ghép lại DataFrame với các hàng đã di chuyển
        data = pd.concat([data, duplicated_ids], ignore_index=True)
        return data


    def check_duplicate_no_pation(data, no_pation_col='No_Pation'):
        if data.duplicated(subset=[no_pation_col]).any():
            data = data.drop_duplicates(subset=[no_pation_col], keep='first')
        return data


    sorted_data = move_duplicate_ids_to_end(data)
    sorted_data = check_duplicate_no_pation(sorted_data)

    def categorize_bmi(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Normal'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

    # Thêm cột BMI_CATEGORY
    sorted_data['BMI_CATEGORY'] = sorted_data['BMI'].apply(categorize_bmi)
    sorted_data.to_csv(OUTFILE_PATH, index=False)

    # Tắt nhãn thông báo đang Cleaning...
    if frame:
        frame.toggleOffLoading()


if __name__ == "__main__":
    main()