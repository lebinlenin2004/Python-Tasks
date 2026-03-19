class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print("Name is ",self.name)
        print("Salary is",self.salary)
        
class Manager(Employee):
    pass
    def bonus(self):
     return self.salary * 1.2

class Developer(Employee):
    pass
    def bonus(self):
     return self.salary * 1.1
        
m1 = Manager("Lebin",160000)
print(m1.bonus())


d1 = Developer("Rahul", 10000)
print(d1.bonus())



        
        