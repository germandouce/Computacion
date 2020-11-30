#TP 3: C I C L O S

#PRIMERA PARTE:
            
                                #CILOS INTRO

#rangos
'''
rango::range([<valor_inicio>,]<valor_fin>[,<paso>])
Ej:range(1,10)1,2,3,4,5,6,7,8,9
range(6)0,1,2,3,4,5
range(0,8,2)0,2,4,6
range(15,10,-5)15
El paso DEBEser un entero valor_inicioestá incluído en el rango; valor_fin NO 
valor_inicioes opcional;si no se coloca se asume 0
pasoes opcional; si no se coloca se asume 1
Si se desea rango decreciente se debe colocar un pasonegativo
Si se coloca paso DEBE COLOCARSE valor_inicio, aunque este último sea 0
'''
#banderas
'''
ban=0
print('Ingrese 20 números enteros positivos')
cant=1
while cant<=20:
    num=int(input())
    if num%10==0:
        ban=1
    cant+=1
if ban==1:print('En la lista ingresada hubo al menos un múltiplo de 10')
else: print('En la lista ingresada no hubo múltiplos de 10')
exit()
'''
#ejercicio 3.1

'''Ejercicio 3.1
Elaborar un programa que solicite al usuario que ingrese un número entero y 
determine si el mismo es un número primo.'''
#res 3.1
'''
num=int(input('ingrese un numero entero: '))
while num <=1:
    print('ingrese un numero mayor que 1')
while num in range (2,3):
    print(num, 'es primo')
else:
    ban=0
    divisor=2
    while divisor<=num//2:
        if num%divisor==0:
            ban=1
        divisor+=1
    if ban !=0:
            print('no es primo')
    else: 
        print ('es primo')
exit()
'''
#Ejercicio 3.2
'''Encontrar y mostrar todos los números de 4 cifras que cumplan la condición de que 
la suma de las cifras de orden impar es igual a la suma de las de orden par.'''
#res 3.2
'''
for num in range(1000,10000):
    d1=num//1000
    d2=(num%1000)//100
    d3=(num%100)//10
    d4=num%10
    if (d1+d3)==(d2+d4):
        print(num)
exit()
'''
#Ejercicio 3.3.0
'''Confeccionar un programa en el que se ingresa undígito a buscar y luego  10 números
de 5  cifras.  El  programa  debe informar  cuántas apariciones del dígito hay en 
total.
Ejemplo:
Ingrese el dígito a contar: 1
Ingrese número 1: 23451 Ingrese número 2: 11101 Ingrese número 3: 96587
Ingrese número 4: 10000 Ingrese número 5: 22122 Ingrese número 6: 11111
Ingrese número 7: 88888 Ingrese número 8: 15151 Ingrese número 9: 51515 
Ingrese número 10: 33215    El dígito 1 aparece 18veces'''
'''
dig=int(input('ingrese un digito a contar: '))
i=0
ban=0
while i<10:
    num=int(input('ingrese un numero de 5 cifras: '))
    i+=1
    d1=num//10000
    d2=(num%10000)//1000
    d3=(num%1000)//100
    d4=(num%100)//10
    d5=num%10
    if dig==d1:
        ban+=1
    if dig==d2:
        ban+=1
    if dig==d3:
       ban+=1
    if dig==d4:
        ban+=1
    if dig==d5:
        ban+=1
print('el digito',dig, 'aparece', ban, 'veces')
'''

#res 3.1.1
'''
digito=int(input('Ingrese el dígito a contar: '))
while (digito<0) or (digito>9):
    digito=int(input('Ingrese el dígito a contar: '))
cant=0
print('Ingresar 10 números de 5 cifras')
for i in range(1,11):
    num=int(input('Ingrese el número %d: '%i))
    while (num < 10000) or (num > 99999):
      num=int(input('Ingrese el número %d: '%i))        
    divisor=10000
    while num>0:            #modo de comparar cada digito
        dig=num//divisor    #el dig toma el valor del 1er digito(d1)
        if dig==digito:     #si el d1 es igual al numero q quiero buscar
            cant+=1         #sumo 1 a cant sino,
        num%=divisor        #sigo con siguiente digito, que ahora es el resto del     
        divisor/=10                        # numero divido el divisor (1000 la primera vez). Ya la prox vuelta vae 100 
print()                                     #dsos 10 y asi sucesivamente. ah NO ENTIENDO BIEN ESTO
print('El dígito',digito,'aparece',cant,'veces')
exit()
'''
#ejercicio 3.4
'''Construir un programa en el que se ingresen 5 números pares y determinar para cada uno de ellos si también
es múltiplo  de cuatro. Nota: no se debe considerar un ingreso válido un número impar.'''
'''
for i in range(5):
    num = int(input('ingrese el %dº numero par: '%(i+1)))
    while num%2!=0:
        num =int(input('ingrese el %dº numero par: '%(i+1)))
    if num%4==0:
        print(num,'SI es multiplo de 4')
    else:
        print(num,'NO es multiplo de 4')
'''
#ejercicio 3.5
'''Escribir un programa que encuentre los primeros 4 números perfectos.Un número perfecto es un 
entero positivo, que es igual a la suma de todos los enteros positivos (excluido él mismo) que 
son  divisores  del  número.  Por  ejemplo,  el  primer  número  perfecto es 6, ya que los divisores 
de 6 son 1, 2, 3 y 1 + 2 + 3 = 6.'''
'''
print('los 4 primeros numeros perfectos son')
print(6)
cant=1
num=7                                  #cant= cantidad de numeros perfectos
while cant <4:
    sumadiv=1                           #suma de divisores
    for div in range (2, (num//2)+1):
        if num%div==0:
            sumadiv+=div            
    if sumadiv==num:       
        print(num)      #como me piden 4 primeros numeros perfectos
        cant+=1        #recien sumo 1 a cant cuando llegue a un numero perfecto
    num+=1
exit()
'''
'''
contador = 0
i = 1
n=7
while contador <4:
    for i in range(2, (n//2)+1):        
       if(n%i == 0):
        contador += i
       
        if (n%2 == 0):
            i+=1 
        else:
            i += 2
    if(contador==n):
        print(n)        
    n+=1
'''
#ejercicio 3.6
'''Escribir un programa que reciba una cantidad indefinida de números enteros positivos hasta que se
ingresa el 0. A continuación el programa debe indicar cuál fue el mayor y cuál el menor. 
3:25am ''' 
'''
num=int(input('ingrese un numero entero positivo: '))
while num<0:
    num=int(input('ingrese un numero entero positivo:0 '))
if num!=0:
    mayor=num
    menor=num
    num=int(input('ingrese un numero entero positivo: '))
    while num<0:
        num=int(input('ingrese un numero entero positivo: '))
    while num!=0:                           
        if num>mayor: 
            mayor=num                                        
        if num<menor:
            menor=num
        num=int(input('ingrese un numero entero positivo: '))
        while num<0:
            num=int(input('ingrese un numero entero positivo:'))
    print('el mayor numero ingresado fue:', mayor)
    print('el menor numero ingresado fue', menor)
        
else:
    print('no hay numeros')
'''

#3.7
'''Para encontrar el máximo común divisor (mcd) de dos números se emplea el algoritmo de Euclides, 
que se puede describir así: Dados dos enteros a y b (siendo a > b), se divide a por b. Si el resto 
de la división es cero, el número b es el máximo común divisor. Si la división no es exacta, se 
divide el número menor b por el resto de  la  división  anterior.  Se  siguen  los  pasos  
anteriores  hasta obtener  un  resto  cero.  El  último  divisor  (b)  es  el  mcd  buscado. 
Escribir un programa que calcule el mcd de dos números enteros.'''
#res 3.7
'''
a=int(input('ingrese un numero: '))
b=int(input('ingrese otro numero: '))
if a>b:
    dividendo=a        #hago a//b
    divisor=b               
else:
    dividendo=b        #hago b//a         
    divisor=a

if (dividendo % divisor) ==0:  
    print(divisor, 'es max comun divisor')
else:        
    mcd=dividendo%divisor       # a//b    a|_b__   rest
    dividendo=divisor           # a=b     b|___   
    divisor=mcd                 # b|_rest__   
    while mcd!=0:             # mientras resto !=0
        mcd=dividendo%divisor 
        dividendo=divisor          
        divisor=mcd 
    print('el max comun divisor entre', a,'y', b, 'es:',dividendo)
exit()
'''
#Ejercicio 3.8

'''Escribir un programa que permita ingresar las notas de una cantidad indefinida de alumnos.A continuación 
el programa deberá mostrar la cantidad de alumnos aplazados (nota menor a 4), la cantidad de 
alumnos aprobados (nota entre 4 y 7 inclusive) y la cantidad de alumnos que promocionan la materia
(nota superior a 7). En cada caso, se mostrará el porcentaje del total de notas cargadas que 
cada caso representa. Las notas son valores enteros y la carga finaliza cuando la nota ingresada 
es 0. Ignorar las notas no válidas (fuera del rango de 1 a 10).
Ejemplo:Ingrese nota: 5
Ingrese nota: 4
Ingrese nota: 2
Ingrese nota: 8...
Ingrese nota: 0
Cantidad de aplazos: 5 (10%)
Cantidad de aprobados: 15 (30%)
Cantidad de promocionados: 30 (60%)'''

'''
apla=0
apro=0
prom=0
nota=int(input('íngrese nota (1-10): '))
while not (nota in range (11)):
    nota=int(input('íngrese nota (1-10): '))
while nota!=0:
    if 0<nota<4 and nota!=0:
        apla+=1
    if 4<nota<7 and nota!=0:
        apro+=1
    if 7<nota<10 and nota!=0:
        prom+=1
    nota=int(input('íngrese nota (corta con cero): '))
while not (nota in range (11)):
    nota=int(input('íngrese nota (1-10): '))

alumnostot=apla+apro+prom
if alumnostot==0:
    print('NO HAY NOTAS INGRESADAS')
else:
    por=(apla/alumnostot)*100
    print('cantidad de aplazos:', apla,'(%.2f'%por,'%')
    por=(apro/alumnostot)*100
    print('cantidad de aprobados:', apro,'(%.2f'%por,'%')
    por=(prom/alumnostot)*100
    print('cantidad de aplazos:', prom,'(%.2f'%por,'%')
'''
#Ejercicio 3.9
'''La operación factorial de un número entero positivo “n” (expresado como n!) es el producto 
que resulta de multiplicar “n” por todos los enteros inferiores a él hasta el uno. Por 
ejemplo:5! = 5 * 4 *3 * 2 * 110! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
Como salvedad se define 0! = 1. Elaborar un programa que calcule el factorial de un número 
entero. El programa principal debe solicitar el ingreso de un número entero, verificar si 
se trata de un número mayor o igual a 0 y calcular su factorial. En caso de que el usuario
ingresara  un número negativo, imprimir una advertencia. 
Ejemplos: Ingrese un número entero: 5 
El factorial de 5 es: 120 
Ingrese un número entero: -10
No se puede calcular el factorial de un número negativo'''
'''
num=int(input('ingrese un numero entero positivo o cero: '))
while num<0:
    print('No se puede calcular el factorial de un número negativo')
    num=int(input('ingrese un numero entero positivo o cero: '))
if num==0:
    print('el factorial de 0 es 1')
else:
    fact=1
    for n in range (1,num+1):
        fact*=n
    print('El factorial de', num,'es',fact,)        
'''

#SEGUNDA PARTE                    
                                    
                            #DIBUJOS CON CICLOS

#Linea vertical
'''
n=int(input('Ingrese largo (debe ser menor que 21):'))
while n>20:
    n=int(input('Ingrese largo (debe ser menor que 21):'))
for i in range(n):print('*')
exit()
'''
#linea horizontal
'''
n=int(input('Ingrese ancho (menor o igual que 70):'))
while n>70:
    n=int(input('Ingrese ancho (menor o igual que 70):'))
for i in range(n):print('*',end='')
exit()
'''
'''
n=int(input('ingrese el ancho entre 2-20'))
while n<2 or n>20:
    n=int(input('ingrese el ancho entre 2-20'))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
'''
#lineas horizontales
'''
n=int(input('Ingrese ancho ( 2-20 ) :'))
while (n<2)or(n>20):
n=int(input('Ingrese ancho ( 2-20 ) :'))
for i in range(n):
    for j in range(n):
        print('*',end='  ')
    print()
exit()
'''
'''
n=int(input('ingrese ancho'))
for i in range(n):
    print('*',end=' ')
print()
for i in range(n-2):
    print('*',end=' ')
    for j in range(n-2):
        print(' ',end=' ')
    print('*')
for i in range(n):
    print('*',end=' ')
'''

#calculo del cubo de un numero sin usar multiplicaciones
'''
n=int(input('ingrese un num: '))
c=0
for i in range (n):
   for j in range (n):
       for k in range (n):
        c+=1
print(c)
'''
#ej 3.10
'''Ejercicio 3.10
Efectuar un programa que solicite al usuario que ingrese la base de un triángulo rectángulo.
Luego  dibujar en la pantalla dicho triángulo como se muestra en el ejemplo.
Ejemplo:
Ingrese base: 5

*
* *
* * *
* * * *
* * * * *   
'''
'''
n=int(input('Ingrese altura entre 2 y 20: '))
while n<=2 or n>20:
    n=int(input('Ingrese altura entre 2 y 20: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:print('* ',end=' ')
        else:print('  ',end=' ')
    print()
exit()
'''
#ej 3.11
'''
Efectuar un programa que solicite al usuario que ingrese un número entero impar (validar el
valor ingresado). El programa tendrá que dibujar en la pantalla un triángulo de asteriscos 
cuya base sea el valor ingresado.
Ejemplo:
Ingrese número: 8
Número no válido. Ingrese número: 11
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
'''
'''
n=int(input('ingrese altura impar entre 3 y 19: '))
while n%2==0 or n<=2 or n>=20:
    n=int(input('no válido. Ingrese un altura impar entre 3 y 19: '))
for i in range(n//2+1,n+1):
    for j in range(1,n+1):
        if (j>=n+1-i)and(i>=j):print('* ',end=' ')
        else:print('  ',end=' ')
    print()
exit()
'''
#ej 3.12
'''Efectuar un programa que solicite al usuario que ingrese la base de un triángulo rectángulo.
Luego dibujar en la pantalla dicho triángulo como se muestra en el ejemplo.
Ejemplo:
Ingrese base: 5
        *
      * *
    * * *
  * * * *
* * * * *
'''
'''
n=int(input('Ingrese altura entre 2 y 20: '))
while n<=2 or n>20:
    n=int(input('Ingrese altura entre 2 y 20: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=n+1-i:print('* ',end=' ')
    else:print('  ',end=' ')
    print()
exit()

'''
#ej 3.13
'''
Efectuar un programa que solicite al usuario ingresar la diagonal de un rombo (validar que
el valor ingresado sea impar). Luego deberá dibujar dicho rombo en la pantalla.
Ejemplo:
Ingrese diagonal: 8
Valor incorrecto: 7 (ejemplo hecho xa diagonal de)
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *  
      * * * 
'''
'''
d=int(input('ingrese diagonal del rombo (impar): '))
while d%2==0:
    d=int(input('valor incorrecto. ingrese diagonal impar: '))    
for i in range (1,d+1):
    for j in range(1,d-i+1):
        print(' ',end=' ')
    for j in range(1,i*2):
        print('*',end=' ')
    print()
   
for i in range(2,d+1):
    for j in range(1,i):
        print(' ',end=' ')
    for j in range(1,(d+1-i)*2):
        print('*',end=' ')
    print()
print()
exit()
'''
#ej 3.14
'''Efectuar un programa que solicite al usuario que ingrese la base y la altura de un rectángulo.
Luego deberá dibujar en la pantalla el rectángulo hueco con marco doble.
Ejemplo: 
Ingrese base: 7
Ingrese altura: 6
* * * * * * * 
* * * * * * * 
* *       * *
* *       * *
* * * * * * * 
* * * * * * * 
'''
'''
n=int(input('Ingrese base entre 5 y 20: '))
while n <= 4 or n>20:
    n=int(input('Ingrese base entre 5 y 20: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if  (i in (1,2,n-1,n)) or (j in(1,2,n-1,n)):
            print('*',end=' ')
        else:
            print('  ',end='')
    print()
print()
exit()
'''
#Ejercicio 3.15
'''Efectuar un programa que solicite al usuario que ingrese la base de un cuadrado. Luego deberá 
dibujar en la pantalla  el cuadrado vacío dividido en cuartos. 
Ejemplo:
Ingrese base: 5

* * * * * 
*   *   *
* * * * * 
*   *   *
* * * * *
'''
'''
n=int(input('Ingrese base entre 5 y 20: '))
while n <= 4 or n>20:
    n=int(input('Ingrese base entre 5 y 20: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if  (i in (1,n//2+1,n)) or (j in (1,n//2+1,n)):
            print('*',end=' ')
        else:
            print('  ',end='')
    print()
#print() para que esta este print??
exit()
'''
#Ej 3 16
'''
Ejercicio 3.16
Efectuar un programa que solicite al usuario que ingrese la base impar de un triángulo.Luego
deberá dibujar en la pantalla dicho triángulo de la siguiente forma:
Ejemplo:
Ingrese base: 9
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
 *             *
   *         *
     *     *
        *   
'''
'''
n=int(input('Ingrese altura impar: '))
while n <= 0 or n>20 or n%2==0:
    print('No se puede dibujar un rombo con esa altura')
    n=int(input('Ingrese altura impar: '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end=' ')
    for j in range(1,i*2):
        print('*',end=' ')
    print()
for i in range(2,n+1):
    for j in range(1,i):
        print(' ',end=' ')
    print('*',end=' ')
    for j in range(3,(n+1-i)*2):
        print(' ',end=' ')
    if i<n:
        print('*')
exit()
'''
#dibujito interesante
'''
n=13
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1:
            print('* ',end='')
        elif i==n:
            print('* ',end='')
        elif j==1:
            print('* ',end='')
        elif j==n:
            print('* ',end='')
        elif i==n//2+1:
            print('* ',end='')
        elif j==n//2+1:
            print('* ',end='')
        elif i==j:
            print('* ',end='')
        elif j==n+1-i:
            print('* ',end='')
        elif j==n//2+i and i<=n//2+1:
            print('* ',end='')
        elif j==(n+1)//2+1-i and i<=n//2+1:
            print('* ',end='')
        elif j==i-n//2 and i>n//2:
            print('* ',end='')
        elif j==n+1-(i-n//2):
            print('* ',end='')
        else:
            print('  ',end='')
    print()
exit()
'''
                        #EJERCICIO DE AUTOEVALUACION
''' 
Ejercicio de Autoevaluación:
Realiza un programa que ingrese números hasta encontrar 3 capicúas.(Tiempo sugerido en máquina 
1 hora máximo.)
Ejemplo:
Ingrese un número: 879
Ingrese un número:878
Es capicúa, falta 2
Ingrese un número:373211
Ingrese un número:7
Es capicúa, falta 1
Ingrese un número:475
Ingrese un número:2316
Ingrese un número:9229
Es capicúa, listo
20:10-'''

'''print('debe ingresar 3 numeros capicuas el programa dira si lo son o no')
for cuenta in range(3):
    capicua=0
    while capicua==0:
        print('Ingrese un número: ')
        num=int(input())
        desc=num
        inv=0
        while desc>0:
            inv=inv*10+(desc%10)
            desc=desc//10
        
        if inv==num:
            capicua=5352626  #para salir del bucle de capicua==0. Ahora
            if cuenta==2:   #cuenta==1, faltan 2 vueltas. cada vuelta se copleta cuando cpicua es !=0 
                texto='listo'
            else:
                texto='falta '+str(2-cuenta)
            print('Es capicúa,',texto)
        print()
exit()
'''





