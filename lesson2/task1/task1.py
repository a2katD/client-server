import csv
import chardet
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as f:
            data_bytes = f.read()
            file_data = chardet.detect(data_bytes)
            text = data_bytes.decode(encoding=file_data['encoding'])

            os_prod_list.append(re.search('Изготовитель системы:\s*\S*', text).group().split().pop(-1))
            os_name_list.append(re.search('Название ОС:\s*\S*', text).group().split().pop(-1))
            os_code_list.append(re.search('Код продукта:\s*\S*', text).group().split().pop(-1))
            os_type_list.append(re.search('Тип системы:\s*\S*', text).group().split().pop(-1))

    main_data.append(['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])
    temp = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for i in range(3):
        main_data.append([line[i] for line in temp])
    return main_data


def write_to_csv(file_csv):
    main_data = get_data()
    with open(file_csv, 'w', encoding='utf-8') as file:
        file_writer = csv.writer(file)
        for line in main_data:
            file_writer.writerow(line)


write_to_csv('result.csv')
