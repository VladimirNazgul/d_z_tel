from input_data import input_data
from print_data import print_data
from change_data import change_data
from delete_data import delete_data

def interface():
  command = None
  while command != 5:
    command = int(input("Здравствуйте! Это телефонный-справочник! \n"
                        "1 - Вывести данные \n"
                        "2 - Запись данных \n"
                        "3 - Изменение данных \n"
                        "4 - Удаление данных \n"
                        "5 - Выход \n"
                        "Введите число: "))
    command = check_number(command)
    if command == 1:
      print_data()
    elif command == 2:
       input_data()
    elif command == 3:
      change_data()
    elif command == 4:
      delete_data()

def check_number(n):
  while n < 1 or n > 5:
    print("Неправильный ввод")
    n = int(input("Введите число: "))
  return n