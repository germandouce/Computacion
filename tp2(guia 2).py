#ejercicio 2.1
'''
Elaborar un programa que solicite al usuario que ingrese un número positivo y luego muestre 
el próximo número par
Ejemplo:
Ingrese un número positivo: 11
Próximo par es: 12

Ingrese un número positivo: 10
Próximo par es: 12
'''
#resolucion 2.1
'''
num = float(input('ingrese un numero positivo: '))

if  (num>0) :
    if ( (int(num))%2 == 0) :
        print ('proximo par es', ( int( num + 2) ))
    else:
        print ('proximo par es', ( int( num + 1) ) )
else:
    print('no es positivo')
exit()
'''
#Ejercicio 2.2
'''
Confeccionar un programa en el que se ingresen 2 números por teclado y que indique si el 
primero de ellos es divisible por el segundo. Considere utilizar la operación módulo o resto.
Ejemplo:
Ingrese un número: 16
Ingrese divisor: 4
16 es divisible por 4
Ingrese un número: 25
Ingrese divisor: 3
25 no es divisible por 3
'''
num = float (input ('ingrese un numero: ') )
div = float ( input ('ingrese divisor: ') )
if ( ( num - int(num) ) ==0) and ( ( div -  int(div) ) ==0 ):
    if (num % div) == 0:
        print (int (num), 'es divisible por', int (div))
        print ('el resultado de la division entera es', int (num/div))
    else:
        print(int (num), 'no es divisible por', int(div))
else :
    print ('uno de los numeros no es entero, no tiene sentido hablar de divisibilidad')
exit()

#OJO NUMEROS PRIMOS IMPORTANTE SI NO APARECE EN GUIA TP (SI APARECE TAMBIEN XD) 
# POSIBLE PARCIAL