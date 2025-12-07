n = int(input("¿Cuántas notas vas a ingresar?: "))

todas_las_notas = []
aprobadas = []
desaprobadas = []

for i in range(n):
   nota =float(input(f"Ingrese la nota {i+1}: "))
   todas_las_notas.append(nota)

   if nota >= 70:
       aprobadas.append(nota)
   else:
       desaprobadas.append(nota)

cantidad_aprobadas = len(aprobadas)
cantidad_desaprobadas = len(desaprobadas)

promedio_todas_las_notas = sum(todas_las_notas) / n
promedio_aprobadas = sum(aprobadas) / cantidad_aprobadas
promedio_desaprobadas = sum(desaprobadas) / cantidad_desaprobadas

print("Cantidad de notas: ", n)
print("Cantidad de notas aprobadas: ", cantidad_aprobadas)
print("Cantidad de notas desaprobadas: ", cantidad_desaprobadas)
print("Promedio de todas las notas: ", promedio_todas_las_notas)
print("Promedio de notas aprobadas: ", promedio_aprobadas)
print("Promedio de notas desaprobadas: ", promedio_desaprobadas)




