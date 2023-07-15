class PhoneBook:

    def __init__(self, path: str = 'data.txt'):
        self.path = path
        self.data = []

    def open_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for contact in data:
            pb = {}
            new = contact.strip().split(';')
            pb['name'] = new[0]
            pb['phone'] = new[1]
            pb['comment'] = new[2]
            self.data.append(pb)
        print('\nТелефонная книга успешно загружена!\n')

    def save_file(self):
        with open("data.txt", 'r', encoding='utf-8') as data:
            for contact in data:
                data.write(data)

    def get(self):
        return self.data

    def new_contact(self, contact: dict):
        self.data.append(contact)
        print(f'/nКонтакт {contact.get("name")} успешно записан /n')

    def searh(self, word: str) -> dict | list:
        search_result = []
        for contact in self.data:
            for field in contact.values():
                if word in field:
                    search_result.append(contact)
        return search_result

    def change(self, i: int, new_value: dict):
        self.data[1] = new_value

    def delete(self, i: int):
        contact = self.data.pop(i)
        print(f'Контакт {contact.get("name")} успешно удален!')
