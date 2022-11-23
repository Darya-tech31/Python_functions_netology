documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


# Задача №1
def get_people():
    print('Поиск имени по номеру документа')
    doc_number = input('Введите номер документа: ')
    for enum in documents:
        if enum['number'] == doc_number:
            print('')
            print('Имя:', enum['name'])


def get_shelf():
    print('Поиск полки документа')
    doc_number = input('Введите номер документа: ')
    for enum in documents:
        if enum['number'] == doc_number:
            for enum_directories_key, enum_directories_value in directories.items():
                if doc_number in enum_directories_value:
                    print('')
                    print('Номер полки:', enum_directories_key)


def get_list_doc():
    print('Список документов:')
    for enum in documents:
        print(('"{}" "{}"').format(enum['number'], enum['name']))


def get_add_doc():
    print('Добавление нового документа')
    typedoc = input('Введите тип документа: ')
    numdoc = input('Введите номер документа: ')
    namedoc = input('Введите имя владельца: ')
    documents.append({'type': typedoc, 'number': numdoc, 'name': namedoc})
    print('')
    print('Документы: \n', documents)
    print('')
    dir_shelf = (input('Введите номер полки: '))
    print('')
    directories.get(dir_shelf).append(numdoc)
    print('')
    print('Перечень полок: \n', directories)


# Задача №2
def get_delete_doc():
    print('Удаление документа')
    doc_num = input('Введите номер документа: ')
    for enum in documents:
        if enum['number'] == doc_num:
            documents.remove(enum)
        for enum_directories_value in directories.values():
            if doc_num in enum_directories_value:
                enum_directories_value.remove(doc_num)
    print('')
    print('Документы: \n', documents)
    print('')
    print('Перечень полок: \n', directories)


def get_move():
    print('Перемещение документа')
    num_doc = input('Введите номер документа: ')
    new_shelf = input('Введите целевую полку: ')
    for enum_dir_value in directories.values():
        if num_doc in enum_dir_value:
            enum_dir_value.remove(num_doc)
    for enum_dir_key in directories.keys():
        if new_shelf in enum_dir_key:
            directories[enum_dir_key].append(num_doc)
    print('')
    print('Перечень полок: \n', directories)


def get_add_new_shelf():
    print('Добавлени новой полки')
    new_shelf = input('Введите новый номер полки: ')
    for enum_dir_key in directories.keys():
        if new_shelf == enum_dir_key:
            print('Такая полка уже есть!')
            return
    directories[new_shelf] = []
    print('')
    print('Перечень полок: \n', directories)


def main():
    while True:
        user_choice = input('Какую операцию вы хотите выполнить ?\n'
                            'p: выведет имя по номеру документа\n'
                            's: выведет номер полки по номеру документа\n'
                            'l: выведет список всех документов\n'
                            'a: добавит новый документ\n'
                            'd: удалит документ\n'
                            'm: переместит документ с текущей полки на целевую полку\n'
                            'as: добавить новую полку\n'
                            'q: завершение работы \n')
        if user_choice == 'p':
            print(get_people())
        elif user_choice == 's':
            print(get_shelf())
        elif user_choice == 'l':
            print(get_list_doc())
        elif user_choice == 'a':
            print(get_add_doc())
        elif user_choice == 'd':
            print(get_delete_doc())
        elif user_choice == 'm':
            print(get_move())
        elif user_choice == 'as':
            print(get_add_new_shelf())
        elif user_choice == 'q':
            print('Заверешние работы')
        # break
main()
