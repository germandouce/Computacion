'''Hacer un programa que ingrese 5 números y obtenga su promedio; detarmine cuál es el mayor
de los ingresados y cuáles de ellos están por debajo del promedio.
Ej:
Ingrese 5 números
43
-12
11
5
66
El promedio es 22.6
El mayor es 66.0
Por debajo de 22.6 están:
-12.0
11.0
5.0'''

#sin ciclo

num1 = float(input('ingrese numero 1: '))
mayor=num1
num2 = float(input('ingrese numero 2: '))
if num2 > mayor:
    mayor=num2
num3 = float(input('ingrese numero 3: '))
if num3 > mayor:
    mayor=num3
num4 = float(input('ingrese numero 4: '))
if num4 > mayor:
    mayor=num4
num5 = float(input('ingrese numero 5: '))
if num5 > mayor:
    mayor=num5

promedio=(num1+num2+num3+num4+num5)/5

print('el promedio es %.1f'%promedio)
print('el mayor es', mayor)
print('por debajo de', promedio,'estan:' )
if num1 < promedio:
    print(num1)
if num2 < promedio:
    print(num2)
if num3 < promedio:
    print(num3)
if num4 < promedio:
    print(num4)
if num5 < promedio:
    print(num5)

#con ciclo. no dice si cuales con menores q el promedio

'''
i=0
num=float(input('ingrese un numero: '))
mayor=num
sumnum=num
while i <4:
    num=float(input('ingrese un numero: '))
    if num>mayor:
        mayor=num
    sumnum+=num
    i+=1
promedio=(sumnum)/5

print('el promedio es %.1f'%promedio)
print('el  mayor es', mayor)
'''


