from return_data_file import data_file
from print_data import print_data

def delete_data():
  print_data()
  data = data_file()
  count_rows = len(data)
  if count_rows == 0:
    print("Файл пусто!")
  else:
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
          number_row = int(input(f"Ошибка!"
                                 f"Введите номер строки "
                                 f"от 1 до {count_rows}: "))
    del data[number_row - 1]
    data = [f'{i + 1};{data[i].split(";")[1]};'
            f'{data[i].split(";")[2]};'
            f'{data[i].split(";")[3]};'
            f'{data[i].split(";")[4]}'
            for i in range(len(data))]
    with open(f'data.csv', 'w', encoding='utf-8') as file:
            file.writelines(data)
    print("Строка успешно удалена!")
  