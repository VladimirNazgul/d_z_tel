from print_data import print_data
from return_data_file import data_file

def change_data():
  print_data()
  data = data_file()
  count_rows = len(data)
  number_row = int(input(f"Введите номер строки "
                         f"от 1 до {count_rows}: "))
  while number_row < 1 or number_row > count_rows:
    number_row = int(input(f"Ошибка!"
                           f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
  name = input("Введите имя: ")
  surname = input("Введите фамилию: ")
  phone = input("Введите дату рождения: ")
  adress = input("Введите город: ")
  data[number_row - 1] = f'{number_row};{name};{surname};{phone};{adress}\n'
  with open(f'data.csv', 'w', encoding='utf-8') as file:
      file.writelines(data)
  print("Данные успешно изменены!")