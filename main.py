from typing import Dict
#Задание 2.
#Реализуйте класс «Книга». Необходимо хранить в полях класса:
#название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
#конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
#отдельным полям класса через методы класса (геттеры и сеттеры).
 class Book:
     name: str
     author: str
     year: str
     publisher: str
     qenre: str
     price: float

     def __init__(self, name: str, author: str, year: str, publisher: str, genre: str, price: float):
         self.name = name
         self.author = author
         self.year =year
         self.publisher = publisher
         self.qenre = genre
         self.price = price

    def __str__(self):
        return f"Название: {self.name}\n" \
                f"Автор: {self.author}\n" \
                f"Год издания: {self.year}\n" \
                f"Издание: {self.publisher}\n" \
                f"Жанр: {self.genre}\n"\
                f"Цена: {self.price}\n"



def execute_application():
    pass





if __name__=="__main__":
    execute_application()