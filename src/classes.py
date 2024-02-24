class Category:
	name: str
	description: str
	goods: list

	category_counter = 0
	unique_goods_counter = 0
	goods = []

	def __init__(self, name, description, goods):
		self.name = name
		self.description = description
		self.__goods = goods
		Category.category_counter += 1
		Category.unique_goods_counter += len(set(goods))

	@property
	def get_goods(self):
		result = ''
		for prod in self.__goods:
			result += f"{prod.name}, {prod.price} руб. Остаток: {prod.amt_in_stock} шт."
		return print(result)

	@get_goods.setter
	def get_goods(self, product):
		self.__goods.append(product)

	@property
	def goods_list(self):
		return self.__goods


class Product:
	name: str
	description: str
	price: float
	amt_in_stock: int

	def __init__(self, name, description, price, amt_in_stock):
		self.name = name
		self.description = description
		self._price = price
		self.amt_in_stock = amt_in_stock

	@classmethod
	def make_product(cls, name, description, price, amt_in_stock, goods):
		for i in goods:
			if name == i.name:
				amt_in_stock += i.amt_in_stock
				if price < i.price:
					price = i.price
		return cls(name, description, price, amt_in_stock)

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, value):
		if value <= 0:
			print("Цена введена некорректно!")
		else:
			self._price = value


# phones = Category('Телефоны', 'Хорошие', [])
# iphone = Product('iPhone', 'Стильный телефон', 150, 5)
# android = Product('Xiaomi', 'Умный телефон', 75, 10)
#
# print(phones.name)
# print(phones.description)
# print(phones.goods)
# print(phones.category_counter)
# print(phones.unique_goods_counter)
#
# print(iphone.name)
# print(iphone.price)
# iphone.price = 0
# print(iphone.price)
# iphone.price = 200
# print(iphone.price)
# print(iphone.description)
# print(iphone.amt_in_stock)
#
# print(android.name)
# print(android.price)
# print(android.description)
# print(android.amt_in_stock)
