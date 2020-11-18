####OJO LAS COMAS VAN CON PUNTOS####

#ejercicio 1.3
''' Confeccionar un programa en el que se ingrese la base y la altura de un triángulo e informe su superficie.
Ejemplo:Ingrese base del triángulo: 20
Ingrese altura del triángulo: 4.6
Para una base de 20.00 y una altura de 4.60 la superficie del triángulo será de: 46.00
'''
#resolucion 1.3
'''
print('CALCULO DE AREA DE TRIANGULO')

print('ingrese la base del triangulo')
b = float (input())

print('ingrese la altura del triangulo')
h = float (input())

area = (b*h)/2

print('para una base de',b,'y una altura de',h,'el area del triangulo es',area)
exit()
'''
#ejercicio 1.4
'''Confeccionar un programa en el que se ingrese un monto expresado en dólares y 
la cotización del dólar y luego imprima dicho monto en pesos.
4.a- Deberá aceptarse los datos con precisión decimal y mostrar el resultado del mismo modo.
4.b- Deberá aceptarse datos enteros y mostrar un resultado con precisión decimal.
4.c- Deberá aceptarse datos con precisión decimal y mostrar un
resultado entero.
'''
#resolucion 1.4
'''
print ('CASA DE CAMBIO')
print('solo puede comprar un numero entero de dolares')
print('su cotizacion en cambio es un numero decimal')
print('como somos buena onda tomamos la parte entera del precio q tengas q pagar')

saludo = 'mas'
print ('buenos dias')
while saludo == 'mas':
    print ('cunatos dolares quiere comprar?')
    amount = int (input())
    if 0<=amount<=200:
        print('el dolar cotiza hoy en la city portenia a')
        dolarPrice = float (input())
        
        deuda = int(amount*dolarPrice)
        
        print ('son', deuda ,'ARS', '.escriba "mas" para comprar mas o cualquier otra', 
        'cosa para retirarse')
        saludo = input()
    
    elif amount<=0:
        print('no queias comprar dolares?')

    elif amount >= 200 :
        print ('JAJAJJA vivis en argentina y tenes cepo de 200 USD')
        
else:
    print('si, deja de fugar dolares vas a hacer defaultear el pais')
    exit()
'''
#ejrcicio 1.5
'''Confeccionar un programa en el que se ingrese un monto expresado en pesos y la cotización del dólar y luego 
imprima dicho monto en dólares.
5.a- Deberá aceptarse los datos con precisión decimal y mostrar el resultado del mismo modo.
5.b- Deberá aceptarse datos enteros y mostrar un resultado con precisión decimal.
5.c- Deberá aceptarse datos con precisión decimal y mostrar un resultado entero.
'''
#resolucion 1.5
'''
print("cuantos pesos quiere comprar?")
amountInPesos = int(input())

print ('el dolar cotiza hoy en la city porteña a')

dolarPrice = float(input()) 
print ('ARS')

deuda = (1/dolarPrice)*amountInPesos   

print ('son', deuda, 'USD')
exit()
'''
#ejercicio 1.6
''' Elaborar un programa en el que se ingrese una cantidad expresada en segundos y luego la
exprese en días, horas, minutos y segundos.
Ejemplo:
Ingrese tiempo en segundos: 87708 
1 día(s), 0 hora(s), 21 minuto(s), 48 segundo(s).
'''
#resolucion 1.6
'''
print ('¿cuantos segundos dedico ud a pensar el ejercicio sin mirar el resuelto?')
segundos = float(input())
#teach program a time meassuring system
segunodosEnUnDia = 60*60*24
segundosEnUnaHora = 60*60
segundosEnUnMinuto = 60

dias = int((segundos//segunodosEnUnDia))
horas = int((segundos%segunodosEnUnDia)//segundosEnUnaHora)
minutos = int(((segundos%segunodosEnUnDia)%segundosEnUnaHora)//segundosEnUnMinuto)
segundos = (int((segundos%segunodosEnUnDia)%segundosEnUnaHora)%segundosEnUnMinuto)

print (dias,'día(s)',horas,'hora(s)', minutos,'minuto(s)',segundos,'segundo(s)')
exit()
'''

#ejercicio 1.7
'''
Ejercicio 1.7
Confeccionar un programa en el que se ingresen 5 notas de exámenes y luego imprima el 
promedio general redondeando a una cifra decimal.
Ejemplo:
Ingrese las 5 notas de exámenes: 10 8 4.75 9 6.5
El promedio general es: 7.6
'''
#resolucion 1.7
'''
print ('ingrese sus 5 notas. dsps de cada una presione enter')
nota1= float(input())
nota2= float(input())
nota3= float(input())
nota4= float(input())
nota5= float(input())

promedio= round(((nota1 + nota2+ nota3 + nota4 + nota5)/5),ndigits=1)
print('su promedio es', promedio)
'''
#ejercicio 1.8
'''
Desarrollar un programa en el que se ingrese un número de 4 dígitos y que luego imprima cada
dígito separado por un guión.
Ejemplo:
Ingrese número: 5962
Separación en dígitos: 5-9-6-2
'''
#resolucion ejercicio 1.8
#(como estoy con sueño y fiaca la voy a hacer corta)
'''
print ('ingrese un numero de 4 digitos')
numero = (input())
print (numero[0],'-',numero[1],'-',numero[2],'-',numero[3])
'''
#ejercicio 1.9
'''
Elaborar un programa en el que se ingrese un número positivo y, a continuación, se imprima 
el doble y el impar siguiente.
Ejemplos:
Ingrese número: 5
Doble: 10 Siguiente impar: 7    Ingrese número: 6   Doble: 12   Siguiente impar: 7
'''
#resolucion 1.9
'''
print('ingrese un numero positivo y entero')
num = int (input())
doble = 2*num
sigImpar = num%2+num+1
print ('doble:',doble,)
print ('siguiente impar',sigImpar)
'''
#Ejercicio 1.10
'''Hacer un programa en el que se ingrese una distancia en kilómetros y la exprese en 
centímetros y metros.
Ejemplo:
Ingrese distancia en kilómetros: 51
Son 5100000 centímetros
Son 51000 metros
'''
#resolucion 1.10
'''print ('CONVERSOR DE UNIDADES')
print ('ingrese una distancia en km')
distanciaEnKm = float(input())
distanciaEnM = distanciaEnKm*(1000)
distanciaEnCm = distanciaEnM*(100) 
print('son', distanciaEnCm, 'Cm','0', distanciaEnM, 'm')
'''
#ejecicio 1.11
'''Ejercicio 1.11
Hacer un programa en el que se ingrese un número par y muestre los cuatro siguientes 
pares.
Ejemplo:
Ingrese un número par: 6
Los cuatro pares siguientes son: 8 -10 -12 -14
'''
'''
#resolucion 1.11
print('ingrese un numero par')
num = int(input())
print('los 4 pares siguientes son', num+2,'-', num+4,'-', num+6,'-', num+8)
'''
#ejercicio 1.12
'''Hacer un programa en el que se ingrese un múltiplo de 11 y muestre
los tres siguientes múltiplos de 11.
Ejemplo:
Ingrese un múltiplo de 11: 121
Los tres múltiplos de 11 siguientes son:
132 -143 – 154
'''
#resolucion 1.12
'''
print ('ingrese un multiplo de 11')
num = int(input())
print ('los 3 multiplos de 11 siguientes son', num+11,'-', num+22,'-', num+33,)
'''
#ejercicio 1.13
'''
Ejercicio 1.13
Hacer un programa en el que se ingresen dos números positivos y se muestre un común 
múltiplo de ambos.
Ejemplos:
Ingrese primer número positivo: 10
Ingrese segundo número positivo: 3
30 es múltiplo de 10 y de 3
Ingrese primer número positivo: 7
Ingrese segundo número positivo: 5
35 es múltiplo de 7 y de 5
'''
#resolucion 1.13
'''
print ('ingrese primer número positivo')
positvo1 = int (input ())
print('segundo número positivo')
positivo2 = int(input())
print (positvo1*positivo2,'es multiplo de', positvo1,'y', positivo2)
'''
#AUTOEVALUACION: 
'''
Realiza un programa que permita ingresar un número de 3 cifras e imprima su inverso y 
el doble de este último. (Tiempo sugerido en máquina 1 hora máximo.)
Ejemplo:
Ingrese un número de tres cifras:
879
879 invertido es 978
El doble de 978 es 1956
'''
#RESOLUCION MIA 3:15 - 4am (45 min) (no funciona para 0yz o 00z)

'''
num= int(input())
aux1 = (num//10)*10
primerCifra = int(num%aux1)
aux2 = (num//100)*10
aux3 = num//10
segundaCifra = aux3 % aux2
terceraCifra = num//100
#print (primerCifra)
#print (segundaCifra)
#print (terceraCifra)
numInvertido = (primerCifra*100+segundaCifra*10+terceraCifra)
dobleNumInvertido = 2*numInvertido
print (num, 'invertido es', numInvertido)
print ('el doble de', numInvertido, 'es', dobleNumInvertido)
'''

#Ej Autoevaluacion 1 X PROFE
'''
print('Ingrese un número de 3 cifras: ')

num=int(input()) #xyz tres cifras, x y z 

d1=num //100    #primera cifra, la centena "x"

num=num % 100   #redefino el numero como el resto de su divion entera x 100 (me queda -yz)

d2=num // 10    #con el nuevo numero, su divion entera yz//10 me da la decena "y"

d3=num % 10     #y el resto de esa divion me da la unidad "z"

inverso=d3*100 + d2*10 + d1 #sumo digitos como integers

print('El inverso es:',inverso)

print('El doble de ',inverso,' es ',inverso*2)

exit()
'''
'''
b= 7//2  
c= 7%2
print(b)
print(c)
''' 
#copia libro algo 1
'''
millas = int(input('cunatas millas'))
pies = int(input('ingrese algo'))
pulgadas = int(input('cuantas pulgadas'))

metros = 1609.344*millas + 0.304*pies + 0.0254*pulgadas
print(metros)
''' 

#practica renglones input print con ej extra 
# * salto de linea \n (se pued usar en sep)
# sep = 'caracter para separar plbrs'     end =  '' mantiene el renglon
'''
a = int(input('alfajorcitos: '))
b = (3*a)
c = int( round ( ( (1/5)*a ), ndigits=0) )

d = 10*a
e = 12.5*a

print ('Necesitaras\n','1-', b,'gr de azucar\n','2-',c,'toneladas de chocolate\n','3-',
c,'huevos\n','4-', d,'gr de harina\n','5-',e, 'soretes',)

print('Yo\nSoy')
print('un',end= '')
print(' renglón')
'''
#practica de
# * variables dentro de un input (var = input ('texto')) 
# * mascara sintax: var = (input (%s ' %VariableCuyoContenidoQUieroLlamar))
'''
NombreHermanoMenor = input('ingresa el nombre del hermano menor ')
edadHermanoMyor = int(input('ingresa la edad de %s ' %NombreHermanoMenor))
print (edadHermanoMyor +1)
'''

#   E J E R C I C I C I O S    E X T R A   P R A C T I C A     1   #
#ej 1.1 fiaca xd

#ej 1.2 
#leccion: puedo meter cuantas funciones quiera adedntro de otra siempre y cuanado respete lo basico
'''
print(input('Ingresa un numero '))
print(input('Ingresa un numero '),input('Otro '), sep= '\n' )
'''

#Ejercicio 1.3
'''
Confeccionar un programa en el que se ingresen un par de números enteros. Calcular y 
mostrar la distancia entre ellos.
Ejemplos:
Ingresá un número entero: -133
Ingresá otro número entero, además de -133: -3
(-133)->(-3)=130
Ingresá un número entero: 33
Ingresá otro número entero, además de 33: -33
(33)->(-33)=66
Pista: Explorá la sección Funciones y Métodos Predefinidos para Números del PP
'''

#resolucion 1.3
'''
n1 = int ( input (' ingrese un numero entero ') )
n2 = int ( input ('ingrese otro numero entero ademas de %s : ' %n1 ))
dist = abs(n2-n1)
if n1 <= n2:
    print ('(',n1,')','->', '(', n2, ')' "=", dist)
else:
    print ('(',n2,')','->', '(', n1, ')' "=", dist)
'''
#ejercicio 1.4
'''
Ejercicio 1.4
Para la siguiente receta:   
15 alfajorcitos
3 yemas    
250 gr fécula maíz 
300 gr harina de trigo
Ralladura limón c/n
Esencia de vainilla c/n
150 gr Azúcar
200 gr manteca
Confeccionar un programa que solicite una cantidad deseada de alfajorcitos e informe ingredientes y cantidades correctas.
Ejemplo:
Calculadora de Ingrediente, Ingresá la cantidad de alfajorcitos que querés hacer: 28
Necesitarás
1- 6 un de Yemas
2- 466 gr de Fécula de Maíz
3- 560 gr de Harina
4- Ralladura de Limón c/n
5- Escencia de Vainilla c/n
6- 280 gr de Azúcar
7- 374 gr de Manteca
'''
#resolucion 1.4

'''
alfajorcitos = int(input('ingrese la cantidad de alfajorsitos que queres hacer: '))

RelacAlf = 15


yemas = int (round ( float ( (3/15)*alfajorsitos ), ndigits = 0) )
fecMaiz = int (round ( (float ((250/15)*alfajorsitos) ), ndigits = 0) )
harina = int (round ( (float ((300/15)*alfajorsitos) ), ndigits = 0) )
ralladuraLimon = int( alfajorsitos*1) 
escenciaVainilla = int (alfajorsitos*1)
azucar = int ( round (float ( (150/15)*alfajorsitos ), ndigits = 0 ) )
manteca = int ( round ( float ( (200/15)*alfajorsitos )) )

print ('Necesitaras: \n1-', yemas, 'yemas\n2-', fecMaiz, 'gr de fecula de maiz\n3-',
harina, ' gr de harina\n4-', 'Ralladura de Limón c/n \n5-', 'Escencia de Vainilla c/n \n6-',
azucar, 'gr de azucar \n7-', manteca, 'gr de manteca')\
'''
'''
numero = input() #toma lo que pongo como strings
print(numero*5)
'''
#ejercicio 1.5
'''
Ejercicio 1.5
Confeccionar un programa en el que se ingresen 10 números (1 o 2). Serán las selecciones de una 
encuesta (que tiene sólo dos opciones, 1 o 2). Informar cuál fue la cantidad de respuestas opción 
1 y cuál la de respuestas opción 2.
Ejemplo:
Ingrese 10 opciones (1y2)
1
2
2
1
1
1
1
1
2
1
Opción 1: 7
Opción 2: 3
'''
#resolucion ej 1.5
'''
print ('ingrese 10 opciones (1 y 2 )')
preg1 = int (input ('ingrese 1 o 2: '))
preg2 = int (input ('ingrese 1 o 2: '))
preg3 = int (input ('ingrese 1 o 2: '))

preg4 = int (input ('ingrese 1 o 2: '))
preg5 = int (input ('ingrese 1 o 2: '))
preg6 = int (input ('ingrese 1 o 2: '))
preg7 = int (input ('ingrese 1 o 2: '))
preg8 = int (input ('ingrese 1 o 2: '))
preg9 = int (input ('ingrese 1 o 2" '))
preg10 = int (input ('ingrese 1 o 2: '))

#cada vez q escribis el numero 2, le restamos 1 que, casualmente, 
# es la cantidad de veces q lo ingresaste
#lo separe en 2 para q se vea mas lindo xddddd

opcion2Pregunta1a5 = preg1-1 + preg2-1 + preg3-1 + preg4-1 + preg5-1
opcion2Pregunta5a10 =  + preg6-1 + preg7-1 + preg8-1 + preg9-1 + preg10-1
opcion2total = opcion2Pregunta1a5 + opcion2Pregunta5a10
opcion1 = 10 - opcion2total
'''
'''
print ('opcion 1:', opcion1)
print ('opcion 2 ', opcion2total)
'''
'''
print('Opción 1:',opcion1,'\nOpción 2:',opcion2total)
'''
#1.5 hecho por profe
# 5a parecido a mi metodo va haciendo las sumas de a poco y se las carga a la variable
'''
print('Ingresá 10 respuestas (1/2)')
opc1=0
opc2=0
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
n1=int(input())
opc1+=n1%2
opc2+=n1//2
print('Opción 1:',opc1,'\nOpción 2:',opc2)
exit()
'''
'''
n1 = int (input())
opc1 = 0
opc2 = 0
n1= int (input())
opc1 +=1
opc1 +=3
opc1 +=3

print (opc1)
'''
'''
#5b muy bicho, invento un contador diciendole al user que ingrese un cero para opcion 1
#y un 1 para opcion 2 entonces solo cuento las opc2  sumandolas porque le pedi que escriba
#1, que es justo la cantidad de veces q la ingreso
print('Ingresá 10 respuestas \n0- Opción 1\n1- Opción 2')
opc2=0
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
n1=int(input())
opc2+=n1
print('Opción 1:',10-opc2,'\nOpción 2:',opc2)
exit()
'''