# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def create_sql_file_list(file_list):
    sql_file_list = []    
    for file in file_list:
        if file.endswith('.sql'):
            sql_file_list.append(file)
    return sql_file_list

def find_text_in_file(search_text, sql_file_list):
    new_sql_file_list = [] 
    for file in sql_file_list:
        with open(os.path.join(current_dir, migrations, file)) as f:
            read_data = f.read()
            if search_text in read_data.lower():
                new_sql_file_list.append(file)
    return new_sql_file_list
            
def print_find_files(new_sql_file_list):
    if len(new_sql_file_list) > 10:
        print('...большой список файлов...')
        print('Всего:', len(new_sql_file_list))
    elif len(new_sql_file_list) > 0:
        for file in new_sql_file_list:
            print(os.path.join(migrations, file))
        print('Всего:', len(new_sql_file_list))
    else:
        print('Файлов, содержащих введеный текст не найдено')
                        
if __name__ == '__main__':
    # ваша логика
    file_list = os.listdir(os.path.join(current_dir, migrations))
    sql_file_list = create_sql_file_list(file_list)
    while True:
        search_text = input('Введите строку:').lower()    
        new_sql_file_list = find_text_in_file(search_text, sql_file_list)
        print_find_files(new_sql_file_list)
        sql_file_list = new_sql_file_list
            
