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

    @classmethod
    def add_product(cls, product):
        cls.__goods.append(product)
        print(f"Продукт '{product.name}' добавлен в категорию '{cls.name}'.")

    @property
    def get_goods(self):
        result = ""
        for product in self.__goods:
            result += f"{product.name}, {product.price} руб. Остаток: {product.amt_in_stock} шт.\n"
        return result


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

    @staticmethod
    def create_product(name, description, price, amt_in_stock):
        new_product = Product(name, description, price, amt_in_stock)
        return new_product


