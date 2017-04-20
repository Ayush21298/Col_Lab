class Employee:
	count=0
	def __init__(self,name,sal):
		self.name=name
		self.sal=sal
		Employee.count+=1
		self.id=Employee.count
	
	def details(self):
		print 'Employee ID : ',self.id, ' Name : ',self.name,' Salary : ',self.sal
	
	def setSal(self,s):
		self.sal = s
	@classmethod
	def add(emp,a,b):
		return emp(a,b)

emp1=Employee('ABC',2000)
Employee.details(emp1)
Employee.setSal(emp1,4000)
Employee.details(emp1)
emp2 = Employee.add('XYZ',1000)
Employee.details(emp2)


