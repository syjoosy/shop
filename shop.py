shop = {
    'мучное': {
        'хлеб': 200
    }
}

def add_products(user_group, shop = shop, **products):
    if user_group in shop:
        shop[user_group].update(products)

    elif user_group not in shop:
        shop.update({user_group:{}})
        shop[user_group].update(products)

    else:
        return "Ошибка"

    return shop

def change(products):
    for group, array in shop.items():
        for product, price in array.items():
            if product == products:
                price = input("Введите новую цену для продукта {} ".format(product))
                

def print_all_products(shop=shop):
    for group, array in shop.items():
        print("\nРаздел: " + group)
        for product, price in array.items():
            print(product + ' - ' + str(price))
            
while True:
    choice = input("Добавить продукт? ")
    if choice == "Да" or choice == "ДА" or choice == "да" or choice == "дА":
        pass
        # category = input("Введите категорию: ")
        # product = input("Введите продукт: ")
        # price = input("Введите цену: ")
        # add_products(input("Введите категорию: "), input("Введите продукт: ") = int(input("Введите цену: ")))

    change(input("Введите продукт: "))
    print_all_products()