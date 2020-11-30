'''Ingresar números reales. El final vendrá dado por 0. Determinar si ingresó alguno estrictamente entero, cuántos negativos hubo, la cantidad total de números ingresados y el promedio de los positivos.
Ej:
Ingrese números reales
12
-3.55
5.66
11
-99
1.25
-27.8
0
Hubo por lo menos un número entero
Vinieron 3 negativos en un total de 7 números
El promedio de los números positivos es: 7,48'''

enteros=0
negativos=0
positivos=0
totnum=0
sumapositivos=0
num=float(input('ingrese numeros reales: '))         
while num!=0:
    if num%1==0:
        enteros+=1
    if num<0:
        negativos+=1
        totnum+=1                       #el numero es negativo
    if num>0:
        positivos+=1
        totnum+=1                       # o es positivo
        sumapositivos+=num
    num=float(input('ingrese números reales: '))

if enteros>0:
    print('hubo por lo menos un número entero')
else:
    print('no hubo ningún número entero')

print('vinieron', negativos,'negativos en un total de', totnum,'números')

if sumapositivos>0:
    promedio=(sumapositivos/positivos)
    print('El promedio de los números positivos es: %.2f'%promedio)
else:
    print('no se ingresaron numeros positivos para calcular el promedio')

