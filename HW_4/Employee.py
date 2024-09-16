
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def update_salary(self,increase):
        self.salary *= (1+ increase /100)
        return (self.salary)
    

John=Employee("John",5000)

new_salary = John.update_salary(10)

print("John's Updated salary is:", new_salary)

##
# Q: How to I print the updated salary? here is background information and my code. Create a class called Employee with attributes name and salary. 
# Implement a method within the class that increases the salary of the employee by a given percentage. 
# Instantiate an object of the Employee class with name = "John" and salary = 5000, increase the salary by 10%, 
# and print the updated salary. (then gave code)

#Q:what does this error mean:File "<stdin>", line 1
#& C:/Users/carte/AppData/Local/Programs/Python/Python312/python.exe c:/Users/carte/OneDrive/Documents/GitHub/data5500_hw/HW_4/Employee.py
#^
#SyntaxError: invalid syntax
#>>>