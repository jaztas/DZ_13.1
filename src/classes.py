class Category():
	name: str
	description: str
	goods: list

	category_counter = 0
	unique_goods_counter = 0

	def __init__(self, name, description, goods):
		self.name = name
		self.description = description
		self.__goods = goods


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
