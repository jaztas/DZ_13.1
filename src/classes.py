class Category():
    name: str
    description: str
    __goods: list

    category_counter = 0
    unique_goods_counter = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = []

    def add_product(self, product):
        self.__goods.append(product)
        print(f"Продукт '{product.name}' добавлен в категорию '{self.name}'.")

    def get_goods(self):
        return self.__goods


class Product():
    name: str
    description: str
    price: float
    amt_in_stock: int

    def __init__(self, name, description, price, amt_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.amt_in_stock = amt_in_stock
