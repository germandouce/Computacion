                        #PRÁCTICA VII FUNCIONES Y PROCEDIMIENTOS: 
#INTRO Y TEORIA
#Un ejemplo
'''
def suma(x,y):
    return (x+y)      
a=int(input())
b=int(input())
print('a','+','b','=', suma(a,b)) 
'''
#Matching o apareo de parametros (posicional), python compara a y b con x e y
#Si modifico x, en realidad no estoy tocando a. Cuando se envía a una funciónun parámetro 
#de este modo se dice que el Pasajede Parámetroes por Valor
#La funcion utiliza un espacio de memoria separado al del FCP para ejecutarse
#Cuando python ejecuta la funcion "suma", guarda en una variable temporal el resultado de dicha operac
#AMBITO DE UNA FUNCION: La region de memoria donde se ejecuta, define variables propias dentro de ella
#DURACION, ALCANCE, VIDA de un objeto: como máximo, el tiempo que permanece en ejecución la función que lo crea

#Otro ej
'''
def suma(b,a):
    b=b+a
    return b            #no tira errores porque esta b este definida dentro del ambito de
print('Ingresá dos números') #de la funcion suma
a=int(input())
b=int(input())
c=suma(a,b) #Recien aca el programa llama a la funcion suma, hace matching con b y a 
print(a,'+',b,'=',c)            #y devuelve el valor de suma
'''
#NO HACER!!!
'''
def suma(b,a):
    return(x+y)     ##MUY MAL! No se debe referenciar una variable global dentro de una funcion
print('Ingresá dos números')  #deberia decir return (a + b)
x=int(input())
y=int(input())
print(x,'+',y,'=',suma (x,y))
'''

#Guia de ejs
#PRIMERA PARTE 1: complete las siguientes funciones para que realizen lo pedido
#Ej 7.1: 
'''
Ejemplo:
Ingrese un texto l8/a CULPA NO ES DE LA chancha==, sino de quien" le da de comer!
Texto inicial
l8/a CULPA NO ES DE LA chancha==, sino de quien" le da de comer!
Texto Modificado
La culpa no es de la chancha, sino de quien le da de comer!
'''
'''
def muestra(c,t):
    print(c)
    print(t)
    print()

def leeTxt():
    t=input('Ingrese un texto: ')
    return t

def limpia(t):
    puntuacion=(' ',',',';','.',':','-','?','!','¿','¡')
    t=t.strip()
    for car in t:
        if not car.isalpha() and car not in puntuacion:
            t=t.replace(car,'*')
    t=t.replace('*','')
    t=t.capitalize()
    return t

def invalidos(t):
    puntuacion=(' ',',',';','.',':','-','?','!','¿','¡')
    respuesta=False
    i=0
    while i<len(t) and not respuesta: #mientras i recorre el texto y respuesta no es F (es V)
        if not t[i].isalpha() and t[i] not in puntuacion:
            respuesta=True #si no es alfa o no esta en puntuacion, la rta es tru, entonces
        i+=1               #salgo del loop, y entro al if (del FC pcpal) y t=limpia
    return respuesta    #devuelvo rta, segun el while es true o false

texto=leeTxt()
if invalidos(texto): #si rta es true, t=limpia(texto), si es false, salto al print
    t=limpia(texto)
print(invalidos(texto))
muestra('Texto inicial:',texto)
muestra('Texto Modificado:',t) #solo se muestra si el txto es modificado xq t se define 
#dentro del if, sola// si hay chars invalidos
'''
#Ejercicio 7.2
'''Ejemplo:
Ingrese un texto CualQUIERA puede estar más cómodo aquí QUE ALLÁ!!
Texto inicial
CualQUIERA puede estar más cómodo aquí QUE ALLÁ!!
Texto con Shift a derecha
dvbmrvjfsb qvfef ftubs nbt dpnpep brvj rvf bmmb!!
Texto con Shift a izquierda
btzkpthdqz otdcd drszq lzr bnlncn zpth ptd zkkz!!'''
#escribe la oracion pero en cada letra pone la q le sigue en el abcdario
'''
def muestra(c,t):
    print(c)
    print(t)
    print()

def leeTxt():
    t=input('Ingrese un texto  ')
    return t

def derecha(t):
    con='áéíóú'
    sin='aeiou'
    sacaAcento=t.maketrans(con,sin) #meto en un diccionario los ascii de las letras de con y sin
    t=t.lower() #minuscula a todo
    t=t.translate(sacaAcento) #("encripta", reemplaza las letras de con por las de sin)
    letras='' #defino varibale letras vacio
    for i in range(97,123):
        letras=letras+chr(i) #ahora letras es un string con todo el abcdario
    desplaza=letras[1:]+letras[0] #desplaza es el abcdario pero empzando con b y poniendo la a al final
    nuevo='' #variable para meter otro texto   #bcd...za asi las letras estan corridas hacia la der
    for car in t:
        if car.isalpha():
            nuevo+=desplaza[letras.find(car)] #los voy agregando en la var nuevo
            # letra [(posicion del car en la cadena letras)]  en desplaza la letra de letras esta corrida 1 a la dere
        else:
            nuevo+=car #si no es alpha no lo cambio por nada
    return nuevo

def izquierda(t):
    con='áéíóú'
    sin='aeiou'
    sacaAcento=t.maketrans(con,sin)
    t=t.lower()
    t=t.translate(sacaAcento)
    letras=''
    for i in range(97,123):
        letras=letras+chr(i) #string con todo el abcdario
    desplaza=letras[len(letras)-1]+letras[:len(letras)-1] #corro el abcdario hacia la izq zabcd...y
    nuevo='' #xa el texto
    for car in t:
        if car.isalpha():
            nuevo+=desplaza[letras.find(car)]#mete las letras pero desplazadas a la izq
        else:
            nuevo+=car
    return nuevo

texto=leeTxt()
muestra('Texto inicial',texto)
t1=derecha(texto)
t2=izquierda(texto)
muestra('Texto con Shift a derecha',t1)
'''
#PROGRAMA DE ENCRIPTACION
#s.maketrans(x[,y[,z]])
'''asocia en un diccionario los correspondientes ASCII de las cadenas x e y
Ejemplo:'''
'''
vocales="aeiou"
numeros="12345"
texto="murcielagos"
relacion=texto.maketrans(vocales,numeros) #guarda y asocia el ascii de a y 1, ey 2,i y 3 etc
print(texto.maketrans(vocales,numeros))
print(texto.translate(relacion))
'''
#s.translate(pares)
'''devuelve s con los caracteres asociados en el diccionario pares remplazados
Ejemplo:
vocales="aeiou"
acentos="áéíóú"
texto="murcielagos"
parejas=texto.maketrans(vocales,acentos)# guarda y asocia el ascii de a y á, e y é, i e í etc
print(texto.translate(parejas)'''

#TEORIA ADICIONAL PARA SEGUNDA PARTE

#Ejemplo de devolución de tupla en una función
'''
def carga():
    nom=input('Ingresá nombre ')
    nom=mejora(nom)
    apel=input('Ingresá apellido de %s '%nom)
    apel=mejora(apel)
    edad=int(input('Ingresá edad de %s '%(nom+' '+apel)))
    while edad<1:
        edad=int(input('Ingresá edad de %s '%(nom+' '+apel)))
    return nom,apel,edad #OJO CON EL ORDEN
def mejora(txt):
    for car in txt:
        if not car.isalpha()and car!=' ':
            txt=txt.replace(car,'*')
    txt=txt.replace('*','')
    txt=txt.strip()
    return txt.title()
datos=[]
opc=input('Cargas? s/n ')
while opc=='s'or opc=='S':
    nom,apel,edad=carga() #le asigno a cada var la correspondiente q devuelve carha
    datos.append([nom,apel,edad])
    opc=input('Cargas? s/n ')
print('Datos')
for persona in datos:
    print(persona[1],',',persona[0],' ',persona[2],' años',sep='')
'''
#Si usamos * delante de un parámetro, en la definición de la función, estamos diciendo 
# que ese es un parámetro tuplaque recibirá una cantidad arbitraria de datos.
#ejemplo bastante feo pero ingenioso...
'''
def prueba(oper,*num): #*num puede recibir una cantidad varibale de parametros
#num se convierte en una tupla
    total=str(num[0]) #pasame a string el primero ele de num esta linea sirve solo xa q no de
    for n in num[1:]: #xa q no sume 2 vcs el 2 #error python xq no puedo definir total dentro del for
        total=str(total)+oper+str(n) #n cada vuelta agrego numeros con la oper al string
        print(total,'=',end=' ') # 2 = (me quedo en el renglon)
    return eval(total) #evalua el string de total como una suma 

print(prueba('+',2,3,4,5)) #se imprime en mismo renglon q el print de la funcion
print(prueba('-',2,3,4))
print(prueba('*',2,3,4,10,0.6))
'''
#Nota:Si una función espera parámetros fijos y variables, siempre el parámetro 
# variable debe ir al final!!!
'''
def suma(*terminos):
    acum=0
    for t in terminos:
        acum+=t
    return acum
print('Sumador')
n1=int(input('nro 1: '))
n2=int(input('nro 2: '))
n3=int(input('nro 3: '))
print(suma(n1,n2,n3))
'''
#Es decir, que la función espere una cantidad fija de parámetros, pero que éstos, en vez
#de ser enviados de forma separada, se encuentren contenidos en una lista o tupla. En este
# caso, el signo asterisco (*) deberá preceder a ia estructura de datosque es pasada como
# parámetro durante la llamada a la función
'''
def prueba(oper,n1,n2): #espero 3 parametros
    return eval(str(n1)+oper+str(n2))
print(prueba(*('+',2,3))) #envio 3 pero en una tupla
operacion=('*',5,10)
print(prueba(*operacion))
'''
#Nota:Si vas a poner un argumento opcional, éste debe ir en último lugar!!!

#LOS OBJETOS INMUTABLES SE PASAN POR VALORY LOS MUTABLES POR REFERENCIA.
#Pasaje de Parámetro por Valor, (la tupla es inmutable)
#Cuando "modifico la tupla" creo una var tupla dentro de la MI de cambia() q apunta a (1,0)
#mientras que en la MI del ppal queda temp=(1,0) (se guarda en una var temporal) y la tupla
# t1 sigue apuntando a [1234]. Cuando termina cambia, t1, mantiene su valor porque no fue 
# modificada en la MI
'''
def cambia(tupla):
    print('Estoy en cambia')
    print('Esta es la tupla que recibo: ',tupla)
    tupla=(1,0)
    print('Esta es la tupla que modifico: ',tupla)
    return tupla
t1=(1,2,3,4)
print('Estoy en PPal')
print('Esta es la tupla inicial antes de invocar cambia ',t1)
t2=cambia(t1)
print('Estoy en PPal')
print('Esta es la tupla inicial después de invocar cambia ',t1)
print('Esta es la tupla que devuelve cambia ',t2)
'''
#Pasaje de Parámetro por Referencia (la lista es mutable)
#Cuando "modifico la lista" creo una var lista dentro de la MI de cambia() q apunta a [1,0]
#mientras que en la MI del ppal queda intacta la original l=[1,2,3,4]. CUando termina cambia()
#mantine su valor
'''
def cambia(lista):
    print('Estoy en cambia')
    print('Esta es la lista que recibo: ',lista)
    lista=[1,0]
    print('Esta es la lista que modifico: ',lista)
l=[1,2,3,4]
print('Estoy en PPal')
print('Esta es la lista inicial antes de invocar cambia ',l)
cambia(l)
print('Estoy en PPal')
print('Esta es la lista inicial después de invocar cambia ',l)
'''
#Pasaje de Parámetro por Referencia
#Ahora si se modifica la lista porque al hacer l[1]=0 no estoy creando ninguna copia en la MI
# de cambia. Estoy trabajando sobre la l del ppal
'''
def cambia(lista):
    print('Estoy en cambia')
    print('Esta es la lista que recibo:  ',lista)
    lista[1]=0
    lista.append(10)
    print('Esta es la lista que modifico:  ',lista)
l=[1,2,3,4]
print('Estoy en PPal')
print('Esta es la lista inicial antes de invocar cambia  ',l)
cambia(l)
print('Estoy en PPal')
print('Esta es la lista inicial después de invocar cambia  ',l)
'''
#Corolario de pasaje de objetos mutables de la profesora arriazu:

#Si vas a definir una función carga() que cargue una lista te conviene trabajar con una de dos opciones:
# 1- Debes crear la lista vacía en el PPal y enviarla como argumento a carga() 
# Cuando carga() finalice, tendrás la lista cargada X ej:
'''
def carga(lista):
    for i in range(4):
        lista.append(i)
        i+=1
l=[]
carga(l)
print(l)
'''
# 2- Puedes crear la lista dentro de carga() y rellenarla con todo lo ingresado. Pero al 
# finalizar debes devolver la lista cargada con un return y desde el PPal debes convocar 
# a carga de la siguiente manera: lista=carga() X ej:
'''
def carga(): #no colocar l como argumento, porque no es un parametro q necesite de antes,
    l=[]     #lo defino dentro de la funcion
    for i in range (5):
        l.append(i)
        i+=1
    return l #Devuelvo solo lo q necesito: la lista
#NO HACER
#print(l) #no la imprime porque l estra definida solo en la MI de carga()
lista=carga() #Guardo el return de carga en una var xa no perderlo
print(lista) #Ademas, carga() no tiene argumentos, no "evaluarla" en nada
'''
#Si no quiero que las modificaciones que hagas a una lista dentro de una función permanezcan
#cuando la función deje de existir hay un único camino para eso:
# La función debe trabajar con 'su propia copia'. Por lo tanto:
# 1- Puedo enviarle ya una copia desde el PPal. Aunque quedará almacenada en la región de 
# MI del PPal, no será la misma zona de la original.
'''
def funcion(l):
    l[0]=0
    return l
l=[1,2]
print(l)
lis=l.copy()
print(funcion(lis))
'''
#  2-Puedes hacer una copia dentro de la función
'''
def función(lista):
    lis=l.copy()
    #sigo trabajando con lis
    lis[0]=0
    return lis

l=[1,2]
print(l)
print(función(l))
'''
# 3-Puedes enviarle una copia en la llamada. En este último caso la copia quedará en la MI
# del PPal, pero no será accesible desde allí, porque no tendrá una variable asociada
'''
def funcion(l):
    l[0]=0
    return l
l=[1,2]
print(l)
print(funcion(l.copy()))
'''
#Otra manera de copiar efectivamente una lista es usando el siguiente artilugio:
# l=list(tuple(lista))
#Al pasar, con la función tuple(), la lista a un objeto de tipo inmutable,la tupla se 
# coloca en otra región de MI(son objetos diferentes). Luego cuando la reconvierto a 
# lista ya se perdió la conexión de MI con la lista original. Puedes emplear esto también 
# para trabajar con copias de listas dentro y fuera de funciones.
'''
def funcion(l):
    l=list(tuple(l))
    l[0]=0
    return l                                                                            
l=[1,2]
print(l)
print(funcion(l))
'''
#Ejemplo interesante xa una tupla q tiene una lista adentro (un objeto inmutable)
'''
def fun1(t):
    t[0][1]='*'
def fun2(l):
    l[2]='*'
lis=[1,2,3,4]
t=(lis,3)
#si no quisiese guardar las modificaciones sobre la tupla para usar afuera de la funcion:
#t=(lis.copy(),3)

print(t)
print('Antes de fun1','PPal','lis:',lis,'t:',t)

fun1(t)
print('Despues de fun1','PPal','lis:',lis,'t:',t)

fun2(lis)
print('Despues de fun2','PPal','lis:',lis,'t:',t)
'''

#SEGUNDA PARTE: En todos los ejercicios debe emplearse técnicas de modularización con funciones propias

#ejercicio 7.3
'''Confeccionar un programa que permita leer un texto y luego reemplazar en el mismo todas las
vocales por un carácter sugerido por el usuario.
Ejemplo:
Ingrese texto: Un sol sale todos los días por la mañana
Caracter de reemplazo: a
Texto reemplazado: An sal sala tadas las daas par la mañana'''
'''
def depura(t):
    t=t.strip()
    t=t.lower()
    return t #devuelvo texto depurado

def cambia(tx,c):
    tx=depura(tx) #mando a depura el tx
    for vocal in ('a','e','i','o','u','á','é','í','ó','ú'): #xa cada vocal
        tx=tx.replace(vocal,c) #reemplazo en todo el texto x c
    return tx.capitalize() #devuelvo el texto con los reemplazos

texto=input('ingrese texto')
caracter=input('ingrese caracter de reemplazo')
print('texto reemplazado')
print(cambia(texto,caracter)) #mando texto y caracter a la funcion
'''
#Ejercicio 7.4
'''Confeccionar un programa que permita leer un texto e informe cuántas vocales hay en él. Desarrolle
e invoque una función depura que organice el texto reemplazando todo carácter que no sea blanco o
letra por espacio y deje todo el texto en minúsculas.'''
'''
def depura(t):
    t=t.strip()
    t=t.lower()
    for letra in t:
        if not(letra.isalpha()or letra==' '):
            t=t.replace(letra,' ')
    return t

def cuenta(t):
    cont=0
    for letra in t:
        if letra in ('a','e','i','o','u','á','é','í','ó','ú'):
            cont+=1
    return cont
texto=input('ingrese un texto: ')
texto=depura(texto)
print('Hay',cuenta (texto), 'vocales en: ' )
print(texto)
'''
#ejercicio 7.5
#Confeccionar un programa que permita leer un texto e informe si hay una cantidad par o impar de consonantes.
'''
def depura(t):
    t=t.strip()
    t=t.lower()
    for letra in t:
        if not (letra.isalpha()):
            t=t.replace(letra,'')
    return t #devuelvo texto depurado

def cuenta (tx):
    tx=depura(tx) #traigo tx depurado
    total=0
    for vocal in ('a','e','i','o','u','á','é','í','ó','ú'):
        total+=tx.count(vocal)
    return len (tx)-total #longitud total del texto -vocales =cosonantes

def par(cant):
    return bool(cant%2-1) #devuelve el valor booleano de "el resto de dividir por 2 -1"
                          # 0 False (impares) cualquier otro valor True (pares) (-1)
texto=input('ingrese un texto: ')
if par(cuenta(texto)):
    print('Hay una cantidad par de consonantes en: ')
else:
    print('Hay una cantidad impar de consonantes en: ')
print(texto)
'''
#ej 7.6
#Ejercicio 7.6
'''Programe el Juego de Batalla Naval usando funciones propias. Puede tomar de base el código
brindado por la cátedra para resolver el ejercicio.'''
'''
import random
def tableroVacio(l):
  for i in range(10):
    l.append([])
  for i in range(10):
    l[i]=[' ']*10


def carga(l1):
  orientacion=(0,1,2,3)
  tableroVacio(l1)
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
  return l1


def juega (l1,tope):
  cont=0
  hayFlota=True
  while (cont<tope)and hayFlota:
    fila=0
    while (fila<1)or(fila>10):
      fila=int(input('Ingrese fila: '))
    columna=0  
    while (columna<1)or(columna>10):
      columna=int(input('Ingrese columna: '))
    if l1[fila-1][columna-1]=='*':
      print('TOCADO')
      l1[fila-1][columna-1]=' '
    else:
      print('AGUA')
    quedan=0
    for i in range(10):
      quedan+=l1[i].count('*')
    hayFlota=bool(quedan)
    cont+=1
  return hayFlota


tablero=[]
tablero=carga(tablero)
if juega(tablero,60):
  print('PERDISTE EL JUEGO!!!')
else:
  print('GANASTE EL JUEGO!!!')
'''
#ej 7.7
'''
Realice un programa que permita leer un texto y luego elimine la última aparición en el mismo de
una cadena brindada por el usuario.
Ejemplo:
Ingrese texto: La luna sale todos los días por la tarde
Cadena a eliminar: la
Texto resultante: La luna sale todos los días por tarde
'''
'''
def elimina(tx,c):
    tx=tx.lower()
    tx=invierte(tx)#invierto el texto xq voy a eliminar la ult (la 1era q encuentro)
    c=invierte(c) #invierto la cadena xa coincidir con texto
    pos=tx.find(c) #devuelve la posicion de la cadena
    #aclaracion xa mejor comprension de la funcion
    #print('eltexto ivertido:', tx)
    #print('tx hasta plbra:',tx[:pos])
    #print('txt dde plbra h/ final:',tx[pos+len(c):])
    tx=tx[:pos]+tx[pos+len(c):] #dejo el texto hasta la palabra (no la incluye)
        # y le sumo lo q queda desde la palabra 
    
    tx=invierte(tx) #pongo al derecho
    return tx.capitalize()

def invierte(cadena):
    l=list(cadena) #convierto el string en lista xa invertirlo
    l.reverse() #lo invierto (como lista)
    cadena=''.join(l) #haceme string la lista l, uniendo segun espacio ('')
    return cadena

texto=input('ingrese un texto: ')
subText=input('inrese cadena a eliminar: ')
print('texto resultante: ')
print(elimina(texto,subText))
'''
#ej 7.8
'''Confeccione un programa que permita cargar una lista con números enteros positivos. Reorganice la
lista para que al principio queden los pares y al final los impares.'''
#MIO, MAL RESUELTO, UTIL XA VER QUE NOOOO HACER VER COMENTARIO
'''
def ingreso():
    l1=[]
    n=int(input('ingrese numeros positivos: '))
    while n!=0:
        while n<0:
            n=int(input('Ingrese número positivo, 0 para terminar: '))
        l1.append(n)
        n=int(input())
    return(l1)

def ordenar(num):
    print(num)
    impar=[]
    for n in num:
        print(n)
        if n%2 !=0:
            impar.append(n)
            num.remove(n) #cada vez q hago remove modifico la lista num
            print(num) #entonces cuando la leo de nuevo con el for, tengo un
    print(num) #elemento menos pero el contador cuenta como si ese estuviese
    print(impar) #==> se saltea un elemento
    for imp in impar:
        num.append(imp)
    return (num)

totNumeros=ingreso()
print(ordenar(totNumeros))
'''
#opcion profe
'''
def carga(l):
    num=int(input('Ingrese número positivo, 0 para terminar: '))
    while num!=0:
        while num<0:
            num=int(input('Ingrese número positivo, 0 para terminar: '))
        l.append(num)
        num=int(input('Ingrese número positivo, 0 para terminar: '))

def organiza(l):
    pares=[]
    impares=[]
    for elem in lista:
        if elem%2: #resto 0 es Flase (y par), 1 u otro num es True (e impar)
            impares.append(elem)
        else: 
            pares.append(elem)
    l.clear() #borro la lista (ya guarde imp y par en listas)
    l.extend(pares) #le agrego ak final de l (ahora sta vacia) los pares
    l.extend(impares) #al final de l, pongo los impares (tiene los pares)

def muestra(l):
    print('Primero los pares...')
    print(l)

lista=[]
carga(lista)
organiza(lista)
muestra(lista)
'''
#Ejercicio de Autoevaluación 1
'''Cargar una lista con 50 números entre 100 y 200 de forma aleatoria. Solicitar al usuario el ingreso
de un número entre 100 y 200 y brindarle el siguiente menú de opciones:
Eliminar el número, si se encuentra
Reemplazar el número, si se encuentra, por otro
Agregar el número al principio de la lista
Agregar el número al final de la lista
Agregar el número al final, sólo si no existe ya
Contar la cantidad de apariciones del número en la lista
Opción de salida'''
'''
import random
def cargaLista(l):
    for i in range (50): #50 numeros
        l.append(random.randint(100,200)) #random entre 100 y 200

def elimina (lista,n):
    while lista.count(n)>0:
        lista.remove(n)

def reemplaza (lista,n,otro):
    while lista.count(n)>0: 
        lista.insert(lista.index(n),otro) # (en la ubicacion de n, nuevo)
        lista.remove(n)
        #Insert (posicion en la lista, ele a insertar)

def agrInicio(lista,n):
    lista.insert(0,n)

def agrFinal(lista,n):
    lista.insert(len(lista),n)

def insOrdenado(lista,n):
    lista.sort(reverse=True) #descendente la lista
    i=0
    ban=0
    while (i<len(lista)) and ban==0:
        if lista[i]<n: #ele i de lista es menor a n
            lista.insert(i,n) #en pos i, inserta n
            ban=1
        i+=1
    if ban==0:
        lista.insert(len(lista),n)

def agrFinalNoExiste(lista,n):
    if lista.count(n)==0:
        lista.insert(len(lista),n)

def minModa(lista,n):
    l=[] #creo l vacia
    print(lista)
    for i in lista:
        l.append([abs(i-n),i]) #cargo listas en l con 2 elementos (diferencia, num de lista)
        print(l) #diferencia = (numero de la lista-numero elegido)
    l.sort()  #ordena l segun el 1er ele de cada lista (pos-num), es decir la menor dif
    print(l)
    return (l[0][1]) #devuelve el numero de la lista con menor dif (el 1ero, pues esta ordenada)
            #l habia sido ordenado de may a men

def ordModa(lista,n): #Ordena ascendete x distancia, es decir, de men a may distancia
  print(lista)
  l=[[abs(elem-n),elem] for elem in lista ]  #creo una lista l donde meto listas con [distancia al numero, numero]                
  l.sort() #ordeno la lista l segun el primer elemento de cada listita, es decir, la distancia( elem-n)
  lista.clear() #borro la lista con numeros orig
  for i in l:   #con cada elemento d l ya ordenada
    lista.append(i[1]) #agrego los numeros a la lista orig
  return lista

numeros=[]
cargaLista(numeros)
opc=1 #xa entrar al while
opciones=(1,2,3,4,5,6,7,8,9) #tupla opciones
while opc in opciones:
    print('MENU DE OPCIONES')
    print('1-Eliminar','2-Reemplazar','3-Agregar al Principio',sep='\n')
    print('4-Agregar al Final','5-Insertar Ordenado Descendente',sep='\n')
    print('6-Agregar al Final si no Existe','7- Contar Repeticiones',sep='\n')
    print('8-Buscar Menor Distancia','9-Ordenar Ascendente por Distancia',sep='\n')
    print('Otro-Salir')
    opc=int(input())
    while opc not in opciones:
        opc=int(input())
    existe=opciones.count(opc) #cant de veces q aparece el numero opc en opciones (0 o 1)
    if bool(existe): #notar que existe solo puede ser 0-False o 1-True 
        num=int(input('ingrese número: '))
        while num<100 or num>200: #si no esta en el rango pedido...
            num=int(input ('ingrese un numero'))
        if opc==1: #funcion 1, eliminar
            elimina(numeros,num)
        if opc==2:
            nuevo=1 #xa entrar al while
            while not (nuevo in range (100,201)):
                nuevo=int(input('ingrese numero de reemplazo:'))
            reemplaza(numeros,num,nuevo)
        elif opc==3:
            agrInicio(numeros, num)
        elif opc==4:
            agrFinal(numeros,num)
        elif opc==5:
            insOrdenado(numeros,num)
        elif opc==6:
            agrFinalNoExiste(numeros,num)
        elif opc==7:
            veces=numeros.coun(num)
            if veces==1: #si lo encuentra 1 vez
                print(num,'aparece 1 vez en')
            elif veces==0: #si no lo encuentra
                print(num,'no aparece en')
            else:
                print(num,'aparece',veces,'veces en')
        elif opc==8:
            print('El numero mas cercano a',num,'es',
            minModa(numeros,num))
        elif opc==9:
            numeros=ordModa(numeros,num)
        print(numeros)
        print('ADIOS')
'''
#Ejercicio de autoevaluacion 200
'''Cargar números naturales (0 es salida ) y para cada uno de ellos determinar 
su reverso'''
'''
def inverso(num):
    n=list(str(num)) #crea una lista donde cada ele es un dig de n
    print(n)     #str(num) lo hace string
    n.reverse() #da vuelta la lista con digitos de n
    return int(''.join(n)) #vuelve a unir la lista colocando "" en el 1/2 (vacio)
            #lo paso a int=> si hay un cero que queda adelante lo saca ej: 12300-->321
num=-1
while num!=0:
    while num<0:
        num=int(input('ingrese un número natural (0 xa salir): '))
    if num>0:   #al hacerlo int, saca los ceros al principio
        print('el reverso de',num,'es',inverso(num) )
        num=-1 #xa salir del loop (en realidad entro al n<0 y pido otro numero)
    print('hasta pronto')
'''

