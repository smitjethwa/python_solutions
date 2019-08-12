"""
WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers. Calculate the premium amount and display the vehicle details.

Identify the class name and attributes to represent vehicles. Drag and drop the chosen class name, attributes and methods into the appropriate section of the box shown below.

Write a Python program to implement the class chosen with its attributes and methods.


Note:

Consider all instance variables to be private and methods to be public
Include getter and setter methods for all instance variables
Display appropriate error message, if the vehicle type is invalid
Perform case sensitive string comparison
Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.

"""


class Vehicle:
	def __init__(self, vehicle_id, vehicle_type , vehicle_cost):
		self.__vehicle_id = vehicle_id
		self.__vehicle_type = vehicle_type
		self.__vehicle_cost = vehicle_cost

	def calculate_premium(self):
		if self._Vehicle__vehicle_type == 2:
			self.prm_prcnt = 2
			self.prm = self._Vehicle__vehicle_cost * 2//10
			self._Vehicle__vehicle_cost = self._Vehicle__vehicle_cost + self.prm

		elif self._Vehicle__vehicle_type == 4:
			self.prm_prcnt = 6
			self.prm = self._Vehicle__vehicle_cost * 6//100
			self._Vehicle__vehicle_cost = self._Vehicle__vehicle_cost + self.prm
	
	def display_vehicle_details(self):
		print("Vehicle ID :",self._Vehicle__vehicle_id)
		print("Vehicle Type :",self._Vehicle__vehicle_type)
		print("Premium Percent ",self.prm_prcnt)
		print("Premium AMount ",self.prm)
		print("Vehicle Cost ",self._Vehicle__vehicle_cost)

duke = Vehicle("DUKE 200",2,20000)
duke.calculate_premium()
duke.display_vehicle_details()