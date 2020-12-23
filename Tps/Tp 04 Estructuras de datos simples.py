                    #TP  IV: ESTRUCTURAS DE DATOS SIMPLES

#PRIMERA PARTE:            "EDICIÓN" DE TEXTO 

# tipos de variables
#bool-string-char-int-float

#coercion de tipos

#int float string 
'''
a=4 
print('a =',a,'es un entero')
c=a/2
print('c = a/2 =',c,'es float pero a y 2 siguen siendo enteros')
d=('d')
print('d =',d,'es un string (en realidad un char)')
'''
# test 1 con boolean   se asocian:  Flase='''0''' true='''1''' 
'''
c=True              
d=False

e= c-d #(1-0 = 1)
f= c-1 #(1-1 = 0)
print(e,c)
print(f,d)
'''
#test 2 con boolean
'''
b=1
if b:
    print('true')
else:
    print('false')
'''
#secuencia: Una secuencia en PYTHON es un conjunto contiguo de elementos con una 
#organización interna.
'''
txt=input('hola: ')
print(txt)
'''
#ascii datazo
#Pero... Recordar que en la Tabla ASCII las mayúsculas tienen código ascii menor 
# que las minúsculas. Por lo tanto: ‘ANALIA’ será MENOR que ‘ana’. Incluso ‘Juana’ 
# es MENOR que ‘ana’.

#clase strings (secuencia ORDENADA, SOLO DATOS DEL TIPO CARACTER)
'''
s='cámara de fotos'
a=s
print(s)
b=a[2]
print(b)
c=a[0:3] #posiciones 1,2,3
print(c)
'''
'''
pais=('alemania')
ultimos=pais[5:len(pais)] #ultimos= 'nia'
print(ultimos)
'''
#métodos: Son funciones propias de una clase, se pueden aplicar sólo a objetos de 
#esa Clase. Por eso siempre llevan paréntesis!

#Ejemplos:
'''
titulo='méToDOs De lA ClaSe string'
titulo=titulo.capitalize( )  #sintx: nombre.metodo()
print(titulo)
'''
#Recorrer un texto char a char
'''
texto1 = input('Ingrese el texto: ')
print()
for i in range(len(texto1)):
    print(texto1[i],' ',sep='',end='')
print()
print('O sino')
texto1 = input('Ingrese el texto: ')
print()
for char in texto1:print(char,end=' ')
exit()
'''
'''
numero=input('ingrese un numero: ')
print(int(str(numero).replace('1','9'))) #reemplza el primer'' por el segundo
'''
'''
txt='   ALterado y sin paciencia no se alcanza la PERFECCIÓN    '
print((txt.title()).strip())  #el strip saca el espacio del principio. El tittle mete mayusulas a cada plbrs   
#print( ( nombre.metodo() ) . ( metodo2() ) . metodo3() ) 
'''
'''
nombre='Ana'
apellido=input('Cuál es el apellido de %s? '%nombre)
print('1-',nombre,apellido)
cartel='Cuál es el apellido de '+nombre+'? '
apellido=input(cartel)
print('2-',nombre,apellido)
apellido=input('Cuál es el apellido de '+nombre+'? ')
print('3-',nombre,apellido)
'''
'''
nombre='dada'
cartel='Cuál es el apellido de {}? '
cartel=cartel.format(nombre)
apellido=input(cartel)
'''
'''
apellido='Douce'
nombre ='cual es el nombre de {}?'
nombre = nombre.format(apellido) 
nombre=input(nombre)
edad=input('ingrese edad de '+apellido+'')
print(nombre, 'tiene', edad, 'años')ç
'''
'''
print('4-',nombre,apellido)
apellido=input('Cuál es el apellido de {}? '.format(nombre))
print('5-',nombre,apellido)
exit()
'''
# var.format(1er{}, 2do{})  meto en los {}{} de nombre lo q esta dentro del parentesis
#o direcramente .format(bla, ble)
'''
nom1=input('Nombre: ')
ape1=input('Cuál es el apellido de '+nom1+'? ')
cel1=input('Número de celular de {} {} 54-'.format(nom1,ape1))
cel1='54-'+cel1
ingreso=float(input('Ingreso mensual promedio de {},{}  '.format(ape1,nom1)))
print(cel1)
'''
'''
nom1=input('Nombre: ')
ape1=input('Cuál es el apellido de '+nom1+'? ')
cel1=input('Número de celular de {} {} 54-'.format(nom1,ape1))
cel1='54-'+cel1
ingreso=float(input('Ingreso mensual promedio de {},{}  '.format(ape1,nom1)))
nom2=input('Nombre: ')
ape2=input('Cuál es el apellido de {n}? '.format(n=nom2))
cel2=input('Número de celular de {1} {0} 54-'.format(ape2,nom2))
cel2='54-'+cel2
nom3=input('Nombre: ')
ape3=input('Cuál es el apellido de {0}? '.format(nom3))
cel3=input('Número de celular de {c1} {c2} 54-'.format(c2=ape3,c1=nom3))
cel3='54-'+cel3
print('Apellidos'.center(15),'Nombre'.center(15),'Nro celular'.center(10))
print('{:15} {:15} {:10} {:.2f}'.format(ape1,nom1,cel1,ingreso))
print(ape2.ljust(15),nom2.ljust(15),cel2.center(10))
print(ape3.ljust(15),nom3.ljust(15),cel3.center(10))
exit()
'''
'''
print('Apellidos'.center(30),'Nombre'.center(15),'Nro celular'.center(10))
num='un numero'
print('justificame esto'.ljust(20),num.center(15),num.ljust(12))
print()
'''
#ej 4.1
'''Confeccionar un programa en el que se ingresandos textos y determinar cuál es el 
más largo. Dejar a ambos del menor largo. (del largo del largo del menor texto)'''
'''
txt1=input('ingrese un texto: ')
txt2=input('ingrese otro texto: ')
if len(txt1) > len(txt2):
    print(txt1)
    print('es mas largo que: ')
    print(txt2)
    txt1=txt1[0:len(txt2)] #txt1= a los elementos entre su letra 0 y la letra numero  
    print('Versión corta:',txt1,sep='\n') #longitud del txt2
else:
    print(txt2)
    print('Es más largo o igual que :')
    print(txt1)
    txt2=txt2[0:len(txt1)]
    print('una version corta es', txt2, sep='\n')
'''
#Ejercicio 4.2
'''Confeccionar un programa en el que se ingresa un texto. Se debe eliminar del 
carácter 11 al 20 inclusive.
Ejemplo:
Ingrese el texto: Si quieren sAber un poco más deben Practicar bastante
Si quierenpoco más deben Practicar bastante'''# (eliminad 10 caracteres)
#[no incluye al primero, si a este segundo]
#opción 1
'''
texto=input('Ingrese un texto: ')
if len(texto)<=20:
   texto=texto[0:10] #elimino clqr cosa q supere los 10 caracteres no incluye el 10
else:
   textoaux=texto[10:20] #tomo los caracteres del 11 al 21 no incluye el 20 pero si el 10
   texto=texto.replace(textoaux,'')
print()
print('Texto Final:',texto,sep='\n')
exit()
'''
#opción 2
'''
texto=input('Ingrese un texto: ')
aux1=texto[:10] #todo hasta el 10
if len(texto)>20:
   aux1=aux1+texto[20:] 
   print(texto[20:])  #todo a partir del 20
texto=aux1
print()
print('Texto Final:',texto,sep='\n')
exit()
'''
#Ejercicio 4.3
'''Confeccionar un programa en el que se ingresa una letra a buscar y luego un texto. 
Luego, el programa debe informar cuántas apariciones de la primera hay en el texto.
Ejemplo:
Ingrese un caracter: a
Ingrese el texto: Si quieren sAber un poco mas deben Practicar bastante
a aparece 5 veces'''
'''
caracter =input('Ingrese un caracter: ')
texto1 = input('Ingrese el texto: ')
car=caracter[0]             
print('hay ',texto1.count(car),car,' en:')   #.count(loq q queres contar)
print(texto1)                          # O J O lo del parentesis tiene q ser string
exit()
'''
#ej 4.4
'''Escribir un programa que permita ingresar un texto de hasta 100 caracteres y convertirlo 
a mayúsculas completamente. 
Ejemplo:Ingrese el texto: 
Cuando estoy CANSADO todo me da igual!!
CUANDO ESTOY CANSADOTODO ME DA IGUAL!!
'''
'''
txt=input('ingrse un texto: ')
txt=txt[0:100]
print()
txt=txt.upper()
print(txt)
'''
#ej4.5
'''Confeccionar un programaen el que se ingresa una letra a reemplazar y luego un texto de 
tamaño máximo de 30. Luego, el programa debe devolver el texto con todas las apariciones
de la letra buscada reemplazada por ‘*’.
Ejemplo:
Ingrese un caracter: a
Ingrese el texto: Si quieren saber un poco mAs deben practicar bastante
Texto reemplazado: Si quieren s*ber un poco m*s deben pr*ctic*r b*st*nte
'''
#ojo el .replace distingue mayusculas de minusculas (hay q transformar)
#comparar minusculas con minsuculas o mayusc y mayusc
#ojo metodos solo para letras (no numeros o simbolitos)
'''
caracter='*'    #defino el caracter xa entrar al while
while not  (caracter.isalpha()) or len(caracter)!=1:
    caracter=input('ingrese una letra: ')
txt=(input('ingrese un texto: '))
txt=txt[0:30]
txt=txt.lower()
caracter=caracter.lower()
txt=txt.replace(caracter,'*')
print()
print(txt)
print()
'''
#Ejercicio 4.6
'''
Confeccionar un programa en el que se ingresa una letra a eliminar y 
luego un texto de tamaño máximo de 30. 
Luego, el programa debe devolver el texto con la letra completamente 
eliminada del mismo.
Ejemplo:Ingrese un caracter: a
Ingrese el texto: 
Si quieren saber un poco mAs deben practicar bastante
Texto reemplazado: 
Si quieren sber un poco ms deben prcticr bstnte
'''
'''
car='*'
while not (car.isalpha()) or (len(car)!=1):
    car=(input('ingrse una letra: '))
txt=input('ingrese un texto: ')
txt=txt[0:30]
car=car.lower()
txt=txt.lower()
txt=txt.replace(car,'')
print()
print(txt)
print()
'''
#ej 4.7
'''
Confeccionar  un  programa que inserte un nombre ingresado por teclado luego de la frase 
‘oso y’ que figure en un texto de hasta 50 caracteres también leído por teclado.
Ejemplos:Ingrese un nombre: 
anita
Ingrese el texto: En el Bosque de Tundragón juegan el oso y saltando por doquier
En el Bosque de Tundragón juegan el oso y anita saltando por doquier.
Ingrese un nombre: anita
Ingrese el texto: En el Bosque de Tundragón juegan saltando por doquier 
El texto no contiene la frase:‘oso y'''
'''
nombre='1'
while not(nombre.isalpha()):
  nombre=input('Ingrese nombre ')
nombre=nombre[0:50]
texto = input('Ingrese el texto: ')
texto=texto[0:50]
texto=texto.lower()
nombre=nombre.lower()
if texto.count('oso y')==0:
   print('El texto ingresado no contiene la frase clave:"oso y"')
else:
   texto=texto[0:texto.find('oso y')+5]+' '+ nombre+texto[texto.find('oso y')+5:]
   texto=texto[0:50]
   texto=texto.capitalize()
   print()
   print(texto)
exit()
'''
#ej 4.8
'''Confeccionar un programa que  lea  un texto y luego genere otro de exactamente 70
caracteres concatenando las veces que sea necesario el texto 
ingresado.
Ejemplos:Ingrese un texto:Lápiz azul
Lápiz azulLápiz azulLápiz azulLápiz azulLápiz azulLápiz azulLápiz azul
Ingrese un texto:casonacasonacasonacasonacasonacasonacasonacasonacasonacasonacasonacasonacas
Ingrese un texto:La clave de la Felicidad radica en una vida sana, armoniosa, social, vital 
y ordenada La clave de la Felicidad radica en una vida sana, armoniosa, social, v
'''
'''
txt1=input('ingrese un texto: ')
txt2=' '
if txt1=='':
    txt1=txt2
txt2=txt1
while len(txt2)<70:
    txt2= txt2+txt1
txt2=txt2[0:70]
print()
print(txt2)
exit()
'''
#ej 4.9
'''
Confeccionar un programa que lea un texto y lo imprima saltando un caracter. 
Ejemplos:
Ingrese el texto: Si quieren saber un poco más deberían practicar bastante
Texto recortado:
S uee ae npc á eeínpatcrbsat
Ingrese el texto: Estaba la paloma blanca sentada en un verde limón
Texto recortado:Etb aplm lnasnaae nvrelmn
'''
'''
#(v. mía)
txt=input('ingrese un texto: ')
i=0
txt2=''
b=0
for i in range (len(txt)):
    if b%2==0:
        txt2=txt2+txt[b]
    b+=1
print(txt2)
'''
'''
#(v. profe)
texto = input('Ingrese un texto: ')
print(texto[::2]) 
exit()
'''
#s[i:j:k]Referencia la porción de la secuencia s que va del elemento i al j-1, 
# con paso k. i no incluido, j incluido, k es paso. i=0/ 2 arranca 1era/ 2da letra

#ej 4.10    
'''Ejercicio 4.10
Confeccionar  un  programa que  lea  un  texto  y  lo  encripte  corriendo  sus 
letras  a  derecha  según  el alfabeto. El corrimiento debe ser circular, es decir
que a la z le sigue la a.
Ejemplo:Ingrese el texto: 
Ana es la mas CapazTexto encriptado:Bob ft mS nbt Dbqb'''
'''Pero... Recordar que en la Tabla ASCII las mayúsculas tienen código ascii menor 
que las minúsculas. Por lo tanto: ‘ANALIA’ será MENOR que ‘ana’. Incluso ‘Juana’
es MENOR que ‘ana’. Ya que la comparación se hace de izquierda a derecha, letra 
por letra comparando los códigos ascii. Se compara los primeros caracteres, si 
son distintos, el texto menor es el que comienza con el carácter con código ascii 
menor. Si son iguales se prosigue a desempatar con el siguiente. Si hay una sucesión
de caracteres iguales el primero que desempata decide, o el primer texto que acabaes
el menor'''
#chr(x) Devuelve el carácter ascii del valor x  chr(65)=‘A’
# ord(x) Devuelve el valor ascii del carácter x  ord(‘A’)=65
'''
texto2=''
texto = input('Ingrese el texto: ')
for i in range(0,len(texto)):
  if ((texto[i]>='a') and(texto[i]<'z'))or((texto[i]>='A') and (texto[i]<'Z')):
    texto2=texto2+chr(ord(texto[i])+1)
  elif texto[i]=='z':
    texto2=texto2+'a'
  elif texto[i]=='Z':
    texto2=texto2+'A'
  else:
    texto2=texto2+texto[i]  
print('Texto encriptado:')
print(texto2)
exit()
'''
                            #AUTOEVALUACION 4.1 
'''Confeccionar  un  programa que  lea  un  texto  y  lo  devuelva  depurado. Es
decir, sin blancos al principio ni al final, completamente en minúsculas, exceptuando
la  primera letra y eliminando caracteres que no sean letras o signo de puntuación
y más de un blanco como separador de palabras.
Ejemplo:Ingrese el texto:
si QUIEREN   *saber un poco mAs,debe-rían// practicar bastante.
Texto depurado: Si quieren saber un poco mas,deberían practicar bastante.'''
#opcion mia
'''
txt=input('ingrese un texto: ')
txt=txt.strip().lower()
txt2=''
while txt.count('  ')>0:
   txt=txt.replace('  ',' ')
for i in range (len(txt)):
    if ( txt[i].isalpha() or txt[i] in (';',':',';','?',',','!','(',')','.') 
    or txt[i]==' '):
        txt2=txt2+txt[i]
print(txt2.capitalize())
'''
#opcion profe
'''
texto=input('Ingrese texto:\n')
texto=texto.strip()
texto=texto.lower()
for car in texto:
   if (not(ord(car) in range(ord('a'),ord('z')+1) or car in ('á','é','í','ó','ú',',','.',';',':'))):
          #el nº ascii del caracter esta entre el de la a y la z o el carcater es á, é etc
      texto=texto.replace(car,' ')
while texto.count('  ')>0:      #si encontras mas de un espacio en blanco
   texto=texto.replace('  ',' ') #reemplaza mas de dos espacios x solo 1
print(texto.capitalize())
exit()
'''
#SEGUNDA PARTE:          TUPLAS CONJUNTOS y LIBRERIAS
'''Los módulos importables en PYTHON son librerías. Una librería es un archivo que 
contiene una colección de funciones y/o variables definidas y con valor asignado 
por terceros. NO es un conjunto de herramientas predefinidas; por eso debemos 
informarle a PYTHON en qué consiste cada recurso que estemos usando. Pero en 
lugar de reescribir, una por una,las herramientas que queramos utilizar, dejamos 
que el propio PYTHON se encargue de esa tarea ordenándole la importación.'''
'''Para poder usar el contenido de un módulo es necesario importarlo con la sentencia 
import. Esta le pide  a PYTHON que se encargue de volver conocidos dentro del programa,
algunos, o todos, los recursos del módulo.'''

#Importar al principio del programa!!!
#En PYTHON cada módulo es un objeto de la Clase librería/módulo. Por ello, todas 
#las variables que estén definidas allí son atributos de la clase y las funciones, 
#métodos. Que deben invocarse como tales.

#importacion de un modulo completo
'''
import random
from random import randint #as rd #importo el modulo random ( q es un objeto de la cla
for i in range (5):         #se libreria/modulo)
    print('Dado', i+1, random.randint(1, 6))
                       #objeto.metodo
                       #rd
'''
'''
#ahora iporto solo un metodo (radint) del modulo (random)
from random import randint
for i in range(5):
    print ('Dado',i+1,randint(1,6))
    #una tupla
'''
'''
for i in range (10):
    for b in range(10):
        print(i,b)
'''
#tuplas (secuencia de:
#DATOS ORDENADOS, INMUTABLE, CLQR TIPO DE DATO)
'''Las tuplas son una secuencia (una subclase de las secuencia) inmutable de 
objetos ORDENADOS que pueden ser de cualquier tipo, a diferencia de las string que
sólo pueden tener caracteres. Por ser una subclase de la clase secuencia son 
aplicables las funciones, métodos, operadores y modos de acceso que están 
definidos para las secuencias.'''
#UNA TUPLA ES SUBSCRIPTABLE VAR=()
'''
numeros=()
mayor=4
numeros+=(mayor,)
numeros+=('hola',)
numeros+=(3,)
print(numeros[1])
print(numeros)
'''
#UN CONJUNTO NO ES SUBSCRIPTABLE VAR = SET()
'''
numeros= set()
mayor=4
numeros.add(mayor,)
pepe=4
numeros.add(pepe,)
nombre='juan'
numeros.add(nombre,)
print(numeros[0])
'''
'''
numeros=()
# definimos la tupla numeros, sin elementos
mayor=float(input('Ingrese número 1: '))
numeros+=(mayor,)
# agregamos mayor a la tupla vacía con el operador +, equivale a
# números=números+(mayor,)
# Pero sólo puedo agregarle una tupla a otra, por eso primero armo la tupla
# con el elemento mayor
for i in range(5):
    num=float(input('Ingrese número %d: '%(i+2)))
    if num>mayor:
        mayor=num
    numeros+=(num,) # agrego todos los números a la tupla
print('El mayor es:',mayor)
print('Distancias al mayor')
print('   Número'.ljust(10), 'Distancia')
for i in range(len(numeros)):
    print('%9.2f%9.2f'%(numeros[i],mayor-numeros[i]))
#muestro los contenidos de la tupla indicando la posición ([i])
'''
#conjuntos (es una clase
# DATOS HETEROGENEOS, NO ORDENADOS, MODIFICABLE, NO REPETIDOS)
'''
hola='juan'
a={hola, 1,2,3}
print(a) #cada vez q lo imprimo lo hace en orden distinto
b={} #ojo conjunto vacio
print(b)
set=()''' #SET es una FUNCION -> crea conjunto para llenar
#Este programa permite cargar las direcciones de mail de compañeros y listarlas

'''mails=set()
dcc=input('Mail de un compañero, * para salida: ')
while dcc!='*':
    mails.add(dcc.lower())  #objeto.add agrega un elemento al conjunto
    dcc=input('Mail de un compañero, *salida: ')
while len(mails)>0:print('elimino uno al azar y lo muestro:',mails.pop())
print(mails)''' #printea un set(vacio porque con mails.pop elimine todos los elementos)
#remove() elimina elemento especifico da erro si no existe
#discard() elimina un elemento especifico
#clear() borra todo el conjunto
'''
series=('Acción','Suspenso','Comedia','Terror','Romance','Drama')
nombre=input('Ingresá tu nombre, para salir *:  ')
while nombre!='*':
    print('Durante la cuarentena...')
    mayor=-1
    preferida=''
    for tipo in ('Acción','Suspenso','Comedia','Terror','Romance','Drama'): 
# o sino for i in range(len(series)):                                 %series[i]
        cant=int(input('Ingresá la cantidad de series de %s que viste'%tipo))
        while cant<0:cant=int(input('Ingresá la cantidad de series de %s que viste'%tipo))
        if cant>mayor:                                                      #series[i]
            mayor=cant
            preferida=tipo
    print(nombre,'sos fan de las de',preferida)
    nombre=input('Ingresá tu nombre, para salir *:  ')
'''
#Ejercicio 4.11
'''Confeccionar un programa que tire una mano de cuatro naipes de póker para un 
jugador. La baraja de póker tiene 4 palos con 12 valores cada uno ( As,2,3,4,5,
6,7,8,9,J,Q,K)
Ejemplo:
7 de trébol 
Jota de corazón 
7 de diamante 
As de pica'''
'''
import random

palos='corazones','pica','diamante','trebol'
num='AS','2','3','4','5','6','7','8','9','10','J','Q','K'
import random
mano=set()
while len(mano)<4:
  mano.add(random.randint(0,51))
while len(mano)>0:
  naipe=mano.pop()
  print(num[naipe%13],'de',palos[naipe//13])

'''
'''
var='1','2','3'
mano=set()
while len(mano)<4:
    mano.add(random.randint(0,1))
while len(mano)>0:
    naipe=mano.pop()
    print(var-naipe)
'''
#Ej 4.12
'''Confeccionar un  programa  que  permita  ingresar  21  números  que  no  sean 
repetidos y  mostrar  su suma (ignorando repeticiones).
Ejemplo: Ingrese 21 números: 15
10
-3
33
15
-10...
Suma: 45(Nota:resultado parcial para los números consignados ...'''
#opcion a)
'''
print('ingrese 21 numeros no repetidos')
numeros=set()
i=1
while len(numeros)<5:
    num=int(input('ingrese numero %d: ' %i))
    numeros.add(num)
    i+=1
sum=0
for i in range(len(numeros)):
    sum+=(numeros.pop())
print('la suma total es:',sum)
'''
#opcion b)
'''
numeros=set()
print('Ingrese 21 números que no sean repetidos')
i=1
suma=0
while len(numeros)<21:
    n=int(input(' Ingrese número %d  '%i))
    if not(n in numeros):
        i+=1
        suma+=n
    numeros.add(n)
print('La suma total es: ',suma)
exit()
'''
#Ej 4.13
'''Reprograme el ejercicio 12 del TP 2. Se deberá producir aleatoriamente el número 
(entre 1 y 10) a adivinar  por  el  usuario.  También  el  usuario  deberá  elegir  
el nivel  de  dificultad  del  juego  (1,2  o  3 intentos).'''
'''
import random

numero=random.randint(1,10)
tiros=4
while not (tiros in (1,2,3)):
    print('ingrse dificultad') 
    tiros=int(input('Adivinar en 1 tiro (1), 2 tiros (2), 3 tiros (3): '))
intento=0
exito=False
while (intento<tiros) and (exito==False):
    num=int(input('Adivine el numero: '))
    if num == numero:
        exito=True
    intento+=1
if exito:
    print('Acertaste, el numero era', numero)
else:
    print('Perdiste, el numero era', numero)
'''
#ej 4.14
'''Reprograme  el  ejercicio  anterior.  Ahora  el  usuario  deberá  elegir  entre  
10,  15  o  20  intentos  para adivinar  un número del 0 al 30 (inclusive) y el 
programa deberá descartar los tiros repetidos.'''
#Opcion mia
'''
import random
numero=random.randint(0,30)
tiros=1
while not (tiros in (10,15,20)):
    print('ingrse dificultad') 
    tiros=int(input('Adivinar en 10 tiro (10), 15 tiros (15), 20 tiros (20): '))
intento=0
exito=False
numsuser=set()
while (intento<tiros) and (exito==False):
    num=int(input('Adivine el numero: '))
    if not (num in numsuser):
        numsuser.add(num)
        if num == numero:
            exito=True
        intento+=1
if exito:
    print('Acertaste, el numero era', numero)
else:
    print('Perdiste, el numero era', numero)
'''
#opcion profe
'''
from random import randint
num=randint(0,30)
tiros=4
print('Jugá a adivinar un número entre 0 y 30!!')
while not(tiros in (10,15,20)):
    print('nivel de Dificultad\nAdivinar en ...')
    print('10 - Tiros (Dif Alta)\n15 - Tiros (Dif Media)\n20 - Tiros (Dif Baja)')
    tiros=int(input())
intento=set()   #meto los intentos aca
exito=False
while (len(intento)<tiros)and(exito==False): #comparo el nº de intentos con tiros q tengo
    num1=int(input('Intento %d  '%(len(intento)+1))) # (len de la tupla intentos)
    if num1 == num:
        exito=True
    intento.add(num1) #sumo los numeros q tira el user a intentos
if exito:             #, y voy alargando el len. de a 1 unidad por cada numero
    print('Acertaste!!!')
else:
    print('Perdiste!!!')
exit()
'''
#ej 4.15
'''Confeccionar un programa que permita ingresar nombres de 17 concursantes y el puntaje
obtenido (0-100). Conservar y mostrar los 3 con mayor puntaje.'''
'''
concurso=set()
filtro=set()
for i in range(3):
   nombre=input('Ingrese nombre de Concursante:  ')
   puntaje=int(input('Ingrese el puntaje de %s :  '%nombre))
   while puntaje not in range(0,101):
      puntaje=int(input('Ingrese el puntaje de %s :  '%nombre))
   concurso.add((nombre,puntaje))
   filtro.add((nombre,puntaje))   
mayor=('',-1)
for i in range(2):
   for participante in filtro:
       if participante[1]>mayor[1]: ###################ACAAAAAAAAAAAAAA?????????
           mayor=participante
   filtro.remove(mayor)  #le saco los mayores entonces filtro contiene a los 3 menores
   mayor=('',-1)      
concurso=concurso-filtro    #le resto a concsurso (total) los menosres = solo los mayores
print('Participantes con Mayor Puntaje')
while len(concurso)>0:
   participante=concurso.pop()  #concurso vale solo menores
   print(participante[0],'obtuvo',participante[1],'puntos')
exit()
'''
#ej 4.16
'''Ingresar los legajos de los alumnos que cursan Física I en fiuba por un lado, y luego los 
legajos de los alumnos del Curso 5 de Computación. Mostrar la lista de legajos que están 
simultáneamente en ambos cursos(por ejemplo, para no agendarles examen de Física viernes de 
10:00 a 14:00...).'''
#Opcion mía
'''
fisica=set()
fyc=set()
print('ingrese legajo de alumno de fisica, 0 xa salir: ')
alfisica=int(input('Legajo: '))
while alfisica!=0:
    fisica.add(alfisica)
    alfisica=int(input('legajo: '))
print('ingrese legajo de alumno de computacion, 0 xa salir: ')
alcomputacion=int(input('Legajo: '))
while alcomputacion!=0:
    for alumno in fisica:
        if alumno==alcomputacion:
            fyc.add(alcomputacion)
    alcomputacion=int(input('Legajo: '))
if len(fyc)>0:
    print(fyc)
else:
    print('No hay alumnos que esten en los 2 cursos')
'''
#opcion profe
'''
fisica=set()
compu=set()
print('Ingrese legajos de Física I, 0 para terminar')
legajo=int(input())
while legajo!=0:
   fisica.add(legajo)
   legajo=int(input())
print('Ingrese legajos de Curso 5 Computación, 0 para terminar')
legajo=int(input())
while legajo!=0:
   compu.add(legajo)
   legajo=int(input())
viernesNo=compu&fisica  #interseccion del conjunto de computacion
print()           #con el de fisica
print('Listado de Alumnos que cursan ambas')
for alumno in viernesNo:
   print(alumno)
exit()
'''
#OPERACIONES CON CONJUNTOS
'''
tupla=(1,2,3)

nums1=set([1,2,3,4,8,'s','t'])
nums2=set([2,3,4,5,6,7,'s','t','f'])
nums3={2,3,4,5,'s','g'}
inter=nums1&nums2&nums3
print(inter)
difsimetrica=nums1^nums2 #diferencia simetrica (super util)
print(difsimetrica)
union=nums1|nums2|nums3
print(union)
'''
'''
a=[1,2,3,4]
for elem in a:
    elem=elem*10
    print(elem)
for i in a:
    print(elem)
'''
                            #AUTOEVALUACION 4.2
#Obtener los invertidos de 5 números ingresados de cualquier cantidad de cifras.
'''Ejemplo: Ingrese el número: 278 Invertido: 872 
Ingrese el número: 257080 Invertido: 080752 
Ingrese el número: 22 Invertido: 22
Ingrese el número: 1004 Invertido: 4001 
Ingrese el número: 1 Invertido: 1'''
'''
for i in range(5):
    num=int(input('ingrese un numero: '))
    num=str(num)
    reversa=() #creo una tupla distinta oara cada numero
    for car in range(len(num)):
        reversa+=(num[-(car+1)],) # el caracter nº (car+1) contando DESDE ATRAS lo concateno adelante
    print(num)
    print(reversa)    #en la tupla unum
'''
#practica módulo random
'''
for j in range(5):
   num=int(input('Ingrese número: '))
   numero=str(num)
   reversa=''
   for i in range(len(numero)):
      reversa+=numero[-(i+1)]
   print('Invertido:',reversa)
'''
'''
import random
for i in range(19):
    print(random.choice((1,2,3,4,5)),end='-')
print()
for i in range(19):
    print(random.randint(1,5),end='-')
print()
for i in range(19):
    print(random.randint(1,6),end='-')
print()
for i in range(5):
    print(random.random())
print()
for i in range(5):
    print(random.uniform(1,24))
for i in range(19):
    print(random.choice(range(1,5)),end='-')
print()
for i in range(19):
    print(random.choice('abracadabra'),end='-')
exit()
'''