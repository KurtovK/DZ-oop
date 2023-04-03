from typing import Dict
#Задание 1.
 #дату рождения, контактный телефон, город, страну, домашний адрес.
#Реализуйте конструктор по умолчанию и метод для вывода данных.
#Реализуйте доступ к отдельным полям класса через методы класса (геттеры
#и сеттеры).


class Human:
    name: Dict[str: str]
    birthday: Dict[str, str]
    phone: str
    country: str
    city: str
    address: str

    def __init__(self,name: Dict[str, str], birthday: Dict[str, str], phone: str,
                     country:str, city: str, address: str):
        self.name = name.copy()
        self.birthday = birthday.copy()
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address.copy()
    def __str__(self):
        return  f"ФИО: {list(self.name.values())}\n" \
                f"Дата рождения: {list(self.birthday.values())}\n"\
                f"Номер телефона: {self.phone}\n" \
                f"Страна: {self.country}\n"\
                f"Город: {self.city}\n" \
                f"Адресс: {self.address}\n"

def execute_application():
    human1 = Human({"first_name": "Куртов", "last_name": "К.Д."}, {"day": "21", "month": "02", "year": "1987"},
                   "910-979-23-19", "Россия", "Ярославль", "ул. Панина, д. 17, кв. 0")
    humans = []
    humans.append(human1)
    for human in humans:
        print(human)


if __name__=="__main__":
    execute_application()
