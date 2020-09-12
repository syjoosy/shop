from django import *

money = 500
bag = []
shop = [
            ["макароны", 100],
            ["гречка", 88],
            ["мясо", 500],
            ["лимон", 200],
        ]
warehouse = []

file = open("array.txt" , 'a')
for line in shop:
    product = line[0]
    price = line[1]
    file.write(product + " : " + str(price) + "\n")
file.close()

print("Добро пожаловать в наш магазин")
name = input("Введите своё имя: ")
if name == "Админ" or name == "админ" or name == "АДМИН" or name == "аДМИН":
    print("Добро пожаловать в админ панель: ")
    print("В магазине имеются товары: ")
    for array in shop:
        print(array[0], "-", array[1], 'p')
    while True:
        choice_3 = input("Добавить/удалить товар? ")
        if choice_3 == "Добавить" or choice_3 == "ДОБАВИТЬ" or choice_3 == "добавить":
            product = input("Введите название продукта: ")
            price = input("Введите цену: ")
            file = open("array.txt" , 'a')
            file.write(product + " : " + str(price) + "\n")
            file.close()
            warehouse.append(product)
            warehouse.append(price)
            shop.append(warehouse)
        elif choice_3 == "Удалить" or choice_3 == "УДАЛИТЬ" or choice_3 == "удалить":
            delete = input("Введите продукт, который желаете удалить: ")
            for array in shop:
                test = array[0]
                if test == delete:
                    print(test, " = ",delete)
                    array.pop(0)
                    array.pop(0)
                    print("Товар ", delete, " удален из магазина")
                    print(shop)
        else:
            break


choice = input("Будете что-нибудь приобретать? ")
while choice == "ДА" or choice == "да" or choice == "Да" or choice == "дА":
    
    print("В магазине имеются товары: ")
    for array in shop:
        print(array[0], "-", array[1], 'p')

    print("Сейчас у вас ", money, " рублей")
    print("В вашей сумке сейчас находятся следующие товары: ")
    for i in bag:
        print(i)
    
    if money <= 88:
        print("У вас недостаточно средств для покупки в нашем магазине ")
        break
    choice_2 = input("Что будете приобретать? ")

    for array in shop:

        if choice_2 in array[0]:

            if money >= array[1]:
                money -= array[1]
                bag.append(array[0])
                print("С вашего счета списано", array[1], ' рублей в ', array[0], " добавлен в вашу корзину ")
                continue

            else:
                print("У вас недостаточно средств для покупки ")
        
        elif choice_2 not in array[0]:
            continue

        else:
            print("Такого товара в магазине нет! ")

else:
    print("Выход из программы магазина ")