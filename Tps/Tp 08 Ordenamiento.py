                        #PRÁCTICA VIII ORDENAMIENTO 
#INTRO Y TEORIA
#Ordenamiento tipo: "Uno contra todos"
'''compara elemento x elemento, uno, contra todos, pasa al siguiente, lo compara con todos etc'''
'''
def intercambio(i,j,l): #ej:
    aux=l[i]        #aux=3  [3,0]
    l[i]=l[j]     # 3--->0  [0,0] aux= [3]
    l[j]=aux      # 0--->3  [0,aux] = [0,3]
l=[1,10,0,-5,2]
print(l)
for i in range(len(l)-1): #xa cada numero
    for j in range(i+1,len(l)): #comparo con el resto de los numeros
        if l[i]>l[j]: #si el primero es mayor
            intercambio(i,j,l) #aplico intercambio
print(l)
'''
#Ordenamiento tipo Bubble sort
'''Tiene varias pasadas y en cada una se va empujando un elemento de izquierda a 
derecha buscando su posición. En cada pasada, a diferencia de Uno Contra Todos que 
busca dejar el menor al principio, deja el mayor al final.'''
'''
def intercambio(i,j,l):
    aux=l[i]
    l[i]=l[j]
    l[j]=aux
l=[1,10,0,-5,2]
print(l)
for i in range(1,len(l)):
    for j in range(len(l)-i):
        if l[j]>l[j+1]:
            intercambio(j,j+1,l)
print(l)
'''
#Ordenamiento con funcion sorted() o metodo .sort (solo Python y otros pocos)
'''El método .sort() modifica la lista sobre la que se aplica el ordenamiento y no 
devuelve nada (NONE), mientras que sorted() no toca la Estructura y devuelve una versión 
ordenada (por eso si se puede aplicar a secuencias inmutables).'''
#l.ssot()
'''
def ordena(l): 
    l.sort() #ordena la lista (modifica lista, ya ordenandola)
lista1=[10,2,-3.5,0] 
ordena(lista1) 
print('Lista1:') 
print(lista1)
'''
#sorted(l)
'''
def ordena(l): 
    lista2=sorted(l) #necesito guardar el resultado de la funcion sorted en una var (lista2)
    return lista2           #sino, la pierdo    
lista1=[10,2,-3.5,0] 
lista1=ordena(lista1) 
print('Lista1:') 
print(lista1)
'''
#Corolario Fundamental del Teorema de Ordenamiento de Secuencias de la Profesora Arriazu:
'''Todos los elementos de la secuencia a comparar deben ser comparables; es decir, deben 
tener tipos compatibles para comparación (enteros con enteros o float, string con string 
o char, etc.)
Cuando la comparación se hace entre dos Estructuras de Datos se compara elemento a elemento
de izquierda a derecha hasta desempatar, que alguna finalice, o determinar que son iguales.
Por ejemplo:
lis=[1,’camila’,True,2] no es ordenable'''

'''Tanto sort() como sorted() disponen de un argumento opcional: reverse, que por defecto 
está seteado en False. Si deseamos ordenar una lista o secuencia en forma descendente 
bastará con prender en True este parámetro.'''
'''
l=[10,22,-3.5,0] 
print('lista inicial:')
print(l) 
print('lista ordenada descendente:') 
l=sorted(l,reverse=True)
print(l)
'''

#ejemplo de ordenamiento de nombres con sublistas de trabajo
'''
lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía'] 
listaOrdenada=[] 
print('Lista Inicial') 
for n in lista: 
    print (n) 
for n in range(len(lista)): 
    listaOrdenada.append([lista[n].lower(),n]) 
print() 
print('Lista de Trabajo')
for n in listaOrdenada: 
    print (n) 
listaOrdenada.sort() 
print()
print('Lista de Trabajo Ordenada') 
for n in listaOrdenada: 
    print (n) 
print()
print('Lista Original Ordenada') 
for n in listaOrdenada: 
    print (lista[n[1]])
'''
#.sort() o sorted() con parametro key = funcion o key=clase.metodo 

'''usar el parámetro key del método sort() (o la función sorted()) que permite indicar 
una función a aplicarse como clave de ordenamiento, sin que se modifiquen los datos.
ej: ''' 
'''
lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía']
print('Lista Inicial')
for n in lista: 
    print (n) 
lista.sort(key=str.lower) #ordena segun la primer letra minuscula
print()         #OJO: uso str.lower xq es un metodo de la clase string (ver aclar abajo)
print('Lista Ordenada') 
for n in lista: print (n)
'''
#Nota: Como lower() no es una función, sino un método, para usarlo debimos referenciarlo 
# como tal key=str.
'''Lower En ese caso se consigna el nombre de la Clase a la que corresponde el método (str). 
Si quisiéramos ordenar la misma lista de nombres pero''' 
#por longitud de nombres podríamos usar la función len() en el parámetro key. Mirá:\
'''
lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía']
print('Lista Inicial')
for n in lista:
    print (n)
lista.sort(key=len) #parametro = len xq ordeni segun la longitud
print() #OJO: Aca len es una funcion entonces no tengo q invocar a la clase
print('Lista Ordenada')
for n in lista: 
    print (n)
'''
#Qué pasa si no disponemos de una función predefinida o método de clase que sirva para 
# el criterio de ordenamiento que se desea establecer?
'''
def cantVoc(pal): 
    pal=pal.lower()
    cant=0 
    for v in ('a','e','i','o','u','á','é','í','ó','ú'): 
        cant+=pal.count(v) 
    return cant
lista=['Juan','ana','sergio','ELEna','ELEONORA','anALía']
print('Lista Inicial')
for n in lista:
    print (n)
    lista.sort(reverse=True,key=cantVoc)
print()
print('Lista Ordenada')
for n in lista:
    print (n)
'''
#otro ejemplo variando la columna "key" principal (2 en este caso)
'''
def reorganizaFila(fil,posicion): 
    fil.insert(0,fil[posicion]) 
    fil.pop(posicion+1)
lista1=[['Calvo','ana',25,'La Plata 233','25638944'],
['Calvo','ana',18,'Saavedra 122','24568779'],['Brunetti','analía',21,'San luis 15','23554010'],
['Tineo','LUIS',33,'Mendoza 1002','45896233'],['Santa Cruz','eliseo',29,'Garay 5021','43015668']] 
print()
print('Tabla Ingresada')
for n in lista1: 
    print (n) 
print() 
for fila in lista1: 
    reorganizaFila(fila,2) 
print('Tabla Reorganizada')
for n in lista1: print (n) 
print()
lista1.sort() 
print('Tabla Ordenada por Apellido, Nombre, Edad, Dirección, Teléfono')
for n in lista1: 
    print (n)
'''
#ordenamiento definiendo funcion "clave" con columnas a ordenar
'''
def clave(l): 
    return (l[2],l[1].lower(),l[0].upper())  #primero segun edad, 2do nombre, apellido
lista1=[['CALVO','ana',25,'La Plata 233','25638944'],['Calvo','ana',18,'Saavedra 122','24568779'],
['Brunetti','Analía',21,'San luis 15','23554010'],['Tineo','ELISEO',33,'Mendoza 1002','45896233'],
['Santa Cruz','LUIS',25,'Garay 5021','43015668']]
print() 
print('Tabla Ingresada')
for n in lista1: 
    print (n)
print()
lista1.sort(key=clave) #ver q que recibe un UNICO elemento del TIPO que se compara
print('Tabla Ordenada sólo por Nombre, Apellido y Edad, sin diferenciar mayúsculas y minúsculas')
for n in lista1: 
    print (n)
'''
#Nota: 1-
'''Fijate cómo invocamos a clave. Sólo va su nombre en el parámetro key, sin paréntesis, 
ni parámetros. sort() y sorted() automáticamente la invocarán por cada elemento que deseen
comparar. Por eso clave tiene que tener definido un parámetro de entrada del tipo del 
elemento de la lista a ordenar, en este caso, una lista.'''
#2-
'''Si usamos una función que devuelve algunas columnas de tu tabla como criterio, sort()
(o sorted()) emplearán estrictamente dichas columnas para el orden. Si hay empate con 
ellas, es empate.'''
#ordenamiento con columnas calculadas
'''
def prome(l): 
    aux=eval('+'.join(l[1:len(l)]))/4 #eval hace la oper entre parentesis evaluandola c/
#este string (ele1+ele2+ele3+ele4)/4
    return aux #devuelvo el valor del promedio, como lo toma key=prome, ordeno segun ese valor
lista=[['Juan','10','9.5','7','6'],['Camila','5','7.5','9','9'],
['Luciana','10','8','10','10'],['Tomás','8','2','5','2']] 
print('Lista Original')
for n in range(len(lista)):
    print (lista[n]) 
lista.sort(key=prome,reverse=True)
print()
print('Lista Ordenada por Promedio')
for n in range(len(lista)):
    print (lista[n])
#ver que la fcion prome devuelve un string, y con key comparo strings OK!
'''
'''Es muy importante tener en cuenta que al trabajar con una función propia, ya sea para
ordenar listas ordinarias o tablas, la función debe esperar recibir exactamente un único
elemento del tipo que se está ordenando; siempre. Porque eso es lo que le enviará para 
cada uno de los elementos a comparar, de manera automática sort() o sorted(). Eso es 
algo que no podemos modificar.'''

'''O sea que si estamos ordenando una lista de números, la función que asociaremos al 
parámetro key debe esperar estrictamente un número (sin agregados); y claramente no debe
interactuar con el usuario. Si lo que se pretende ordenar es una lista de listas, la 
función recibirá una lista, del tipo de las que componen las filas de esa tabla.

Por ejemplo, si quieres ordenar una lista de números de acuerdo a la distancia (moda) a
un número fijo cualquiera, para definir una función propia que actúe como clave de 
ordenamiento tendrás que agregarle a tu lista una columna con el número repetido en 
cada fila, o con la la distnacia ya calculada. No podrás enviarle esa información 
adicional a través de la llamada desde sort() o sorted()
'''
#ojo lo anterior ocurre xq los numeros no son enteros son strings, entonces si devuelvo 
# la ditancia, le estoy dando a key un parametro int y no uno de tipo string (como lo 
# son las col de las filas)
#ejemplo abajo CORRECTO
'''
def prome(l): 
    aux=abs(l[1]) #el valor absoluto del segundo ele de c/ lista
    return aux #devuelvo el numero
lista=[['Juan',10,'9.5','7','6'],['Camila',5,'7.5','9','9'],
['Luciana',10,'8','10','10'],['Tomás',8,'2','5','2']] 
print('Lista Original')
for n in range(len(lista)):
    print (lista[n]) 
lista.sort(key=prome,reverse=True) #descendete (may a men) con key=numero
print()
print('Lista Ordenada por Promedio')
for n in range(len(lista)):
    print (lista[n])
#ver q key = prome = dato entero y sorteo justamente datos enteros (10,5,10,8)
'''
#FUNCIONES LAMBDA λ
#Estas funciones sólo admiten en su cuerpo una única expresión que permita obtener el 
#resultado.

#ej de funcion λ
'''
def suma(x,y): 
    return x+y 
#Esta última versión se aproxima bastante a la sintaxis de una función lambda. Si le 
#quito el nombre y el return (ya que se supone que lambda siempre devuelve un resultado) 
#tendríamos lo siguiente:
lambda x,y:x+y
'''
#un ejemplo mas complex
'''
lista=[['Juan','10','9.5','7','6'],['Camila','5','7.5','9','9'],
['Luciana','10','8','10','10'],['Tomás','8','2','5','2']]
print('Lista Original')
for n in range(len(lista)):
    print (lista[n])
lista.sort(key=lambda   lista     :eval('+'.join(lista[1:len(lista)]))/4,reverse=True) 
print()              #param(único)  #expresion se referencia x columnas xq λ recibe filas
print('Lista Ordenada por Promedio') #  lista1[2],lista1[0].upper(),lista1[1].upper())
for n in range(len(lista)):
    print (lista[n])
'''
'''Nota: Prestá atención a la forma en que usamos lambda dentro de sort() (o sorted()). 
El parámetro enviado será siempre uno, la lista a ordenar, (sort() o sorted() van pasando
las filas).
Tiene una única expresión, es una tupla de tres elementos, en este caso. 
Fijate que se referencian los elementos sólo por las columnas, porque lambda recibirá filas
enviadas por sort() (o sorted()).
'''
#funciones Map() y Filter()
'''
map(fun,iter) aplica una función cualquiera a cada elemento de una secuencia y genera otra 
secuencia con los resultados.
filter(fun, iter) selecciona elementos de una secuencia de acuerdo a la evaluación hecha por una
función booleana y devuelve la secuencia con los elementos que pasaron el filtro (la 
función devolvió True).'''
'''Nota: Tanto map() como filter() en PYTHON 3.x devuelven un iterable. Para poder usarlo
correctamente debes convertir la salida antes a lista con list() !!!'''
#ejemplo
'''siguiente ejemplo partimos de una lista de números naturales y obtenemos una lista con 
los cuadrados y otra con los pares.'''
'''
def cuadrado(x):
    return x**2
def par(x):
    if x%2==0:
        return True 
    else: 
        return False
lista=[1,2,3,4,5,6]
print('Lista Original')
print(lista)
lis = list(map(cuadrado,lista))
print('Lista de Cuadrados')
print(lis)
filtro=list(filter(par,lista))
print('Lista de Pares')
print(filtro)
'''
#otro ejemplo con funciones lambda
'''
print('Ingrese 80 números naturales')
import random
numeros=[]
for i in range(80):
    num=random.randint(-100,100)
    #num=int(input('%d- '%(i+1)))
    while num<1: 
        num=random.randint(-100,100)
        #num=int(input('%d- '%i))
    numeros.append(num)
pares=list(filter(lambda n:n%2==0,numeros))
print('Números Pares')
for n in pares: 
    print(n,end=',')
print()
print('Cantidad de pares: ',len(pares))
impares=list(filter(lambda n:n%2!=0,numeros))
print('Números Impares')
for n in impares: 
    print(n,end=',')
print()
print('Cantidad de impares: ',len(impares))
'''
#Guia de ejs
#ej 1
'''
Cargar una lista de 20 nombres femeninos. Mostrar la lista ordenada alfabéticamente con los
nombres en minúscula, salvo la letra inicial.'''
#notas
'''
a='hola'
print(a.title())
l=['7','3','5','9','-11']
l.sort()
print(l)
'''
'''
datos=[]
for i in range (4):
    print(datos)
    if i>0:
        print('elem 0 datos: ',datos[0])
    datos.insert(-1,[1+i,2,3]) #si no existe la pos '8'
    #lo agrega en la posicion len(l)+1. Si pido una posicion
    #anterior n , lo agrega en la poscion n, pateando
    #al q ya esta hacia adelante.
print(datos)
'''
'''
datos=[0,1,2,3,5]
datos.insert(-1,4) #recordad q si es neg da la vuelta
print(datos)
'''

#Guia de ejs

#Ej 1
'''Cargar una lista de 20 nombres femeninos. Mostrar la lista ordenada alfabéticamente con los
nombres en minúscula, salvo la letra inicial.'''
#Opción a:
'''
def carga(lista):
    for i in range(20):
        nom=input('Ingresá nombre femenino  ')
        while not nom.isalpha():
            nom=input('Ingresá nombre femenino  ')
        lista.append(nom.capitalize())

lis=[]
carga(lis)
lis.sort()
print()
print('Nombres Femeninos')
for n in lis:
    print(n)
'''
#Opción b:
'''
def sinacen(s):
    trad=s.maketrans('áéíóú','aeiou')
    s=(s.lower()).translate(trad)
    return s
    
def carga(lista):
    for i in range(20):
        nom=input('Ingresá nombre femenino  ')
        while not nom.isalpha():
            nom=input('Ingresá nombre femenino  ')
        lista.append(nom.capitalize())

lis=[]
carga(lis)
lis.sort(key=sinacen)
print()
print('Nombres Femeninos')
for n in lis:
    print(n)
'''
#Ej 2
'''CargarCargar una lista de 20 nombres femeninos y otra con 20 nombres masculinos. Armar una 
sola lista que contenga los nombres de las mujeres primero y luego los de los hombres. Todos 
los nombres deben estar en minúscula. Además, los nombres de mujeres deben estar ordenados alfabéticamente
entre ellos y los de los hombres también'''
'''
def sinacen(s):
    trad=s.maketrans('áéíóú','aeiou')
    s=s.translate(trad)
    return s
    
def carga(lista,txt):
    for i in range(20):
        nom=input('Ingresá nombre %s  '%txt)
        while not nom.isalpha():
            nom=input('Ingresá nombre %s  '%txt)
        lista.append(nom.lower())

lisFem=[]
lisMasc=[]
carga(lisFem,'femenino')
print()
carga(lisMasc,'masculino')
lisFem.sort(key=sinacen)
lisMasc.sort(key=sinacen)
lis=lisFem+lisMasc
print()
print('Nombres Ingresados')
for n in lis:
    print(n)
'''
#ej 3
#Opción a:
'''Cargar una lista de n nombres de ciudades y mostrarla ordenada. Luego solicitar el nombre de otra
ciudad y cargarla en la posición que corresponda alfabéticamente si no está previamente 
cargada.'''
'''
def carga(lista):
    nom=input('Ingresá nombre de ciudad, * para salir  ')
    while nom!='*':
        lista.append(limpia(nom))
        nom=input('Ingresá nombre de ciudad, * para salir  ')

def limpia(s):
    s=(s.strip()).upper()
    for car in s:
        if not car.isalpha() and car!=' ':
            s=s.replace(car,'*') #mete astersicos en los no alphanum
    s=s.replace('*','') #saca asterisco
    return s

def agrega (ciudades,c):
    ciudades.append(c) #ciudades es la lista ciud
    ciudades.sort() #ordeno la lista ciud
    print(ciudades) 

ciud=[]
carga(ciud)
print()
ciud.sort()
otra=input('Ingrese nombre de ciudad  ')
otra=limpia(otra)
if otra not in ciud:
    agrega(ciud,otra)
print()
print('Nombres de Ciudades')
for n in ciud:
    print(n)
'''
#Opción b
'''
def carga(lista):
    nom=input('Ingresá nombre de ciudad, * para salir  ')
    while nom!='*':
        lista.append(limpia(nom))
        nom=input('Ingresá nombre de ciudad, * para salir  ')

def limpia(s):
    s=(s.strip()).upper()
    for car in s:
        if not car.isalpha() and car!=' ':
            s=s.replace(car,'*')
    s=s.replace('*','')
    return s

def agrega (ciudades,c):
    lugar=len(ciudades)
    i=0
    while i<len(ciudades) and lugar==len(ciudades):
        print(lugar)
        if c<ciudades[i]: #recordar q se compara el ascii de 1era letra! #ver ej abajo
            lugar=i #xa cortar el while  
        i+=1    #ademas es justo donde tengo q dejar la ciudad xa ordenar
    ciudades.insert(lugar,c) #meto la ciudad

ciud=[]
carga(ciud)
print()
ciud.sort() #primero ordeno 1 vez
otra=input('Ingrese nombre de ciudad  ')
otra=limpia(otra)
if otra not in ciud:
    agrega(ciud,otra)
print()
print('Nombres de Ciudades')
for n in ciud:
    print(n)
'''
'''
#ejemplo de comparacion de strings->se compara el ascii 
#aca b tiene mas ascii q a b>a a<b
var='a'
let='b'
if var<let:
    print('a es menor a b')
else:
    print('a es mayor a b')

var='a'
let='B'
if var<let:
    print('a es menor a b')
else:
    print('a es mayor a B')
'''
#Ej 4
'''Cargar una lista de n platos de un menú. Mostrar luego sólo los platos cuyo nombre comienza con
las letras de la c a la f incluídas.'''
'''
def sinacen(s):
    trad=s.maketrans('áéíóú','aeiou')
    s=s.translate(trad)
    return s
    
def carga(lista):
    nom=input('Ingresá nombre de plato, * para salir  ')
    while nom!='*':
        lista.append(limpia(nom))
        nom=input('Ingresá nombre de plato, * para salir  ')

def limpia(s):
    s=(s.strip()).lower()
    for car in s:
        if not car.isalpha() and car!=' ':
            s=s.replace(car,'*')
    s=s.replace('*','')
    return s

menus=[]
carga(menus)
print()
menus.sort(key=sinacen)
print('Lista de Platos (C-F)')
for p in menus:
    if p>='c'and p<'g':
        print(p.title())
'''
#Ej 5
'''Elaborar un programa que permita cargar una lista con 10 nombres. Luego debe mostrar la lista
ordenada de mayor a menor por cantidad de acentos. Se aceptan nombres compuestos.'''
'''
def cuentacen(s):
    cant=0
    for car in ('á','é','í','ó','ú'):
        cant+=s.count(car) #Recordar, s.count('ele a contar') devuelve cant de veces q aparece
    return cant
    
def carga(lista):
    for i in range(10):
        nom=input('Ingresá nombre número %d  '%(i+1))
        nom=limpia(nom)
        lista.append(nom)

def limpia(s):
    s=(s.strip()).lower()
    for car in s:
        if not car.isalpha() and car!=' ':
            s=s.replace(car,'*')
    s=s.replace('*','') #creo q esta linea esta demas, se la podria quitar colocando un '' 
    return s.title() # en el lugar del replace line 621 en vez de *

nom=[]
carga(nom)
print()     #recordar sort envia filas => el valor de key con q ordeno es de cada fila
nom.sort(key=cuentacen,reverse=True) #ordeno segun el numero de vocales acentudas en c/ plbr (return de cuentacen)
print('Lista de Nombre Ordenada de más a menos acentos')
for n in nom:
    print(n)
'''
#Ej 6
'''Cargar una agenda con apellido, nombre, teléfono fijo y móvil. El fin de contactos viene 
dado por *. Mostrar la agenda ordenada alfabéticamente por nombre y apellido.'''
'''
def criterio(l):
    return (sinacen(l[1]),sinacen(l[0])) #primero nombre l[1] dsps apel l[0]

def sinacen(s):
    trad=s.maketrans('áéíóú','a3l0u') #asocia a cada valor de 1 un valor en 2
    #print(s)           #1      #2
    s=(s.lower()).translate(trad) #pongo en minucula y dsps "aplico el trans" (reemplazo letra x letra)
    print(s)
    return s #devuelve sin acentos, SOLO xa ordenar
    
def carga(lista):
    apel=input('Ingresá apellido contacto, * para salir  ')
    while apel!='*':
        apel=limpia(apel)
        nom=input('Ingresá nombre de %s  '%apel.title())
        nom=limpia(nom)
        fijo=input('Ingresá teléfono fijo de %s  '%(nom.title()+' '+apel.title()))
        celu=input('Ingresá celular de %s   '%(nom.title()+' '+apel.title()))
        lista.append([apel,nom,fijo,celu])
        apel=input('Ingresá apellido contacto, * para salir  ')

def limpia(s):
    s=(s.strip()).lower()
    for car in s:
        if not car.isalpha() and car!=' ':
            s=s.replace(car,'*')
    s=s.replace('*','')
    return s

agenda=[]
carga(agenda)
print()
agenda.sort(key=criterio)
print('Lista de Contacots Ordenada por Nombre y Apellido')
for n in agenda: #imprime sin pasar x sinacen, es decir con todos los acentos
    print((n[1][:15].title()).ljust(16),(n[0][:15].title()).ljust(16),n[2].rjust(10),n[3].rjust(10))
'''
#Ej 7
''' Cargar aleatoriamente una lista de 30 números enteros entre 1 y 100. Mostrarla ordenada
de menor a mayor por la distancia de cada número al promedio de los 30.
Ejemplo:
Números ordenados del más cercano al más lejano al promedio:
50.833333333333336
53 2.1666666666666643
48 2.8333333333333357
45 5.833333333333336
57 6.166666666666664
44 6.833333333333336
44 6.833333333333336
58 7.166666666666664
42 8.833333333333336

61 10.166666666666664
84 33.166666666666664
88 37.166666666666664
13 37.833333333333336
93 42.166666666666664
99 48.166666666666664'''
'''
import random
def promedio(lista):
    suma=0
    for num in lista:
        suma+=num[0] #los numeros de la lisat
    return suma/len(lista)

def carga(lista):
    for i in range(30):
        lista.append([random.randint(1,100),0])
#cada ele es una lista con numero         , 0   

def prepara(lista,p):
    for n in lista: #cada dupla (lista)
        n[1]=abs(n[0]-p)   #el "cero" de la pos 1 pasa a valer modulo de prom - num (distancia xd)
        
lis=[]
carga(lis)
print(lis)
prome=promedio(lis)
prepara(lis,prome)
lis=sorted(lis,key=lambda lis:lis[1]) #ordeno segun el ele 1, de cada dupla/lista (la distancia)
print('Números ordenados del más cercano al más lejano al promedio:',prome)
for n in lis:   #xa cada duplalista
    print(n[0],n[1])    #imprimo el numero y la distancia
'''
#ej 8
'''Cargar una lista de números enteros entre 1 y 1000. Mostrar al final sólo los números 
terminados en 0.'''
#Opción a:
'''
def carga(lista):
    num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
    while num not in range(0,1001):
        num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
    while num>0:    #salgo con cero pues >
        lista.append(num)
        num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
        while num not in range(0,1001): #pido q sea > 0 si pongo 0...ver while
            num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
       
lis=[]
carga(lis)
print(lis)
lisStr=list(map(lambda x:str(x)[::-1],lis)) #1ero convierto a string cada ele de la lista (pues son ints)
print(lisStr)  #2do recorto cada ele desde el ele 0 (es decir tomo solo ese ele) con un paso de -1 (hacia atras) = invertir el numero 
lisStr=sorted(lisStr) #ordeno (muestra lista con numeros invertidos) primero aparecen los terminados en 0, pues inverti la lista
print('Números terminados en 0')
if lisStr[0][0]=='0': #como estan invertidos y ORDENADOS SOLO si alguno tiene cero (aparece primero),
    print(lisStr[0][0]) #esta primerotiene cero ahora aparece primero
    print(lisStr[0][::-1])#imprimo el primer numero de la lista dandolo vuelta de nuevo
    i=1 #y ahora el resto
    while i<len(lisStr)and lisStr[i][0]=='0':   #si estoy en la lista y la pos[0] del ele i es = 0, 
        print(lisStr[i][::-1])  #imprimime el numero ese (invertido)
        i+=1
#como la lista esta ordenada los imprime ordenados
'''
#Opción b:
'''

def carga(lista):
    num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
    while num not in range(0,1001):
        num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
    while num>0:
        lista.append(num)
        num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))
        while num not in range(0,1001):
            num=int(input('Ingresá número entre 1 y 1000, 0 para salir  '))

        
lis=[]
carga(lis)
print(lis)      #filter solo devuelve los valores de la fun q cumple la condicion
lis0=list(filter(lambda x:x%10==0,lis)) #si el resto de dividir x 10 es cero termina en cero
print('Números terminados en 0') # map devolveria true o false
for n in lis0:
    print(n)
'''
#Ejercicio de autoevaluación
''' Cargar una lista con 50 números entre 100 y 200 de forma aleatoria. Solicitar al usuario el 
ingreso de un número entre 100 y 200 y brindarle el siguiente menú de opciones:
Agregarlo en la lista en la posición correcta para mantenerla ordenada ascendentemente
Determinar cuál es el elemento de la lista más cercano
Ordenar la lista de manera ascendente de acuerdo a la distancia de cada elemento al número
ingresado'''
'''
import random
def cargaLista(l):
  for i in range(50):
    l.append(random.randint(100,200))

def inserta(lista,n):
  lista.append(n) #meto el numero en clqr pos
  lista.sort() #ordeno la lista (queda en la pos correcta)

def cercano(lista,n):
  l=[]
  for i in range(len(lista)):
    l.append([abs(lista[i]-n),lista[i]]) #en l meto tuplas con 2 ele. el primero la dustancia, el segundo el num
    return min(l) #devuelvo la lista del men num recordar que lo hace segun el primer ele de la tupla
                    #[distancia, numero]
def ordenaDesv(lista,n):
  l=[[abs(elem-n),elem] for elem in lista]  #Xa cada ele de la lista haceme otra lista con [distancia, numero]
  l.sort()  #ordenamela (segun distancia al num elegido)
  lista.clear() #borro la lista orig
  for i in l:   #y la cargo de nuevo pero ordenada
    lista.append(i[1]) #i[1]= cada numero

def clave(n):
  return abs(n-150)

def ordena(lista,sentido,funcion):
  lista.sort(reverse=sentido,key=funcion)
  
numeros=[]
cargaLista(numeros)
opc=1
opciones=(1,2,3)
while opc in opciones:
  print('MENU DE OPCIONES')
  print('1-Insertar un Número Ordenadamente','2-Determinar más Cercano a un Número',sep='\n')
  print('3-Ordenar Lista por Desvío a un Número')
  print('Otro-Salir')
  print(numeros)
  opc=int(input('ingrese opc: '))  #elijo opc
  if opc in opciones:
    num=int(input('Ingrese número: '))  #dsps pido numero
    while num<100 or num>200:
      num=int(input('Ingrese número: '))
    if opc==1:          #escribo las funciones xa cada opc
      inserta(numeros,num)
      print(numeros) #ya estan ordenados
    elif opc==2:                        #como devuelvo 2 valores...
        distancia,n=cercano(numeros,num)#distancia=[abs(lista[i]-n), n= minimo distancia
        print(n,'es el número más cercano a',num,'sólo a',distancia)
    elif opc==3:
     ordenaDesv(numeros,num)
     print(numeros)
print('ADIOS') #ADIOS!
'''

