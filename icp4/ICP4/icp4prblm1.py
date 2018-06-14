class Employee:  # Employee class
    empNum = 3
        
    def increment(self):
        self.__class__.empNum += 1
    def __init__(self, n, f, s, d): #constructor
        self.name = n
        self.family = f
        self.salary = s
        self.dept = d
    def get_name(self):
        print("Employee Name:" + self.name)
        return
    def get_family(self):
        print("Family:" + self.family)
        return
    def get_salary(self):
        print("Employee's salary : " + str(self.salary))
        return
    def get_salary_value(self):  
        return self.salary
    def get_dept(self):
        print("Employee's department : " + self.dept)
        return
    def get_emp_num(self):
        print("Number of employees :" + str(self.empNum))
        return
class FullTimeEmployee(Employee): #inherited from class EMployee   
    def __init__(self, n, f, s, d, h):
        Employee.__init__(self, n, f, s, d)
        self.hours = h
    def get_hours(self):  # not inherited
        print("Employee works for " + self.hours + " hours")


def AverageSalary():  
    x = 0  
    total = 0  
    while x < len(eArray):  
        total += eArray[x].get_salary_value()  # SAlary + Total
        x += 1 
    total = total / x  # total / no. of Employees
    print("Avg salary" + str(total))
#Creating Employees
Emp1 = Employee("Shruthi", "DES", 400, "CS")
Emp2 = FullTimeEmployee("ANil", "BASE", 700, "Sales", "MAintenance")
Emp3 = Employee("Kittu", "XYZ", 600, "General")
eArray = [Emp1, Emp2, Emp3]

print("Employee 1: ")
Emp1.get_name()
Emp1.get_family()
Emp1.get_salary()
Emp1.get_dept()
print("\n")
print("Employee 3: ")
Emp1.get_name()
Emp1.get_family()
Emp1.get_salary()
Emp1.get_dept()
print("\n")

print("Employee 2: ")
Emp2.get_name()
Emp2.get_family()
Emp2.get_salary()
Emp2.get_dept()
Emp2.get_hours()
print("\n")
Emp1.get_emp_num()
AverageSalary()


