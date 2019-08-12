class Flower:
	def __init__(self, flower_name, quantity):
		self.flower_name = flower_name
		self.quantity = quantity
		self.flowers = ["orchid","rose","jasmine"]
		self.price_dict = {"orchid":25,"rose":20,"jasmine":5}
		self.stock_dict = {"orchid":100,"rose":100,"jasmine":100}
		self.alert_dict = {"orchid":15,"rose":25,"jasmine":40}
		self.wallet_balance = 0

	def validate_flower(self):
		if self.flower_name in self.flowers :
			return True
		else:
			return False

	def validate_stock(self):
		if self.quantity < self.stock_dict[self.flower_name] :
			return True
		else:
			return False

	def update_stock(self):
		self.stock_dict[self.flower_name] = self.stock_dict[self.flower_name] - self.quantity

	def check_level(self):
		if self.stock_dict[self.flower_name] <= self.alert_dict[self.flower_name]:
			return True
		else:
			return False

	def sell_flower(self):
		if self.validate_stock() == True and self.validate_flower() == True :
			self.update_wallet() 
			self.update_stock()
			if self.check_level() == True :
				print("ALERT !!! "+self.flower_name +" Stock Below level")
			self.order_summary()
			self.stock_summary()
		else:
			print("Cant sell flowers")

	def update_wallet(self):
		self.wallet_balance = self.price_dict[self.flower_name] * self.quantity
		#print("wallet balance ",self.wallet_balance)

	def order_summary(self):
		print(" ----- ORDER SUMMARY ------")
		print("FLower To Buy :- ",self.flower_name)
		print("quantity of Flowers :- ",self.quantity)
		print("Price per Unit",self.price_dict[self.flower_name])
		print(" Bill :- ",self.wallet_balance)

	def stock_summary(self):
		print(" ----- STOCK SUMMARY ------")
		print("First Stock")
		print(self.stock_dict)

item1 = Flower("orchid",10)
item1.sell_flower()
