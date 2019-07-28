# INFYTQ OOP Soln, (Assignment)

class Customer():
		def __init__(self, bill_amount, customer_name):
			self.CustomerName = customer_name
			self.BillAmount = bill_amount

		def purchases(self):
			self.BillAmount = self.BillAmount - (self.BillAmount * (5//100))

		def pays_bill(self):
			print(self.CustomerName,"pays bill amount of Rs.",self.BillAmount)

rohan = Customer(5000,"rohan")
rohan.purchases()
rohan.pays_bill()
