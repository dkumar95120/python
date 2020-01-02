class Employee:
    def __init__ (self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary

    def print (self):
        print ('Name: ' + self.name)
        print ('address: ' + self.address)
        print ('salary: ' + self.salary)

    def get_name (self):
        return self.name

    def get_address (self):
        return self.address

    def get_salary (self):
        return self.salary


class Company:
    def __init__ (self,name):
        self.name = name
        self.employees = []

    def employees (self):
        return self.employees;

    def read (self, file):
        with open(file) as fp:
            line = fp.readline()
            while line:
                emp_data = line.split(',')
                self.employees.append(Employee(emp_data[0], emp_data[1], emp_data[2]))
                line = fp.readline()

    def total_employees (self):
        print('Total Employees: ' , len(self.employees))


    def print (self):
        for emp in self.employees:
            emp.print()

