from data_create import name_data, surname_data, phone_data, address_data
from print_data import print_data
from return_data_file import data_file

def input_data():
  name = name_data()
  surname = surname_data()
  phone = phone_data()
  address = address_data()
  data = data_file()
  number_row = len(data) + 1
  var = int(input(f"Вы подтверждаете ввод новыхданных?\n"
  f"1 - да \n"
  f"{name};{surname};{phone};{address}\n"
  f"0 - нет \n"
  f"Выведется имеющийся список \n"))

  while var != 1 and var != 0:
    print("Неправильный ввод")
    var = int(input('Введите число: '))
  
  if var == 0:
     print_data()
  elif var == 1:
    with open(f'data.csv', 'a', encoding='utf-8') as f:
      f.write(f"{number_row};{name};{surname};{phone};{address}\n")
  print("Данные успешно записаны!")

