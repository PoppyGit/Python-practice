#functions
# def area_of_triangle():
#     height = 12
#     base = 6
#     area = 0.5*height*base
#     print(area)
# area_of_triangle()
#method
# class Person:
#     #constructor 
#     def __init__(self,name,Nationality):
#         self.name = name
#         self.Nationality = Nationality
#     #the method details
#     def details(self):
#         print("Hello my name is",self.name,"and am from",self.Nationality)
# #create an object
# description = Person("Natalie","SA")
# #call the methods
# description.details()


# Write a Python class Employee with attributes like emp_id, emp_name, 
# emp_salary, and emp_department and methods like calculate_emp_salary,
# emp_assign_department, and print_employee_details. 
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
# which is the number of hours worked by the employee. If the number of hours worked is 
# more than 50, the method computes overtime and adds it to the salary. 
# Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

class employee:
    #constructor
    def __init__(self,name,emp_id,salary,department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department
    #the method calculate emp salary
    def calculate_employee_salary(self, salary,hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime*(salary/50)
            self.salary = self.salary + overtime_amount   
        else:
            print("You havent worked overtime!")
    #assigned department method
    def assigned_department_method(self,emp_department):
        self.department = emp_department
    #employee details
    def employee_details(self):
        print("Employee name",self.name)
        print("Employee id",self.emp_id)
        print("Salary",self.salary)
        print("department",self.department)
#create an object
emp1 = employee("Loveness","ID55478",75000,"Human resources")
#call employee details
emp1.employee_details()
