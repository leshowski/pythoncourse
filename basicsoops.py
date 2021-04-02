class Employee():
    
    raisepercentage = 1.02
    number_of_employees = 0
    
    def __init__(self, first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first +last +"@lpc.com"

        Employee.number_of_employees +=1
    
    def fullname(self):
        return self.first + " " +self.last

    def salaryRaise(self):
        self.salary = int(self.salary * self.raisepercentage)

class Developer(Employee):
    def __init__(self, first,last,salary,prog_lang):
        #super().__init__(first,last,salary)
        Employee.__init__(self,first,last,salary)
        self.prog_lang = prog_lang

emp1 = Developer('luis','ponce',15000,"Python")
emp2 = Developer('Juan','Perez',5000,"Java")

#print(emp1.fullname())
#print(emp2.fullname())

print(emp1.prog_lang)
print(emp2.prog_lang)

#emp1.salaryRaise()
#print(emp1.salary)
#emp1.salaryRaise()
#print(emp1.salary)
#print(Employee.number_of_employees)

#print(help(Developer))