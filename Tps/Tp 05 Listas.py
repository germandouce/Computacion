#TP5 LISTAS

#          Parte 1
#crear una lista
'''
a=[]
a.append(4)
print(a)
'''
#metodo para copiar dsitintas regiones de la memoria
'''
pares=[1,2,3]
num=pares.copy()
print(num)
'''
'''Si quieres “fotocopiar” un objeto mutable; es decir, hacer una copia en otra parte de memoriadel 
objeto como está en ese momento, una fotografía, debes usar el método copy()o copiar elemento por 
elemento, o por partes.'''
'''
conj1={1,2,3}
conj2=conj1.copy()
'''
#misma region de la memoria
'''
conj1={1,2,3}
conj2=conj1
'''
#LISTAS: # SECUENICA (ORDENADA), HETEROGENEA, MUTABLE, ADMITE REPETICIONES
'''Una listaen PYTHON, esuna secuencia mutablede objetos heterogéneos. Es decir... Son secuencias, por 
lo tanto el orden interno importay admiten, como todas las secuencias, un acceso directo (tomo 
directamente él o los elementos que deseo, PYTHON va directo a su ubicación); son mutables, por ello pueden 
cambiar de tamaño y de contenido total, o por partes y son heterogéneas, por lo que pueden 
contener cualquier tipo de objeto (otra lista, por ejemplo).'''
'''
a=[1,2]
b=[4]
c=[True,'Hola',56, (1,2)]
d=c #misma region
print(d)
'''
#crear y agrfegar elementos
'''
lis=[]
lis=[1,2,'ya']
lis[2]='hola' #cambio el valor del elemento 2 (antes 'ya') por 'hola' 
lis.append(9)
print(lis)
'''
#Ejemplo con Listas
# # for con una parte de lista
'''
from random import randint
a=[]
for i in range(20):
    a.append(randint(1,35))
print('Segunda Mitad')
for n in a[10:]:    #elementos desde el 10 hasta el final
    print(n,end=' ')
print()    
print('Primera Mitad')
for n in a[:10]:    #elementos hasta e 10
    print(n,end=' ')
print()
'''
#GUIA DE EJERCICIOS
'''Elaborarun programa que permita cargar una listacon 10 números. Luego obtener el valor máximo y el
valor mínimo presentes en ella y determinar cuál está más cerca del promedio de valores ingresados.'''
#ej 5.1
#opción a
'''
l1 = []    #creacion de lista l1
print('Ingrese los 10 números')
for i in range(10):
  l1.append(int(input()))   #agrego los numeros hasta el 10 a l1
print()
print('La lista leída es')
print(l1)
print()
mayor=max(l1)   #mayor es una funcion de la clase conjunto
menor=min(l1)   #idem para menor
print('El mayor de la lista es: ', mayor)
print('El menor de la lista es: ',menor)
suma=0
for i in range(10):
  suma=suma+l1[i]   #0 + cada elemento de la lista 1 x 1
suma=suma/len(l1)   # suma es el promediio en castellano
difmay=abs(mayor-suma)  #para diferencia hago el mayor menos el promedio
difmen=abs(suma-menor)
if difmay>difmen:
  print(menor,'Está más cerca del promedio que es: ', suma)
else:
  print(mayor,'Está más cerca del promedio que es: ', suma)
'''
#opcion b
'''
l1 = []  #creacion de lista l1
suma=0
print('Ingrese los 10 números')
for i in range(10):
  l1.append(int(input()))
  suma+=l1[i]   #suma es la suma literal
print()
print('La lista leída es')
print(l1)
print()
print('El mayor de la lista es: ', max(l1))
print('El menor de la lista es: ',min(l1))
if max(l1)- suma/10 < suma/10-min(l1): #resum0 el mayor - el promedio
      #max- promedio < promedio - min
  print(max(l1),'Está más cerca del promedio que es: ', suma/10)
else:
  print(min(l1),'Está más cerca del promedio que es: ', suma/10)
'''
#ej 5.2
'''Confeccionar un programa que solicite al usuario la carga de unalista de 10 elementos con números 
entre 20 y 40. Presentar luego un informe que indique qué cantidad de veces salió cada valor.'''
'''
l1=[]
print('Ingrese los 10 números')
for i in range(10):
    num=int(input('Ingrese un número entre 20 y 40  '))
    while (num<20) or num>40:
        num=int(input('Sólo números entre 20 y 40  '))
    l1.append(num)
print()
print('La lista leída es')
print(l1)
print()
l2=[0]*21   #efectivamente, la l2 es un 0 repetido 21 veces
for i in range(len(l1)):
  l2[l1[i]-20]=l2[l1[i]-20]+1 #xa i=?-->21
# l2[    1   ]=l2[   1    ]+ 1 = 1
#le asigno a  =     0      + 1 = 1        Voy sumando 1 cada vez q me toca el numero 21 
#l2= ; ; ;0;0,      
  #le asigno al elemento de la posicion de la l2, el numero siguiente 
print(' Valor   Cantidad')
for i in range(21):
  print('%6d %8d'%(i+20, l2[i]))
                #i+20 salio l2[i] veces, la posicion l2[i] vale lo me da lo de arriba
'''
#ej 5.3
''' 
Ingresar números naturales(incluido el 0) en una lista. Finalizar la carga con un número negativo. 
A continuación mostrar una gráfica de ‘*’ representando cada cantidad ingresada.
Ejemplo:
Ingrese número: 10
Ingrese número: 20
Ingrese número: 0
Ingrese número: 55
Ingrese número: -1
Gráfico:********** (10)******************** (20)(0)******************************************************* (55)
'''
'''
l1=[]
print('ingrese numeros positivos o 0 ( salida con negativo)')
num=int(input())
while num>=0:
    l1.append(num)
    num=int(input())
print()
print('la lista leida es')
print(l1)                          #Opcion b:
print()                                     #for i in range (len(l1)): #xa cada numero 
for i in range (len(l1)):                       #for j in range (l1[i]): #el rango de cada elemento 
    print('Gráfico: ','*'*l1[i],'(',l1[i],')')   #print('*', end='')   #q equivale a cada numero
                                                #meteme un * cada vuelta, siendo el total de vueltas
                                                # el elemento l1[i], es decir el numero             
'''
#CLAVE DE EJERCICIO: usar el valor de las posiciones como un numero

#ej 5.4
'''
Confeccionarun programa que permita cargar números enteros positivos en una lista hasta que el usuario 
ingrese 0. No se permitirá al usuario cargar 2 veces el mismo valor, en dicho caso se mostrará un 
mensaje. Luego, informe la cantidad final de números cargados e imprima lalista resultante.
'''
'''
l1=[]
print('ingrese numeros enteros positivos. 0 xa cortar')
num=float(input())
while num!=0:
    if num%1==0 and num >0:
        if  num in l1:            #if l1.count(num)==0
            print('ya lo cargo')    #l1.append(num)
        else:                     #else:                      
            l1.append(int(num))           #ya lo cargo
    else:    
        print('solo enteros positivos: ')
    num=float(input())
print('el total de nºs cargados es', len(l1))
print('Lista resultante')
print(l1)
'''
#ej 5.5
'''Cargar 20 elementos positivos en una lista. Dejar sólo una repetición de cada uno en ella. 
Mostrar la lista final.'''
#opcion mia
'''
l1=[]
print('cargue 20 elementos positivos')
i=0
while i<20:
    num=int((input('ingrese elemento: ')))
    if num>0 and num not in l1:
        l1.append(num)
        i+=1
print(l1)
'''
#opcon profe a)
'''
l1 = []  
print('Ingrese 20 números ')
for i in range(20):
  l1.append(int(input()))   #cargo 20 elementos en la l1
l2=[] 
for ele in l1:
  if ele not in l2: #voy copiando los elementos de la
    l2.append(ele)  # l1 en la l2 solo si no lo pase todavia
l1=l2   #le asigno a la l1 los valores de la l2
print(l1)
'''
#opcon profe b)
''''
l1 = []
conj=set()
print('Ingrese 20 números ')
for i in range(20):
  n=int(input())
  l1.append(n)  #meto todos en la l1
  conj.add(n)   #meto todos en el conj1, q no agrega el numero si ya esta
i=0            
while i<len(l1):        #releo todo lo q meti en la l1
  if l1[i] in conj:      #si los de la lista esta en el conj,
    #conj.discard(l1[i])  #los saco del conjunto. Lo saco
    i+=1                #una vez xq solo pueden repetirse 1 vez
  else:  
    l1.pop(i)   #si no esta en el conjunto, es xq ya lo saque,  
print(l1)      #entonces esta repetido y lo saco de la l1
''' 
#ej 5.6
'''Cargar 20 elementos positivos. Ingresar un número por teclado y buscarlo en la lista. Si existe de
forma repetida eliminar todas las repeticiones, dejando sólo la primera aparición en la estructura.'''

'''
l1 = []  
for i in range(20):
    num=int(input('Ingrese número positivo  '))
    while num<=0:
        num=int(input('Ingrese número positivo  '))
    l1.append(num)
buscar=-1   #xa entrar al ciclo
while buscar<=0:
    buscar=int(input('Ingrese número a buscar  '))
if l1.count(buscar)>1:  #si aparece mas de una vez el numero
    pos=l1.index(buscar) #lista.index(valor) devuelve la posición de la primera aparición de valor en
    l1[pos]=0  # a la primera posicion del numero busco le asigno el valor cero   #la lista
    while l1.count(buscar)>0:
        l1.remove(buscar)
    l1[pos]=buscar #restauro el valor de la posicion al de antes
print('Lista resultante')
print(l1)
'''
#conclusion: le asigno el valor cero solamente para guardar la poscion. podria ser cualquier numero 
#distinto de buscar (negativo por ejemplo)
'''Elaborar un programa que permita cargar dos listas booleanasde 15elementos(los elementos sólo 
pueden  ser True  y False).  Luego  se  presenta  el  siguiente  menú deopciones: CONJUNCIÓN, 
DISYUNCIÓN,  SALIR.  A  continuación  se  efectuará  la  operación  entre  ambas listas,  
posición  a posición. Es decir, CONJUNCIÓN o DISYUNCIÓN  entre los elementos de la posición
 0 de ambas listas;  y  el  resultado  debe  ir  a  una  nueva  lista  en  la  posición  0.  
 Proceder  igual  con  todos  los elementos de las listas.Mostrar la lista booleana resultante.
ComputaciónUBA2'''
#Ej 5.7
'''
lis1=[]
lis2=[]
print('Ingrese los 15 elementos de la Primer lista (0 False, resto True )')
for i in range(15):
  verd=int(input('%d  '%(i+1)))
  lis1.append(bool(verd))
print('Ingrese los 15 elementos de la Segunda lista (0 False, resto True )')
for i in range(15):
  verd=int(input('%d  '%(i+1)))
  lis2.append(bool(verd))
print('Seleccione\n1-Conjunción\n2-Disyunción\nOtro-Salir')
opc=int(input())
while opc in(1,2):
  lis3=[]
  if opc==1:
    for i in range(len(lis1)):
      lis3.append(lis1[i]and lis2[i])
  else:
    for i in range(len(lis1)):
      lis3.append(lis1[i]or lis2[i])
  print('Primer Lista ',lis1,sep='\n')  
  print('Segunda Lista ',lis2,sep='\n')  
  print('Lista Resultante',lis3,sep='\n')  
  print('Seleccione\n1-Conjunción\n2-Disyunción\nOtro-Salir')
  opc=int(input())
'''

#Ej 5.8
'''Ejercicio 5.8Confeccionar un programa que permita cargarnúmeros enteros en una lista de 10 
elementos.Luego mostrar la lista en orden de ingreso invertido (el último eningresar ocupa el 
primer lugar). Ejemplo:Ingrese los10 elementos: 1-112-53--64-05-16-127-118-49-910-3Orden 
Invertido394111210-6511
'''
'''
lista=[]
for i in range(10):
  lista.append(int(input('Ingrese elemento %d -  '%(i+1))))
lista.reverse()
print('Orden Invertido')
for elem in lista:
  print(elem,end=' ')
'''
#Ejercicio de Autoevaluación 1
'''Cargar 2 listas de 10 elementos cada una con números positivos. Mostrar un menú de opciones:
1- Unión, 2- Intersección. Obtener la operación seleccionada en cada caso por el usuario,
considerando que no debe haber elementos repetidos en un conjunto.'''
'''
l1=[]
l2=[]
l3=[]
print('Ingrese los 10 elementos de la primer lista')
for i in range(10):
  num=0			#xa entrar al ciclo
  while num<=0:
    num=int(input('%d-'%(i+1)))	#ingreso el numero
    if l1.count(num)>0:	#si contas el numero de una vez
      num=0		#restaurame el valor de num a 0 entonces entro al ciclo de nuevo
  l1.append(num)      #si no es negativo agrega el nunero
print('Lista ingresada')
print(l1)
print('Ingrese los 10 elementos de la segunda lista')
for i in range(10):
  num=0
  while num<=0:
    num=int(input('%d-'%(i+1)))
    if l2.count(num)>0:
      num=0
  l2.append(num)
print('Lista ingresada')
print(l2)
opc=1
while opc in[1,2]:
  l3.clear()
  print()
  print('MENU DE OPCIONES')
  print('1- Unión','2- Intersección', 'Otro- Salir',sep='\n')
  opc=int(input())
  if opc==1:
    l3=l1	#copio la l1 en la l3
    for i in range(len(l2)): #xa cada elementos de la lista 2
      if l3.count(l2[i])==0: #si l0 cuento 0 veces en la l3 ese elemento, 
        l3.append(l2[i])     #lo meto en la l3 (1 o mas no xq esta repe)
    print('Lista Unión')
    print(l3)
  elif opc==2:
    for i in range(len(l1)):
      if l2.count(l1[i])==1: #si en la l2 cuenyo un elemento de la l1
        l3.append(l1[i])  #lo meto en la l3 xq esta en los 2
    print('Lista Intersección')
    print(l3)
'''
#Opción b
#Ej Autoevaluación 1 Práctico 5
'''
c1=set()
c2=set()
l3=[]
print('Ingrese los 10 elementos de la primer lista')
for i in range(10):
  num=0
  while num<=0:
    num=int(input('%d-'%(i+1)))
  c1.add(num)
print('Lista ingresada')
l1=list(c1)
print(l1)
print('Ingrese los 10 elementos de la segunda lista')
for i in range(10):
  num=0
  while num<=0:
    num=int(input('%d-'%(i+1)))
  c2.add(num)
print('Lista ingresada')
l2=list(c2)
print(l2)
opc=1
while opc in[1,2]:
  l3.clear()	# xa q puedas volver a elegir la otra opcion
  print()
  print('MENU DE OPCIONES')
  print('1- Unión','2- Intersección', 'Otro- Salir',sep='\n')
  opc=int(input())
  if opc==1:
    c3=c1.union(c2)	#puedo unir conjuntos pero no listas
    l3=list(c3)
    print('Lista Unión')
    print(l3)
  elif opc==2:
    c3=c1.intersection(c2)
    l3=list(c3)
    print('Lista Intersección')
    print(l3)
  c3.clear()
'''
'''
opc=1
while opc in [1,2])
  L3.clear()
  print('1- Unión','2- Intersección', 'Otro- Salir',sep='\n')
  opc=int(input())
  if opc==1:
'''
#Ejercicio de Autoevaluación 2
'''Cargar 10 números naturales y mostrar para cada uno de ellos su reverso'''
'''
l=[]
print('Ingrese 10 números naturales')
for i in range(10):
  num=0
  while num<=0:
    num1=input('%d-'%(i+1))
    while not num1.isnumeric():
      num1=input('%d-'%(i+1))
    num=int(num1)
    if num>0:
      l=list(num1) #lista con elementos de num1 en este caso, los subnumeros que lo componen
      l.reverse()  #doy vuelta lista con elementos (doy vuelta el numero)
      print(num,' reverso:', int(''.join(l))) #desarma la lista y la hace un solo numero
'''
#           parte 2
'''
txt='1  2  &  3'
lista=txt.split(' ')
print(lista)
'''
'''
nom='juansitoooooiii'
lista=list.append((nom.lower()+('*'*10))[:10])
print(lista)
'''
#PROGRAMA XA INGRESAR NOTAS, PADRONES Y APELLIDOS DE ALUMNOS
# SOLO LISTAS
'''
apellidos=[]
nombres=[]
legajos=[]
par1=[]
par2=[]
recup=[]
apel=input('Ingresá apellido alumno, * para salir ')
while apel!='*':
  nom=input('Ingresá nombre de %s '%apel)
  leg=input('Ingresá legajo de %s '%(nom+' '+apel))
  n1=float(input('Nota Parcial 1 (0 si no rindió)'))
  n2=float(input('Nota Parcial 2 (0 si no rindió)'))
  n3=float(input('Nota Recuperatorio (0 si no rindió)'))
  apellidos.append(apel)
  nombres.append(nom)
  legajos.append(leg)
  par1.append(n1)
  par2.append(n2)
  recup.append(n3)
  apel=input('Ingresá apellido alumno, * para salir ')
print('Listado Alumnos del Curso')
for i in range(len(apellidos)):
  print(legajos[i][:8].rjust(10),apellidos[i][:10].ljust(12), 
  nombres[i][:10].ljust(12),end='')
  if par1[i]==0:
    print('s/n'.rjust(6),end='')
  else:
    print(str(par1[i]).rjust(6),end='')
  if par2[i]==0:
    print('s/n'.rjust(6),end='')
  else:
    print(str(par2[i]).rjust(6),end='')
  if recup[i]==0:
    print('s/n'.rjust(6))
  else:
    print(str(recup[i]).rjust(6))
exit()
'''
'''
curso=[]
apel=input('Ingresá apellido alumno, * para salir ')
while apel!='*':
  nom=input('Ingresá nombre de %s '%apel)
  leg=input('Ingresá legajo de %s '%(nom+' '+apel)) 
  n1=float(input('Nota Parcial 1 (0 si no rindió)')) 
  n2=float(input('Nota Parcial 2 (0 si no rindió)')) 
  n3=float(input('Nota Recuperatorio (0 si no rindió)')) 
  curso.append((apel,nom,leg,n1,n2,n3))
  apel=input('Ingresá apellido alumno, * para salir ')
  print('Listado Alumnos del Curso')
for i in range(len(curso)):   #recorro las "filas" de mi tabla
  print(curso[i][2][:8].rjust(10),curso[i][0][:10].ljust(12), #cada curso[i]
  curso[i][1][:10].ljust(12),end='')    #es un elemento de la fila (cada uno en una col !=)
  #print(curso) imprimiria cada tupla (datos de un alumno), que representa una fila 
  if curso[i][3]==0:            #de la table
    print('s/n'.rjust(6),end='')
  else:
    print(str(curso[i][3]).rjust(6),end='')
  if curso[i][4]==0:
    print('s/n'.rjust(6),end='')
  else:
    print(str(curso[i][4]).rjust(6),end='')
  if curso[i][5]==0:
    print('s/n'.rjust(6))
  else:
    print(str(curso[i][5]).rjust(6))
'''

#ej 5.9
'''Cargar datos de amigos en listas. Armar una lista con los Nombres, otra con
los Apellidos, otra con el contacto de whatsapp. Mantener la consistencia 
(cada fila tiene los datos de la misma persona). Mostrar la agenda resultante
y verificar si hay algún teléfono de afuera de argentina (código país argentina 
54).'''
'''
nombres=[]
apellidos=[]
celus=[]
nom=input('Ingresá nombre de un amigo, * para terminar  ')
while nom!='*'and not nom.isalpha():
  nom=input('Ingresá nombre de un amigo, * para terminar  ')
while nom!='*':
  apel=input('Ingresá apellido de %s  '%nom)
  while not apel.isalpha():
    apel=input('Ingresá apellido de %s  '%nom)
  cel=input('Ingresá celu de %s, ej +54 9 11 98785458  ')
  #meto los datos en las listas (columnas)
  nombres.append(nom.capitalize())
  apellidos.append(apel.capitalize())
  celus.append(cel)

  nom=input('Ingresá nombre de un amigo, * para terminar  ')
  while nom!='*'and not nom.isalpha():
    nom=input('Ingresá nombre de un amigo, * para terminar  ')
print('Agenda de Contactos')
for i in range(len(nombres)): #para la longitud de la lista de la col nombres
  print(nombres[i][:10].ljust(15),end='') #voy imprimiendo cada fila 'i'
  print(apellidos[i][:10].ljust(15),celus[i].ljust(15),end='')  #de cada col
  if celus[i][:3]!='+54':                         #(nombres apellidos  celus)
    print(' del Extranjero')       
  else:                      #listas:| [nombres] | [apellidos] | [celus] |                        #i    0           0         0
    print()                  #   i   |    1      |    1        |   1     |
'''
#ej 5.10
'''Resolver el ejercicio 9 usando una única lista. Se sugiere que cada 
elemento sea una tupla que contenga Nombre, apellido y Contacto.'''
'''agenda=[]
nom=input('Ingresá nombre de un amigo, * para terminar  ')
while nom!='*'and not nom.isalpha():
  nom=input('Ingresá nombre de un amigo, * para terminar  ')
while nom!='*':
  apel=input('Ingresá apellido de %s  '%nom)
  while not apel.isalpha():
    apel=input('Ingresá apellido de %s '%nom)
  cel=input('Ingresá celu de %s, ej +54 9 11 98785458 '%nom)
  #agrego datos a lista
  agenda.append((nom.capitalize(),apel.capitalize(),cel)) #agrego los 3 datos como una tupla
  nom=input('Ingresá nombre de un amigo, * para terminar  ')
  while nom!='*'and not nom.isalpha():
    nom=input('Ingresá nombre de un amigo, * para terminar  ')
print('Agenda de Contactos')
for contacto in agenda: #cada contacto es una tupla con 3 elementos
  print(contacto[0][:10].ljust(15), end='')
  print(contacto[1][:10].ljust(15), contacto[2].rjust(16), end='')
  if contacto[2][:3]!='+54':
    print(' del extrangero')
  else:
    print()
'''
#ej 5.10
'''Ofrecer un menú para seleccionar la unidad de medida. Mostrar la lista 
final de ingredientes de manera tabulada
Ejemplo:Bife de Chorizo   3   unid
        Sal              0.5  cuchditas
        Aceite           1    cuch'''
'''
ingre=[]
medida=('gr','ml','cm3','unid','taza','cuch','cuchdita')
desc=input('Ingrese ingrediente, * para salir  ') #1º ingresa ingriente
while desc!='*':                                    #col 1
  print('Seleccioná Unidad')          #2do ingresa amedida (col 2)
  for i in range(len(medida)):  #recorro las medidas
    print(i+1,' - ',medida[i])  #1-gr   2-ml    3-cm3
  unid=int(input())
  while unid not in range(1,8):
    unid=int(input())
  cant=float(input('Ingresá cantidad de %s  '%medida[unid-1])) #3º ingresa cantidad
  while cant<=0:
    cant=float(input('Ingresá cantidad de %s  '%unid))
  ingre.append( (desc.capitalize(),medida[unid-1],cant) ) #meto los datos de cada
  desc=input('Ingrese ingrediente, * para salir  ') #ingrediente juntos en una tupla
print('\nIngrediemtes') #each new ingredient is a new tuple con su cant y medida
for ing in ingre:
  print(ing[0].ljust(20),str(ing[2]).rjust(8),ing[1].rjust(10))
                            #numero (cantidad)
'''
#ej 5.12
'''Ingresar Nombre y Apellido de personas (el final vendrá dado por *). Cargar
una lista con los datos, de modo que figure el apellido de cada persona (en 
minúsculas e inicial en mayúscula), seguido por una coma y la inicial de su 
nombre en Mayúscula ( Pérez,E ). Mostrar la lista resultante.'''
'''
(#no responde consigna)
txt=input('Ingrese un texto  ')
txt=txt.strip()
lisTxt=txt.split('.') #lospuntos marcan los elementos de la lista
print(lisTxt)
for i in range(len(lisTxt)):
  lisTxt[i]=lisTxt[i].strip() #cada elemento dsps del punto le saco los espacios antes y dsps del string
  lisTxt[i]=lisTxt[i].capitalize()  #le meto mayuscula a cada elemento de la lista
txt='.'.join(lisTxt)#uno todo junto
print('Texto editado')
print(txt)
'''
'''
nom=input('Ingresá nombre:  ')
lista=[]
while nom!='*':
  apel=input('Apellido de %s ?  '%nom)
  lista.append(apel.capitalize()+','+nom[0].upper()) #mayusculizame la primera letra 
  nom=input('Ingresá nombre:  ') #del apellido y unilo con una coma al nombre recortado 
for nombre in lista:            #a la primer letra
  print(nombre)
'''
#resuemen de cosaa clave: combinar listas con tuplas xa hacer tablas. guardo en 
#cada elemento de la lista una tupla y dsps la imprimo como quiero
'''
list=[]
nombre=input('nombre: ')
apel=input('apellido: ')
edad=input('edad: ')
list.append((nombre,apel,edad))
print(nombre.ljust(10),apel.ljust(10), edad.ljust(10))
'''
#              parte 3
#listas de listas (matrices y tablas)
'''
ventas=[]
meses='enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre',
'octubre','noviembre','diciembre'
for i in range(5):    #1 , 2 , 3, 4, 5
  ventas.append([])
  for mes in meses:
    cant=float(input('Ingrese cantidad vendida en sucursal %d en el mes de %s '%(i+1,mes)))
    ventas[i].append(cant)       # 1-enero , 1-feb 1-marz...
  print()                        # 2-enero, 2-feb, 3-marz...
print('Ventas Anuales 2019 de la Compañía')
print('Suc',end=' ')
for mes in meses:
  print(mes.center(13),end='')
print()
for i in range(len(ventas)):
  print(str(i+1).ljust(4),end='')
  for j in range(len(ventas[i])):
    print(str(ventas[i][j]).rjust(13),end='')
print()
'''
#Perecaución al hacer tablas!!
#MAL hecha
'''
fila=[0]*12
ventas=[fila]*5
print(fila)
print(ventas)
#modifico la lista fila ==> se modifica la la lista ventas 
fila[3]=1 #o si no
#ventas[0][3]=1   #modfican el ele[3] de fila
print(ventas)     #cada lista de ventas tiene un 1 en ele[3]
for elemento in ventas:
  print(elemento[3])    #imprime el elemento 3 de c/array, es decir 5 1's
#QUITA DOBLE ESPACIOS PARA COPIAR CONSIGNAS DE PDF DE VSC
'''
#MAL hecha (lo mismo de recién pero simplificado)
'''
fila=[  [0]*12   ]*5  #fila es una lista de 5 litsas de 12 0's
    #[fila=[0]*12]
print(fila)
fila[2][0]=2  #modifico el ele[0] de la segunda lista[2] de la lista fila
print(fila)   #como multiplico el mismo bank de memoria, mete un 2 en cada
for ele in fila:  #posición ele[0]
  print(ele[0])
'''
#CORRECTAMENTE hecha
'''
fila=[0]*12
ventas=[]
for i in range(5):
  ventas.append(fila.copy())    #(fila)
print(fila) #printo la final original
print(ventas) # y la tabla COPIADA ===> queda todo con 0's
fila[3]=1 #modifico la fila original
print(fila) #la fila orig cambia pero...  ===>ele 3 now is 1
print(ventas) #la tabla no porque ahora use fila.copy() y no lo asocie
#o sino         # con " ventas=[fila]*5 " ===>5 filas con 0's
'''
#CORRECTA también
'''
ventas=[]
for i in range(5):
  ventas.append(  [0]*12  )  #meto 5 veces la fila de 12 0's
              #(fila=[0]*12)  #una lista de 5 listas
ventas[0][1]=3 #solo modifico el ele 1 la 1er lista (de 5) de la lista de ventas
ventas[4][4]=8 #y aca la 5ta xq sí
print(ventas) #solo se modifica la fila q qiuiero, no todas las filas
'''
'''De este modo, cada fila de la tabla ventas apunta a una región distinta;
y por lo tanto, cada modificación particular de celda (fila y columna), es
eso mismo, una modificación ESTRICTAMENTE  APLICADA A LA CELDA INDIVIDUAL.'''
#mas ejemplos de tablas
#1-
'''
fila=[0]*12
ventas=[]
for i in range(5):
  ventas.append(fila)
ventas[1][10]=1 #solo modifio la lista 1(fila 1) de ventas
print(ventas)
'''
#2-
'''
ventas=[[0]*12]*5
 #fila= [0]*12
ventas[2]=[(1,3),(1,5)]
print(ventas)
'''
#Guia de ejercicios

#Ejercicio 5.13
'''Cargar una Lista de Menú con varios platos; uno por cada día de la semana.
Para cada plato se debe guardar: nombre, calificación de dificultad 
(baja,media,alta); tiempo de preparación en minutos; ingredientes.
De cada ingrediente se debe consignar: nombre o descripción, cantidad, unidad
de medida (vaso, cuch, cuchdta, unid, gr, cm3, ml). El usuario ingresará un
día de la semana  y deberá mostrarse el menú previsto para ese día. Indicar
además cuántos ingredientes lleva.'''
'''
dias='domingo','lunes','martes','miercoles','jueves','viernes','sabado'
dif=('','baja','media','alta')
medidas=('','vaso', 'cuch', 'cuchdta','unid', 'gr', 'cm3', 'ml')
menu=[]

for dia in dias:
  plato=input('Ingrese Plato del %s  '%dia)
  print('Dificultad\n1-Baja\n2-Media\n3-Alta\n')
  dific=int(input())
  while dific not in (1,2,3):
    dific=int(input())
  tpo=int(input('Tiempo aproximado preparación en minutos  '))
  print('Ingredientes, * para salir ')
  ingre=[]
  ing=input('Ingrediente:  ')
  while ing!='*':
    print('Medida')
    for i in range(1,len(medidas)):
         print(i,'-',medidas[i])
    unid=int(input())
    while unid not in range(1,8):
         unid=int(input())
    cant=float(input('Cantidad de %s  '%medidas[unid]))
    ingre.append([ing,unid,cant]) ##
    ing=input('Ingrediente:  ')
  menu.append([plato,dif[dific],tpo,ingre]) ## xa cada dia
print('Seleccione día de la semana ')
for i in range(len(dias)):
   print(i+1,'-',dias[i])
opc=int(input())
while opc not in range(1,8):
   opc=int(input())
print('Menú para el',dias[opc-1])
#print('menu',menu)
selec = menu[opc-1] #corresponde al plato del nºdia = dias[opc-1] (solo trabajo con ese dia)
#print('selec',selec)
print(selec[0]) #menu[dia][0]=plato
print('Dificultad: ',selec[1]) #menu[dia][1]=dif[dific] (dific 1 a 3 elegido por user)
print('Lleva aprox ',selec[2],'minutos')  #menu[dia][2]=tpo
for ingre in selec[3]:
      print(ingre[0][:10].ljust(12),
str(ingre[2]).rjust(6),medidas[ingre[1]].ljust(8)) #ingre.append([ing,unid,cant])
print('Lleva',len(selec[3]),'Ingredientes') #selec[3]=menu[3]=ingre
'''
#Ejercicio 5.14
'''Cargar una lista con los códigos de repuestos de una casa de reparación de lavarropas (20 en total).
Y para cada código cargar la cantidad vendida en cada venta del mes ( pueden tener diferente 
cantidad de ventas en el mes, se sugiere terminar ingreso de ventas con 0). Mostrar la lista de
códigos con las ventas totales del mes.
Ejemplo:
Llave25 1 2
cuplaX2 1
placaBis 1 1 1 11
…
Mang05 2 2
Articulos Totales Vendidos
Llave25 3
cuplaX2 1
placaBis 14
…
Mang05 4
'''
#opcion a)
'''
l1 = []
for i in range(20):
  art=input('Ingrese el articulo %d ' %(i+1))
  l1.append([]) #creo una lista 'i' vacia dentro de l1. 
  l1[i].append(art) #en la lista vacia 'i' dentro de l1, pongo el nombre del articulo en la 
  cant=1 # primera posicion. ===>l1[i][0]='art'
  while cant>0:
    cant=int(input('Ingrese cantidad vendida, 0 para salir '))
    if cant>0:
      l1[i].append(cant) #dentro de la lista 'i' en la l1, meto a partir de la posicion 1 (la 0 
print() # ta ocupada) las cantidades
print('Artículo'.center(8),' ','Total Vendido'.center(15))
for i in range(len(l1)):
  print(l1[i][0].ljust(10),end='') #impirmo el nombre del articulo 
  suma=0
  for j in range(1,len(l1[i])): #xa cada j en la longitud de la lista i q se creo xa c/ art y 
    suma+=l1[i][j] # A PARTIR DEL 1 (XQ EL 0 ES EL ART) sumo todos los ele (las cantidades)
  print(str(suma).rjust(15))  #stringeo y priteo la suma y la pongo prolija
print()
'''
#Opción b)
'''
l1 = []
for i in range(2):
  art=input('Ingrese el articulo %d ' %(i+1))
  l1.append([art,[]]) #meto en la l1 una list 'i' q tiene en la pos 0 el art y en la pos 1 una
  cant=1    # lista vacia
  while cant>0:
    cant=int(input('Ingrese cantidad vendida, 0 para salir '))
    if cant>0:
      l1[i][1].append(str(cant)) #en la posicion 1 de la lista 'i' (q era la lista vacia), q 
print()    #corresponde al art i, meto las cantidades del art 'i'
print('Artículo'.center(8),' ','Total Vendido'.center(15))
for i in range(len(l1)):
  print(l1[i][0].ljust(10),end='')  #printeo el art
  suma='+'.join(l1[i][1]) #la var suma es una cadena con todos los eles (cantidades) de la lista 
  print(str(eval( suma )).rjust(15))  #q esta enla pos 1 de la lista 'i' de la l1, separadas por un +
print()    #eval(cadena) intenta evaluar cadena como una expresión aritmética
''' 
#Ej Batalla naval (5.15 y 5.16)
'''Ejercicio 5.15
Confeccionar un programa que permita cargar aleatoriamente un tablero para el Juego de la Batalla Naval.
Debe considerarse un tablero de 10x10 y se ubicará, en cualquiera de los cuatro sentidos
(< > ^ v), la siguiente flota:
Tamaño Cantidad
  5       1 = 5
  4       2 = 8
  3       3 = 9 ===> 35 spaces
  2       4 = 8 ===> 15 barcos
  1       5 = 5
Ejercicio 5.16
Completar el programa del ejercicio anterior para permitir que un usuario juegue la Batalla Naval 
contra la máquina. Dispondrá de 60 tiros y por cada uno el programa debe contestar: AGUA o TOCADO.
Si el usuario hunde la flota completa hasta el tiro 60 inclusive, habrá ganado la partida.
'''
#                                      tablero
#Opción a: Llenado en 4 sentidos

#prueba de loop nesteados
'''
l1=[]
sum=0 
for i in range(6):   #0 de 0, 0 de 1, 1 de 2, 2 de 3, 3 de 4
  sum+=i
  for j in range(i):
    l1.append('a')
print(len(l1))
print(sum)
'''
'''
import random
orientacion=(0,1,2,3)
l1 = []   #creo el tablero
for i in range(10):
  l1.append([]) #creo 10 listas vacias dentro de l1 ('10 filas')
for i in range(10):
  l1[i]=[' ']*10  #xa cada columna creo 10 columnas
#hasta aca, cree la tabla
print()
for i in range(10):     #imprimo
  print(l1[i])          #el tablero
print()
sentido=0
fila=0
colum=0
for i in range(1,6): #longitud de cada barco
  for j in range (i): # 15 opc, 15 barcos (factorial sumado ver loop de arriba)
    ban=1     #xa entrar al loop
    while ban!=0:  ### cada vez q tengo q colocar una part del barco, pido q ban!=0
      sentido=random.choice(orientacion) #numero random de la tupla orientacion (1 a 5)
      fila=random.randint(0,9) #(idem xa fila)
      colum=random.randint(0,9) #         col
      ban=0 ###reseteo ban xa no entrar si o si al loop
      #print('sentido',sentido)
      #print('fila',fila)
      #print('col',colum)
      if sentido==0: #abajo
        if fila+5-i>9:  #si pasa esto, se va del tablero =>
          ban=1 #vuelve a entrar al loop de ###
        else:
          for l in range(fila,fila+6-i):  #si entre la fila random y la fila + 6 - i (maximo 5)
            if l1[l][colum]!=' ': #si la columna 'colum' de cada columna l de l1 esta vacia
              ban=1
      if sentido==1: #arriba
        if fila<6-i:
            ban=1 #vuelve a entrar al loop de ###
        else:
          for l in range(fila,fila-6+i,-1): #de la fila hasta la fil-6 yendo de a -1 filas
            if l1[l][colum]!=' ': #si esta vacia toda la columna
              ban=1 #vuelve a entrar al loop de ###
      elif sentido==2: #derecha
        if colum+5-i>9:
          ban=1 #vuelve a entrar al loop de ###
        else:
          for l in range(colum,colum+6-i):
            if l1[fila][l]!=' ': #si NO esta vacio desde colum hasta colum+6-1 (i=1, 5 space
              ban=1 #vuelve a entrar al loop de ###         # i=2, 4 space  i=3, 3 space 
      else: #izquierda                                      # i=4, 2 space, i=5, 1 space )                  
        if colum<6-i: 
          ban=1 #vuelve a entrar al loop de ###
        else:
          for l in range(colum,colum-6+i,-1):
            if l1[fila][l]!=' ':
              ban=1 #vuelve a entrar al loop de ###
    if sentido==0:  #hacia abajo     #(0,0+5)
      for k in range(fila,fila+6-i):  #(i=1 k=5  ,# i=2 k=4  ,# i=3 k=3  ,#i=4 k=2  ,# i=5 k=1)
        l1[k][colum]=str(6-i)  #fila k, llenala k veces (6-i) con 'k's' (para colum cte (vertical=>no varia))
    elif sentido==1: #hacia arriba  
      for k in range(fila,fila-6+i,-1): # paso: - 1 xa ascender
        l1[k][colum]=str(6-i) #k variable, xq es vertical, colum cte
    elif sentido==2: # hacia la derecha
      for k in range(colum,colum+6-i): #sin paso
        l1[fila][k]=str(6-i) #fila cte x ser horizontal, varia colum 'k'
    else: #hacia a izquierda
      for k in range(colum,colum-6+i,-1): #paso de -1 para ir "hacia atrás"
        l1[fila][k]=str(6-i) #fila cte, colum 'k' variable por ser horizontal (sentido==4)

#contador de espacios vacios

#blank=0
#for i in range(10):
#  print(l1[i])
#  blank+=l1[i].count(' ')
#print('ocup:',100-blank)
'''
#                                   tablero
#Opción b: Llenado en 2 sentidos
'''
import random
orientacion=(0,1)
l1 = []
for i in range(10):
  l1.append([]) #meto 10 filas en l1
for i in range(10):
  l1[i]=[' ']*10 #cada fila es una columna de 10 espacios NO una lista

#ojo no sirve
#l1=[]
#for i in range(10):
#  l1.append([])
#for i in range(10):
#  l1[i].append(['']*10) #cada fila es una lista de 10 espacios

print()
for i in range(10):
  print(l1[i])
print()
sentido=0
fila=0
colum=0
for i in range(1,6):
  for j in range (i):   #15 barcos
    ban=1
    while ban!=0:
      sentido=random.choice(orientacion)
      fila=random.randint(0,9)
      colum=random.randint(0,9)
      ban=0
      if sentido==0: #abajo
        if fila+5-i>9:
          ban=1
        else:
          for l in range(fila,fila+6-i):
            if l1[l][colum]!=' ': #fila 'l' varibale x ser vertial colum fija
              ban=1
      else: #derecha
        if colum+5-i>9:
          ban=1
        else:
          for l in range(colum,colum+6-i):
            if l1[fila][l]!=' ': #si NO tiene tantos espacios en blanco como los q necesito,
              ban=1      #  la fila fija x ser horizontal, colum 'l' variable
    if sentido==0: #hacia abajo
      for k in range(fila,fila+6-i): #k=6-i
        l1[k][colum]=str(6-i) #la fila k, variable y colum cte llenala con k's
    else: #sentido==1 hacia la derecha
      for k in range(colum,colum+6-i):
        l1[fila][k]=str(6-i) #fila cte x ser horizontal, colum variable segund k= 6-i
for i in range(10):
  print(l1[i])
print()
'''
#         juego completo
#Opción a): Lleva control del juego por el Tablero
'''
import random
orientacion=(0,1,2,3)
l1 = []
for i in range(10):
  l1.append([])
for i in range(10):
  l1[i]=[' ']*10
print()
sentido=0
fila=0
colum=0
for i in range(1,6):
  for j in range (i):
    ban=1
    while ban!=0:
      sentido=random.choice(orientacion)
      fila=random.randint(0,9)
      colum=random.randint(0,9)
      ban=0
      if sentido==0:
        if fila+5-i>9:
          ban=1
        else:
          for l in range(fila,fila+6-i):
            if l1[l][colum]!=' ':
              ban=1
      if sentido==1:
        if fila<6-i:
          ban=1
        else:
          for l in range(fila,fila-6+i,-1):
            if l1[l][colum]!=' ':
              ban=1
      elif sentido==2:
        if colum+5-i>9:
          ban=1
        else:
          for l in range(colum,colum+6-i):
            if l1[fila][l]!=' ':
              ban=1
      else:#sentido==3
        if colum<6-i:
          ban=1
        else:
          for l in range(colum,colum-6+i,-1):
            if l1[fila][l]!=' ':
              ban=1
    if sentido==0:
      for k in range(fila,fila+6-i):
          l1[k][colum]='*'
    elif sentido==1:
      for k in range(fila,fila-6+i,-1):
          l1[k][colum]='*'
    elif sentido==2:
      for k in range(colum,colum+6-i):
          l1[fila][k]='*'
    else:
      for k in range(colum,colum-6+i,-1):
          l1[fila][k]='*'
cont=0
hayFlota=True
while (cont<60)and hayFlota:
  fila=0 #xa entrar al loop
  while (fila<1)or(fila>10): #sale del tablero
    fila=int(input('Ingrese fila: '))
  columna=0  
  while (columna<1)or(columna>10): #xa entrar al loop
    columna=int(input('Ingrese columna: '))
  if l1[fila-1][columna-1]=='*': #el -1 es xq l1 arranca en 0
    print('TOCADO')
    l1[fila-1][columna-1]=' '
  else:
    print('AGUA')
  quedan=0
  for i in range(10):
    quedan+=l1[i].count('*')
  hayFlota=bool(quedan)
  cont+=1
  print('te quedan bajar:',quedan)
  print('bombas restantes:',60-cont)
if hayFlota:
  print('PERDISTE EL JUEGO!!!')
else:
  print('GANASTE EL JUEGO!!!')
'''
#Opción b: Control del juego con Connjunto de Casilleros Marcados
'''
import random
orientacion=(0,1,2,3)
l1 = []
for i in range(10):
  l1.append([])
for i in range(10):
  l1[i]=[' ']*10
sentido=0
fila=0
colum=0
for i in range(1,6):
  for j in range (i):
    ban=1
    while ban!=0:
      sentido=random.choice(orientacion)
      fila=random.randint(0,9)
      colum=random.randint(0,9)
      ban=0
      if sentido==0:
        if fila+5-i>9:
          ban=1
        else:
          for l in range(fila,fila+6-i):
            if l1[l][colum]!=' ':
              ban=1
      if sentido==1:
        if fila<6-i:
          ban=1
        else:
          for l in range(fila,fila-6+i,-1):
            if l1[l][colum]!=' ':
              ban=1
      elif sentido==2:
        if colum+5-i>9:
          ban=1
        else:
          for l in range(colum,colum+6-i):
            if l1[fila][l]!=' ':
              ban=1
      else:
        if colum<6-i:
          ban=1
        else:
          for l in range(colum,colum-6+i,-1):
            if l1[fila][l]!=' ':
              ban=1
    if sentido==0:
      for k in range(fila,fila+6-i):
          l1[k][colum]='*'
    elif sentido==1:
      for k in range(fila,fila-6+i,-1):
          l1[k][colum]='*'
    elif sentido==2:
      for k in range(colum,colum+6-i):
          l1[fila][k]='*'
    else:
      for k in range(colum,colum-6+i,-1):
          l1[fila][k]='*'
cont=0
tiros=set()
tiros4user=set()
while (cont<60)and len(tiros)<35:
  fila=0
  while (fila<1)or(fila>10):
    fila=int(input('Ingrese fila: '))
  columna=0  
  while (columna<1)or(columna>10):
    columna=int(input('Ingrese columna: '))
  if l1[fila-1][columna-1]=='*':
    print('TOCADO')
    tiros.add((fila-1,columna-1))
    tiros4user.add((fila,columna))
  else:
    print('AGUA')
  cont+=1
  print('tiraste:',tiros4user) 
  print('te quedan bajar:',35-len(tiros))
  print('bombas restantes:',60-cont)
if len(tiros)<35:
  print('PERDISTE EL JUEGO!!!')
else:
  print('GANASTE EL JUEGO!!!')
'''