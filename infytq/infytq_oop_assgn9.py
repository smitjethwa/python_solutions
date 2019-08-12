class Student :
	def __init__(self, student_name , student_age, student_marks, course_id):
		self.student_name = student_name
		self.student_age = student_age
		self.student_marks = student_marks
		self.course_id = course_id
		self.fees = None

	def validate_age(self):
		if self.student_age >= 20 :
			return True
		else:
			return False
	def validate_marks(self):
		if self.student_marks in range(0,100):
			return True
		else:
			return False
	def check_qualification(self):
		if self.validate_age() == True and self.validate_marks() == True :
			if self.student_marks >= 65:
				return True
		else:
			return False
	def check_course(self):
			if self.course_id == 1001 or self.course_id == 1002 :
				if self.student_marks > 85 :
					if self.course_id == 1001 :
						self.fees = 25575.0 - (25575.0 * 25/100)
						return self.fees
					elif self.course_id == 1002 :
						self.fees = 15500.0 - (15500.0 * 25/100)
						return self.fees
				else:
					if self.course_id == 1001 :
						self.fees = 25575.0
						return self.fees
					elif self.course_id == 1002 :
						self.fees = 15500.0
						return self.fees
			else:
				print("course_id IMproper")
				return False

	def display(self):
		# just print the result out
		print("Student NAme :- {} ; student_age :- {} ; student_marks :- {} ; student_course: {}".format(self.student_name,self.student_age,self.student_marks, self.course_id))
		print(" Course Fees :- {} ".format(self.check_course()))

rohan = Student("Rohan",25,70,1002)
rohan.display()