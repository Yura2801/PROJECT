from db import create_products_database,add_product_to_database,find_product
from db import SalesSystem
import datetime

# Вызов функции для создания базы данных продуктов
create_products_database()

# Пример использования функции для добавления товара
add_product_to_database("Яблоко", 40, 5)


# Пример поиска товара
if __name__ == "__main__":
    search_name = input("Введите название товара для поиска: ")
    product_info = find_product(search_name)
    if product_info:
        print(f"Найден товар: {product_info['name']}, Цена: {product_info['price']}, Количество: {product_info['quantity']}")
    else:
        print("Товар не найден")




# Оформление продажи
def main():
    system = SalesSystem()

    # Добавление товаров в чек
    system.add_to_cart("Часы-будильник", 4)
    system.add_to_cart("Футбольный мяч", 5)
    system.add_to_cart("Наушники Bluetooth", 4)

    # Расчет итоговой суммы
    total_price = system.calculate_total()
    print(f"Итоговая сумма: {total_price}")

    # Применение скидки
    system.apply_discount(5)

    # Обработка платежа
    amount_paid = 70
    change = system.process_payment(amount_paid)
    print(f"Сдача: {change}")

if __name__ == "__main__":
    main()



