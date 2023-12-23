def create_products_database():
    # Данные о продуктах
    products = [
        {"name": "Часы-будильник", "price": 25, "quantity": 10},
        {"name": "Футбольный мяч", "price": 15, "quantity": 20},
        {"name": "Книга 'Война и мир'", "price": 30, "quantity": 15},
        {"name": "Наушники Bluetooth", "price": 50, "quantity": 8}
    ]

    # Запись данных в текстовый файл
    with open('products_database.txt', 'w' , encoding='utf-8') as file:
        file.write("Имя продукта,Цена,Количество\n")
        for product in products:
            line = f"{product['name']},{product['price']},{product['quantity']}\n"
            file.write(line)

if __name__ == "__main__":
    create_products_database()


def add_product_to_database(name, price, quantity):
    # Открываем файл для добавления новых данных (режим 'a' - append)
    with open('products_database.txt', 'a', encoding='utf-8') as file:
        # Формируем строку с данными о новом товаре
        new_product = f"{name},{price},{quantity}\n"
        # Записываем данные о новом товаре в файл
        file.write(new_product)


def find_product(name):
    with open('products_database.txt', 'r', encoding='utf-8') as file:
        # Читаем строки из файла
        lines = file.readlines()

        # Перебираем строки и ищем товар по имени
        for line in lines[1:]:  # Пропускаем первую строку с заголовками
            product_data = line.strip().split(',')
            if product_data[0] == name:
                return {
                    'name': product_data[0],
                    'price': float(product_data[1]),
                    'quantity': int(product_data[2])
                }
        # Если товар не найден
        return None


class SalesSystem:
    def __init__(self):
        self.cart = {}  # Словарь для хранения товаров и их количества в чеке
        self.prices = {"Часы-будильник": 25, "Футбольный мяч": 15, "Книга 'Война и мир'": 30, "Наушники Bluetooth": 50}
        self.discount = 0  # Скидка
        self.total = 0  # Итоговая сумма

    def add_to_cart(self, product, quantity):
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    def calculate_total(self):
        self.total = sum(self.prices.get(item, 0) * quantity for item, quantity in self.cart.items())
        return self.total - self.discount

    def apply_discount(self, discount_amount):
        self.discount = discount_amount

    def process_payment(self, amount_paid):
        change = amount_paid - self.calculate_total()
        self.update_sales_history()
        return change

    def update_sales_history(self):
        # Здесь можно добавить логику для обновления истории продаж, например, запись в файл или базу данных
        pass



