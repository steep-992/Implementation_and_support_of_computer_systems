import pandas as pd

excel_file_path = r'D:\задания Касьяненко\adjutanted.xlsx'

try:
    df = pd.read_excel(excel_file_path)

    print(df.to_string())

except FileNotFoundError:
    print(f"Файл не найден: {excel_file_path}")
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")