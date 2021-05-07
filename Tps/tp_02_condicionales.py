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
'''

#Ejercicio 2.3
'''
Armar un programa que solicite al usuario que ingrese nombre y edad de 3 personas. 
El programa deberá indicar quién es el más joven y el más viejo.
Ejemplo:
Nombre Persona 1: Juan
Edad de Juan: 18
Nombre Persona 2:Alicia 
Edad de Alicia: 16
Nombre Persona 3: Justo
Edad de Justo: 17
El más joven es Alicia, de 16 años.El más viejo es Juan, de 18 años.
'''
#res 2.3.0
'''
nom1 = ( input() )
edad1 = int ( input() )
nom2 = ( input() )
edad2 = int ( input() )
nom3 = ( input() )
edad3 = int ( input() )

if edad1<edad2<edad3 :
    print( 'el mas joven es',nom1, 'de','edad', edad1, 'años. El mas viejo es', nom3,'de', 
         'edad', edad3)
elif edad1<edad3<edad2 :
    print('el mas joven es',nom1, 'de','edad', edad1, 'años. El mas viejo es', nom2,'de', 
         'edad', edad2)
elif edad2<edad1<edad3 :
    print('el mas joven es',nom2, 'de','edad',edad2, 'años. El mas viejo es', nom3,'de', 
         'edad', edad3)
elif edad2<edad3<edad1:
    print ('el mas joven es',nom2, 'de', edad2, 'años. El mas viejo es', nom1,'de', 
         'edad', edad1)
elif edad3<edad1<edad2 :
    print('el mas joven es',nom3, 'de','edad', edad3, 'años. El mas viejo es', nom2,'de', 
         'edad', edad2)
elif edad3<edad2<edad1 :
    print('el mas joven es',nom3, 'de','edad', edad3, 'años. El mas viejo es', nom1,'de', 
         'edad', edad1)

'''
#2.3.1
'''
nom1=input('Nombre Persona 1: ')
p1=int(input('Edad de %s: '%nom1))
nom2=input('Nombre Persona 2: ')
p2=int(input('Edad de %s: '%nom2))
nom3=input('Nombre Persona 3: ')
p3=int(input('Edad de %s: '%nom3))
if (p1<=p2)and(p1<=p3):
 print('El más joven es',nom1,', de',p1,'años')
elif (p2<=p1)and(p2<=p3):
 print('El más joven es',nom2,', de',p2,'años')
else:
 print('El más joven es',nom3,', de',p3,'años')
if (p1>=p2)and(p1>=p3):
 print('El más viejo es',nom1,', de',p1,'años')
elif (p2>=p1)and(p2>=p3):
 print('El más viejo es',nom2,', de',p2,'años')
else:
 print('El más viejo es',nom3,', de',p3,'años')
exit()
'''
#2.2.2
'''
nom1=input('Nombre Persona 1: ')
p1=int(input('Edad de %s: '%nom1))
nom2=input('Nombre Persona 2: ')
p2=int(input('Edad de %s: '%nom2))
nom3=input('Nombre Persona 3: ')
p3=int(input('Edad de %s: '%nom3))
if p1<=p2:
    if p1<=p3:
        print('El más joven es',nom1,', de',p1,'años')
        if p2>=p3:
            print('El más viejo es',nom2,', de',p2,'años')
        else:
                print('El más viejo es',nom3,', de',p3,'años')
    else:
        print('El más joven es',nom3,', de',p3,'años')
        print('El más viejo es',nom2,', de',p2,'años')
elif p2<=p3:
    print('El más joven es',nom2,',de ',p2,'años')
    if p1>=p3:
        print('El más viejo es',nom1,', de',p1,'años')
    else:
        print('El más viejo es',nom3,', de',p3,'años')
else:
    print('El más joven es',nom3,', de',p3,'años')
    print('El más viejo es',nom1,', de',p1,'años')
exit()
'''
#Ejercicio 2.4
'''
Escriba un programa en el que se ingresen 2 números y una opción( 1 – suma, 2 – resta, 
3 – multiplicación, 4 – división ) einforme el resultado de la operación. (definir una funcion(?))
'''
'''
num1 = int (input('ingrese un numero: '))
num2 = int (input('ingrese otro numero: '))
print ('ingrese una operacion: ','1+','2-','3*','4//', sep='\n')
ope = int (input() )

if ope == 1:
 print(num1 + num2)
elif ope ==2:
 print(num1-num2)
elif ope ==3:
 print(num1*num2)
else:
 print(num1//num2)
'''
#ejercicio 2.5 
'''
Elaborar un programa que calcule el impuesto que se aplica a una cierta compra de la siguiente 
forma:
- Si el importe de una compra es mayor a $500.- el impuesto serála cuarta parte.
- En caso contrario, el impuesto será la tercera.
El programa debe solicitar el ingreso de la compra y calcular elimpuesto.
Ejemplos:
Valor de la compra: 114
Impuesto: 38
'''
#res 2.5.0
'''
valor = float ( input ('ingrese el precio de un prducto: ') )
if valor >500:
    impuesto = valor/4
    print ('valor de la compra:', (valor - impuesto))
    print (impuesto)
else:
    impuesto = valor/3
    print ('valor de la compra:', (valor - impuesto))
    print (impuesto)
exit()
'''

#Ej 2.5.1
'''
importe=int(input('Valor de la compra: '))
if importe > 500:
 print('Impuesto:',importe // 4)
else:
 print('Impuesto:',importe // 3)
exit()
'''
#Ejercicio 2.6

'''
Armar   un   programa   que   solicite,   para   3   autos,   la   distancia recorrida 
(en metros) en 20 segundos. El programa deberá mostrarlos autos ordenados en forma decreciente 
por su velocidad. #no importan los 20 segs puesn todos recorren 20
'''
'''
d1 = float ( input('ingrese distancia del auto 1 (1): ') )
d2 = float ( input('ingrese distancia del auto 2 (2): ') )
d3 = float ( input('ingrese distancia del auto 3 (3): ') )
print ('resultado: ')
if (d1<=d2<=d3):
    print('(3)', '(2)', '(1)', sep = '\n')
elif (d1<=d3<=d2):
    print('(2)', '(3)', '(1)', sep = '\n') 
elif (d2<=d1<=d3):
    print('(3)', '(1)', '(2)', sep = '\n') 
elif (d2<=d3<=d1):
    print('(1)', '(3)', '(2)', sep = '\n') 
elif (d3<=d1<=d2):
    print('(2)', '(1)', '(3)', sep = '\n') 
else:
    print('(1)', '(2)', '(3)', sep = '\n') 
'''
#ejercicio 2.7
'''
Ejercicio 2.7
Confeccionar un programa que solicite una fecha. El usuario ingresará el día, el mes y el año 
por separado. Luego el programa imprimirá una leyenda si la fecha ingresada es válida.
Ayuda:Para saber si un año es bisiesto: Si el año es divisible por 4, es bisiesto. Pero si el año es 
divisible por 100 debe ser también divisible por 400. Por ejemplo: el año 2000 es bisiesto pero el 
1900 no lo es.
'''
''''
dia = int (input('ingrese un dia: '))
mes = int(input('ingrese un mes: '))
ano = int(input('ingrese un ano: '))

if  ( ( (dia in range(1,32) ) and (mes in [1,3,5,7,8,10,12]) )
 or ( ((dia in range(1,31)) and (mes in [4,6,9,11]) ) )
 or ( (dia in range (1,29)) and (mes==2) )
 or ( ((dia==29) and (ano % 100 != 0) and ( ano%4 ==0)  ) )
 or ((dia == 29) and ((ano %400) == 0) ) ):
 print ('es correcta')
else:
    print ('no es correcta')
'''
#Ejercicio 2.8
'''
Confeccionar un programa en el que se ingrese un número y que se imprima por pantalla si el número
es positivo, negativo o cero.
'''
'''
num1 = float ( (input ('ingrese un numero: ')))

if num1>0 :
    print ('el numero es positivo')
elif num1 <0:
    print('el numero es negativo')
else:
    print('el numero es cero')
'''
#Ejercicio 2.9

'''Confeccionar un programa que solicite 3 notas de parciales obtenidas por un alumno. A continuación 
se imprimirá por pantalla un mensaje que indique la situación del alumno:
1.Si el alumno aprobó los 3 parciales (nota 4 o más) y supromedio  es mayor  a 7,  promociona la 
materia con  la nota promedio.
2.Si el alumno aprobó los 3 parciales pero su promedio no supera los 7 puntos, debe rendir examen 
final.
3.Si el alumno no aprobó uno o más parciales, se solicitará que se ingrese la nota de un recuperatorio
(general). Si éste hubiera sido aprobado, se informará el promedio general (3parciales + el recuperatorio) 
y su condición de aprobado (aún cuando el promedio no supere los 4 puntos). Si no hubiera aprobado
el recuperatorio se informará que el alumno fueaplazado.'''
#resolucion 2.9
'''
print('ingresa tus tres nota parciales')
nota1 = float (input('1 er parcial: '))
nota2 = float (input('2 do parcial: '))
nota3 = float (input('3er parcial: '))
prom = ( ((nota1 + nota2 + nota3)/3) )

if ( (nota1>4) and (nota2>4) and (nota3>4) and (prom>=7) ):
    print('wena promocionaste')
    print ('promedio general:', prom)
else:
    if (nota1<4 or nota2<4 or nota3<4):
        recup = float (input('bueno a ver la nota de tu recup pibe?: '))
        if recup>=4:
            prome = ( (nota1 + nota2 + nota3 + recup)//4 )
            print ('buenardo zafaste, vas a final')
            print ('promedio general:', prome)
        else:
            print('a recursar  recursar loco, shiao t dijo q no uses resueltos')
    else: 
        print('weno no promocionaste pero vas a final') 
        print ('promedio general:', prom)
exit()
'''
#ejercicio 2.10
'''Confeccionar un programa que solicite un número positivo. Si elnúmero es par, mostrar el siguiente par;
si es impar, el anterior impar; si el número ingresado es 1 indicar que es el primer impar y no hay
anteriores.
Ejemplos:
Ingrese un número positivo: 2
Siguiente par es: 4
Ingrese un número: 3
Anterior impar es: 1
Ingrese un número: 1
1 es el primer impar'''
'''
num =  int ( input ('ingrese un numero positivo: ') )
if (num !=1) and (num!=0):
    if (num%2==0):
        print('seiguiente par es:', num +2)
    else:
        print ('el anterior impar es:', num-2)
else:
    if num==1:
        print('1 es el primer impar y no hay anteriores')
    else:
        print('el cero no es ni par ni impar')
exit()
'''
#ejercicio 2.11
'''Confeccionar un programa en el que se ingresen dos números enteros positivos. Luego deberá restar
el menor del mayor e indicar si dicha diferencia es un valor que está entre ambos números (es decir,
la diferencia es mayor que el más chico y menor que el más grande de los ingresados).
Ejemplo:
Ingrese primer número positivo:200
Ingrese segundo número positivo: 44
La diferencia es: 156, mayor que 44
Ingrese primer número positivo: 33
Ingrese segundo número positivo: 42
La diferencia es: 9, menor que 33'''
#resolucion 2.11
'''
num1= int (input('ingrese un primer numero positivo: ') )
num2= int (input('ingrese un segundo numero positivo: ') )
if num1>num2:
    may=num1 
    men=num2
else:
    may=num2
    men=num1
dif = may-men
if (men<dif):
    print('la diferencia es',dif, 'mayor que', men)
    if (dif<may):
        print('tambien menor que',may,'.','Entonces esta entre ambos')
    else:
        print('print la diferencia es mayor que', men,'y que', may )
else:
    print ('la diferencia es:', dif, 'menor que', men, '\n','Entonces es menor que', men,'y que', may)
''' 
#ejercicio 2.12
'''Confeccionar un programa que contenga un número del 1 al 10 como constante. Luego el programa dará 
tres oportunidades de ingresar números para adivinarlo. Cuando se acierte el número, el programa 
imprimirá un mensaje de victoria y terminará (en este caso, no se solicitarán más ingresos si aún 
quedaran oportunidades). Si luego de las 3 oportunidades no se adivina el número, se imprimirá un 
mensaje de derrota.
Ejemplo: (el número a adivinar es 8)
Adivine el número del 1 al 10: 
6
No.
Otra oportunidad: 5
Tampoco.
Última oportunidad: 8
Acertaste!!!
Adivine el número del 1 al 10: 1
No. Otra oportunidad: 2
Tampoco. Última oportunidad: 9
Perdiste!!!'''
#res 2.13
'''
num = int (input('ingrese el numero a adivinar: '))
rta= int (input ('adivine el numero del 1 al 10: '))
if rta==num:
    print ('Victoria! Acertaste!')
else:
    rta= int (input('Incorrecto, segunda oportunidad: ')) 
    if rta==num:
        print('Victoria! Acertaste!')
    else:
        rta= int(input('Incorrecto, ultima oportunidad: '))
        if rta==num:
            print('Victoria! Acertaste!')
        else:
            print('No, perdiste! El numero era', num)
exit()
'''
#ejercicio 2.13
'''Confeccionar un programa en el que se ingrese un número entero positivo. Luego se solicitará lo 
siguiente: si el número es múltiplo de 5, se solicitará que se ingrese un número menor; si  no, se 
solicitará un número mayor. Verificar si el segundo ingresoes correcto o incorrecto indicando dicha 
situación con un mensaje por pantalla.Ejemplo:
Ingrese un número entero positivo: 6
Ingrese un número mayor que 6: 10
Correcto!
Ingrese un número entero positivo: 15
Ingrese un número menor que 15: 20
Incorrecto!'''
#resolucion 2.13
'''
num = int(input('ingrese un numero entero positivo: '))

if num%5==0:
    rta=int(input('ingrese un numero menor que %i: '%num))
    if rta<num:
        print('Correcto!')
    else:
        print('Incorrecto')
else:
    rta = int((input('ingrese un numero mayor que %i: '%num)))  
    if rta>num:
        print('correcto')
    else:
        print('incorrecto')
exit()
'''
#ejercicio 2.14
'''Confeccionar un programa en el que se ingrese un número. Si el número es negativo solicitar el 
ingreso de un número par; si por el contrario fuera positivo pedir el ingreso de un impar. 
Controlar que los ingresos sean correctos. Si el número ingresado originalmente fuera 0 no solicitar
nada más.
Ejemplos:
Ingrese un número: 6
Ingrese un número impar: 1
Correcto!
Ingrese un número: -6
Ingrese un número par: 1
Incorrecto!
Ingrese un número: 0
Correcto! 2:56 -3:22''' 
#resolucion 2.14
'''
num=int(input('ingrese un numero, recuerde que el cero no es par ni impar...: '))
if num<0:
 rta=int(input('ingrse un numero par: '))
 if rta%2==0 and rta!=0:
    print('correcto!')
 else:
    print('incorrecto!')
elif num>0:
 rta=int(input('ingrse un numero impar: '))
 if rta%2!=0 and rta!=0:
    print('correcto!')
 else:
    print('incorrecto!')
else:
    print('nice number, friendly reminder that 0 is neither par not impar')
exit()
'''
#Ejercicio autoevaluacion
'''Ejercicio de Autoevaluación:
Realiza un programa que determine si un número de 3 cifras ingresado es capicúa.
(Tiempo sugerido en máquina 1 hora máximo.)
Ejemplo:
Ingrese un número de tres cifras:
879
879 no es capicúa
Ingrese un número de tres cifras:
373
373 es capicúa'''
'''
num = int(input('ingrese un numero de 3 cifras: '))
numxaprint=num
c1 = num//100       #c1 = 373//100 = 3
num = num%100       #num= 373//100 = 73
c2= num//10         #c2= 73//10 = 7
c3= num%10          #c3 = 73%10 = 3

if c1==c3:
    print(numxaprint,'es capicua')
else:
    print(numxaprint,'no es capicua')
'''




