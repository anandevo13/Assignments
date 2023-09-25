"""
Q. Define a class employee with instance variables empid, name, salary. Define constructor to initialize 
member variables. Define function to show employee data.
"""

class Employee:
    #Common base class for all employees
    empCount = 0
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d"%Employee.empCount)
            
    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)

# This would create first object of employee class
emp1 = Employee("zara",2000)
# This would create second object of employee class
emp2 =  Employee("manni",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d"%Employee.empCount)
        
        