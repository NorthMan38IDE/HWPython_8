def menu() -> int:
    print('\nЭто телефонный справочник. Выбери функцию которую нужно совершить:'
          '\n1. Открыть файл'
          '\n2. Сохранить файл'
          '\n3. Показать контакты'
          '\n4. Добавить контакт'
          '\n5. Изменить контакт'
          '\n6. Найти контакт'
          '\n7. Удалить контакт'
          '\n8. Выход')
    while True:
        choice = input('Введите номер неоходимой функции: ')
        if choice.isdigit() and (0 < int(choice) < 9):
            return int(choice)


def show_contact(data: list):
    print()
    if data:
        for i, contact in enumerate(data, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print()
    else:
        print('\nТелефонная книга не открыта или пуста\n')


def new_contact() -> dict:
    print()


    name = input('Введите имя и фамилию контакта: ')
    valid = False
    while not valid:
        try:
            phone = input('Введите номер телефона: ')
            if len(phone) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone = int(phone)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    comment = input('Введите коментарий: ')
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def change_contact(book: list) -> tuple:
    show_contact(book)
    choice = int(input('Введите номер контакта, который хотите изменить: '))
    name = input('Введите новое имя или Enter: ')
    phone = input('Введите новый телефон или Enter: ')
    comment = input('Введите новый коментарий или Enter: ')
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                        'phone': phone if phone else book[choice - 1].get('phone'),
                        'comment': comment if comment else book[choice - 1].get('comment')}


def select_to_delete(book: list):
    show_contact(book)
    return int(input('Введите номер элемента, который нужно удалить: ')) - 1


def input_request(text: str) -> str:
    return input(f'Введите {text}: ')


def goodbye():
    print('Выход осуществлен')
