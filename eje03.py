"""
Escribir un Programa, que permita, calcular el promedio de un curso en el cual se toman 7 prácticas
y el programa halle el promedio

"""

TOTAL_NOTAS = 7

contador = 1
total = 0

while contador <= 7:
    nota = float(input('ingrese la nota ' + str(contador) + ': '))
    total += nota
    contador += 1

promedio = total / TOTAL_NOTAS

print(promedio)
# print("El promedio es: {:5.2f}".format(promedio))
