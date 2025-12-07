employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

employee_departments = {}
for i in range(len(employees)):
    name = employees[i]["name"]
    department = employees[i]["department"]
    employee_departments[name] = department
# Create a dictionary mapping names to departments using a dictionary comprehension
#employee_departments = {employee["name"]: employee["department"] for employee in employees}
print(employee_departments)


#An empty dictionary named employee_departments is created. This dictionary will be 
#used to store the final result.
#for i in range(len(employees)):

#This is a for loop that iterates through the employees list using an index.
#len(employees) gets the total number of items in the list (which is 4).
#range(4) generates a sequence of numbers from 0 to 3 (0, 1, 2, 3).
#The loop will run four times, with the variable i taking on the values 0, 1, 2, 
# and 3 in each iteration.
#Inside the Loop:

#name = employees[i]["name"]: In each iteration, employees[i] accesses one of the 
# employee dictionaries from the list. Then, ["name"] retrieves the value 
# associated with the "name" key from that dictionary.
#department = employees[i]["department"]: Similarly, this line retrieves the value 
# for the "department" key.
#employee_departments[name] = department: This line adds a new key-value pair to 
# the employee_departments dictionary. The employee's name becomes the key, and 
# their department becomes the value.
#print(employee_departments)

#After the loop finishes, this line prints the final dictionary