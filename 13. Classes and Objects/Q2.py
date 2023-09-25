"""
Q. Using class Employee, create a list of employees(data taken from user), and display list of employees in
sorted order according to their names. Also define a function to sort list of employees according to their
salary in descending order.
"""

class Employee:
    def __init__(self) -> None:
        self.name = input("Enter the name: ")
        self.salary = input("Enter the salary: ")
        
    def __repr__(self):
        return str((self.name, self.salary))
    
list = []    
for i in range(4):
    a = Employee()
    list.append(a)
    
print(sorted(list,key = lambda x:x.name))
print(sorted(list, key=lambda y:y.salary, reverse=True))
     
             
             
             
             
             
             
             
                