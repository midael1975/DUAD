class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def salary(self):
        return self._salary
    
    @property
    def name(self):
        return self._name

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
        
    @name.setter
    def name(self, value):
        self._name = value
    

    def promote(self, increase):
        if increase < 0:
            raise ValueError("Increase cannot be negative")
        self.salary = self.salary * (1 + increase)

# Example usage:
try:
    emp = Employee("Ana", 1000)
    print(emp.name)  # Output: Ana
    print(emp.salary)  # Output: 1000

    emp.promote(0.1)  # Promote with a 10% increase
    print(emp.salary)  # Output: 1100

    emp.salary = -1000  # This will raise an error
except ValueError as e:
    print(e)  # Output: Salary cannot be negative
