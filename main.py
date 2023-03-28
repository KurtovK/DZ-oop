from typing import Dict
#Задание 1.
 #дату рождения, контактный телефон, город, страну, домашний адрес.
#Реализуйте конструктор по умолчанию и метод для вывода данных.
#Реализуйте доступ к отдельным полям класса через методы класса (геттеры
#и сеттеры).


class Human:
    name: Dict[str: str]
    data_birthday: Dict[str, str]
    phone: str
    country:str
    city: str
    address: str

    def __init__(self,name: Dict[str,str],data_birthday: Dict[str, str], phone: str,
                country:str, city: str, address: str):
        self.name = name
        self.data_birthday = data_birthday
        self.phone = phone
        self.city = city
        self.address = address
    def __str__(self):
        return  f"ФИО: {list(self.name.values())}\n" \
                f"Дата рождения: {list(self.data_birthday.values())}\n"\
                f"Номер телефона: {self.phone}\n" \
                f"Страна: {self.city}\n"\
                f"Адресс: {self.address}\n"

def execute_application():
    pass


if __name__=="__main__":
    execute_application()