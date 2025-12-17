
num_grades = int(input("¿Cuántas notas vas a ingresar?: "))

all_grades = []
passed_grades = [] 
failed_grades = []

for i in range(num_grades ):
   grade =float(input(f"Ingrese la nota {i+1}: "))
   all_grades.append(grade)

   if grade >= 70:
       passed_grades.append(grade)
   else:
       failed_grades.append(grade)

num_passed_grades = len(passed_grades)
num_failed_grades = len(failed_grades)

average_all_grades = sum(all_grades) / num_grades

if num_passed_grades > 0:
 average_passed_grades = sum(passed_grades) / num_passed_grades
else:
 average_passed_grades = 0
if num_failed_grades > 0:
 average_failed_grades = sum(failed_grades) / num_failed_grades
else:
 average_failed_grades = 0

print("Cantidad de notas: ", num_grades)
print("Cantidad de notas aprobadas: ", num_passed_grades)
print("Cantidad de notas desaprobadas: ", num_failed_grades)
print("Promedio de todas las notas: ", average_all_grades)
print("Promedio de notas aprobadas: ", average_passed_grades)
print("Promedio de notas desaprobadas: ", average_failed_grades)
