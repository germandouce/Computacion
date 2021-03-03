'''Realizar un programa en PYTHON que permita generar aleatoriamente 20 números pares entre
0 y 100 y determinar cuántos vinieron repetidos (se considera repetición desde la 
segunda aparición del número en adelante), cuántos fueron por debajo del número 50; 
cuántos mayores o iguales a 50 (estos últimos incluyendo repeticiones) . Mostrar 
todos los números ingresados sin repeticiones.
Ej:
Números generados internamente: (32,0,34,2,92,68,38,4,74,58,76,8,78,92,46,20,24,92,58,28)
Salida:
Cantidad repetidos: 3
Números generados debajo de 50: 11
Arriba o igual a 50: 9'''
#ojo, numtot tiene solo los pares NO RPETEIDOS. casi nunca tiene 20...
#opcion 1
'''
import random      #comentado altenativa
numtot=set()
repe=0
sup50=0
inf50=0     #omitir
for i in range(20):
    num=random.randint(0,100)
    num=num//2*2
    if num in numtot:
            repe+=1
    if num>=50:
            sup50+=1
    else:               #omitir
            inf50+=1    #omitir
    numtot.add(num)
print('cantidad de repetidos: ',repe)
print('arriba de 50:', sup50)
print('debajo de 50:', inf50)  #20-sup50
print('mumeros generados:')
for numeros in numtot:
    print(numeros)'''
#opcion 2

from random import choice
numeros=set()
sub=0
for i in range(20):
    n=choice(range(0,101,2))
    if n<50:
        sub+=1
    numeros.add(n)
print('Cantidad repetidos',20 - len(numeros)) #TOTAL GENERADOS (20) MENOS los que estan en
print('Números generados')  #numeros, que al ser un conjunto, son los NO REPETIDOS.
for n in numeros:                   #= REPETIDOS
    print(n)
print('debajo de 50',sub)
print('Arriba o igual a 50',20-sub)
exit()

