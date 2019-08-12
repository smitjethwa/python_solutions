class Student :
	def __init__(self, student_name , student_age, student_marks):
		self.student_name = student_name
		self.student_age = student_age
		self.student_marks = student_marks

	def validate_age(self):
		if self.student_age >= 20 :
			#print("Student age",self.student_age)
			return True
		else:
			return False
			#print("Go Home Kiddo !!!")

	def validate_marks(self):
		#print("Student MArks")
		if self.student_marks in range(0,100):
			#print(self.student_marks)
			return True
		else:
			return False
			#print("Padhai kar sale")


	def check_qualification(self):
		if self.validate_age() == True and self.validate_marks() == True :
			if self.student_marks >= 65:
				return True
				#print("Bada Tir mar dia tu ....")
		else:
			return False
			#print("Naseeb khrab hai bhai :( ")

rohan = Student("Rohan",25,70)
print(rohan.validate_age())
print(rohan.validate_marks())
print(rohan.check_qualification())
