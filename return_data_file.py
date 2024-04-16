def data_file():
    with open(f'data.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data
