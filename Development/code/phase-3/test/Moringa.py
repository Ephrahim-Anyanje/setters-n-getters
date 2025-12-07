class Employee:
    def __init__(self, first_name, last_name, salary, gender, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.gender = gender
        self.phone_number = phone_number
    pass

def fullname(self):
        return f"{self.first_name} {self.last_name}"

def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

@property
def id(self):
     initials = f"{self.first_name[0]}{self.last_name[0]}".upper()
     phone_str = str(self.phone_number)
     last_three = phone_str[-3:]

     return f"{initials}{last_three}"  
  
class Manager:
      def __init__(self, first_name, last_name, salary, gender, phone_number , department,employees=None):
          super().__init__(first_name, last_name, salary, gender, phone_number)
          self._department = department

          if employees is None:
              self.employees = []
          else:
              self.employees = employees
def add_employee(self, employee):
          self.employees.append(employee)
    
def remove_employee(self, employee):
          self.employees.remove(employee)    
    

class Instructor:
    pass