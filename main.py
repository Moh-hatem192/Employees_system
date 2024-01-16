import csv
class Employee:
    def __init__(self, name, age, id, job, phone, bank_account, hours_worked=160, hourly_rate=10):
        self.name = name
        self.age = age
        self.__id = id
        self.job = job
        self.phone = phone
        self.__bank_account = bank_account
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        AllEmployees.add_employee(self)

    def __str__(self):
        return f'{self.name} works as {self.job} and has {self.age} years '
    
    def __repr__(self):
        return f'(Employee) = {self.name}, works as {self.job}'
    
    @property
    def id(self):
        return self.__id

    @property
    def bank_account(self):
        return self.__bank_account
    

    def calculate_gross_salary(self):
        return self.hourly_rate * self.hours_worked

    def calculate_net_salry(self):
        gross_salary = self.calculate_gross_salary()
        net_salary = Finance.calculate_net_salry(gross_salary)
        return net_salary
    
class Finance:
    SALARY_THRESHOLD = 5000
    LOW_TAX = 0.1
    HIGH_RATE = 0.3
    RETIRMENT_COST = 0.2
    INSURANCE = 100

    @staticmethod
    def calculate_tax(salary):
        if salary > 5000:
            tax = salary * Finance.HIGH_RATE
        else:
            tax = salary * Finance.LOW_TAX
        return tax

    @staticmethod
    def calculate_net_salry(gross_salary):
        tax = Finance.calculate_tax(gross_salary)
        retirment_deduction = gross_salary * Finance.RETIRMENT_COST
        total_deductions = tax + retirment_deduction + Finance.INSURANCE
        net_salary = gross_salary - total_deductions
        return net_salary

class AllEmployees:
    __employees = []

    @classmethod
    def add_employee(cls,employee):
        AllEmployees.__employees.append(employee)

    @classmethod 
    def list_employees(cls):
        return AllEmployees.__employees

    @classmethod
    def get_employee_by_id(cls, employee_id):
        for emp in AllEmployees.__employees:
            if emp.id == employee_id:
                return emp
        return None

    @classmethod
    def fire_employee_by_id(cls, emp_id):
        employees = AllEmployees.__employees
        AllEmployees.__employees = [emp for emp in employees if emp.id != emp_id ]

class Manager(Employee):
    BONUS = 400
    def __init__(self, *args, authority_level = 3, **kwargs):
        super().__init__(*args, **kwargs)
        self.authority_level = authority_level

    def demote_employee(self, emp_id, deduction_amount):
        if self.authority_level >=3:
            employee = AllEmployees.get_employee_by_id(emp_id)
            if employee:
                new_rate = employee.hourly_rate - deduction_amount
                employee.hourly_rate = max(new_rate, 4)
                return f'{employee.name} new hourly rate is {employee.hourly_rate}'
            return f'employee with the following id not found'
        return 'You have no acess to demote employees'
    
    
    def calculate_net_salry(self):
        basic_salary = super().calculate_net_salry()
        return basic_salary  + Manager.BONUS

ali = Employee('ali', 12, '4567', 'Software enginer', '+962791048099', '4568')
mohammed = Manager('mohammed', 12, '1234', 'Software enginer', '+962791048099', '4568')
print(mohammed.demote_employee('4567', 23))
print(ali.hourly_rate)
print(mohammed.hourly_rate)