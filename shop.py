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
                # shop.update(price)
                
def remove_product():
    pass


def print_all_products(shop=shop):
    for group, array in shop.items():
        print("\nРаздел: " + group)
        for product, price in array.items():
            print(product + ' - ' + str(price))


def add_products_to_section(section, products):
    if section in shop:
        shop[section].update(products)
    # else:
    #     shop.append(section)
    #     shop[section].update(products)

products_count = int(input("Введите сколько товаров вы хотите добавить: "))
products_section = input("Введите название раздела: ")
user_products = {}

for i in range(products_count):
    product_name = input("Введите название товара: ")
    product_price = input("Введите цену товара: ")
    user_products.update({product_name: product_price})

add_products_to_section(products_section, user_products)
print(shop)

# while True:
#     choice = input("Добавить продукт? ")
#     if choice == "Да" or choice == "ДА" or choice == "да" or choice == "дА":
#         pass
        # category = input("Введите категорию: ")
        # product = input("Введите продукт: ")
        # price = input("Введите цену: ")
        # add_products(input("Введите категорию: "), input("Введите продукт: ") = int(input("Введите цену: ")))
        #add_products(category, product = price),

    # change(input("Введите продукт: "))
    # print_all_products()