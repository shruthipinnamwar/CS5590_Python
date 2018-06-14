

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 16:26:01 2018

@author: shrut
"""


class Employee(object):
    EmplNumber = 2
    def __init__(self,nam,famil,departmen,salar):
        self.name = nam
        self.family = famil
        self.department = departmen
        self.salary = salar# public variable
   
   
        
    #def NumberOfEmployees(self):
        #return str(self) )
    def GetName(self):
        print("Employee Name: "+ self.name)
        return 
    def Family(self):
       
         print("Employee Family: "+ str(self))
         return 
    def Salary(self):
        print("Employee Salary: "+ str(self))
        return
    def SalaryValue(self):
        return self.salary
    def Department(self):
        print("Department:" + str(self))
        return 
    def NumberOfEmployees(self):
        print("The Number Of Employeesis :" + str(self.EmplNumber))
        return
    
    #def AverageSal(self, value):
    
class FullTimeEmployee(Employee):
    def __init__(self,name,family,department,salary,hour):
        self.hours = hour
    def GetHours(self):
        print("The employee works " + self.hours + " hours")

def avg_salary():  # average salary
    x = 0  
    total = 0  
    while x < len(empArray):  # While the counter is in the # of employees
        total += empArray[x].SalaryValue()  # Add salary to total
        x += 1  # Iterate
    total = total / x  # Divide total salaries by # of employees
    print("The average salary is $" + str(total))
    
       
        
        

     
 # Make some employees and call functions
Emp1 = Employee("ABC", "fam", 400, "CS")
Emp2 = FullTimeEmployee("DEF", "Fam2", 600, "Electrical", "20")

empArray = [Emp1, Emp2]

print("For employee 1: ")
Emp1.GetName()
Emp1.Family()
Emp1.Salary()
Emp1.Department()
print("\n")

print("For employee 2: ")
Emp2.GetName()
Emp2.Family()
Emp2.Salary()
Emp2.Department()
Emp2.GetHours()
print("\n")

Emp1.NumberOfEmployees()

#avg_salary()           
        
        



