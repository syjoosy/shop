class Shop:
    name = 'Перекресток'
    info = 'Продаем продукты'


    def __init__(self):
        self.shop = []

    def add_product(self, product):
        self.shop.append(product)

    def add_product(self, product):
        self.shop.remove(product)
