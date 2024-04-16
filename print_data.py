def print_data():
  with open(f'data.csv', 'r', encoding='utf-8') as f:
    data = f.readlines()
  print(f"Вывод данных:\n"
              f"{''.join(data)}")