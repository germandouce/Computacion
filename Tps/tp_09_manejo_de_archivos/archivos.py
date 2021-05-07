                               #TP   IX   
                        #MANEJO   DE   ARCHIVOS
#Buffer: En informática, un búfer (del inglés, buffer) es un espacio de memoria, en el que se
#almacenan datos de manera temporal, normalmente para un único uso (generalmente utilizan un
# sistema de cola FIFO)
#OJO XA ABRIR ARCHIVO EJECUTAR DDE TERMINAL ABIERTA EN CARPETA DEBUGGEAR NO SIRVE!!
#ejemplo 1
'''
vacaTxt = open('arch1.txt','r+', encoding='utf_8') #abrimos el archivo arch1 con nombre interno vacaTxt y modo lectura/escritura
t = vacaTxt.readline() #leemos la primer línea de vacaTxt y la guardamos en t (incluye el carácter \n de finalización de línea de una archivo de texto)
print(t)#mostramos la línea
t = input('Ingresá un texto con vaca: ')
while (t.lower()).count('vaca')==0:
    t = input('Ingresá un texto con vaca: ') #pedimos un ingreso validado de un texto que contenga vaca en cualquier parte
vacaTxt.write(t+'\n') #guardamos en vacaTxt la línea ingresada (es menester agregar \n)
vacaTxt.close() #Cerramos el archivo
vacaTxt = open('arch1.txt') #reabrimos el archivo, ahora con modo sólo lectura (por defecto)
todas = vacaTxt.readlines() #leemos todas las líneas y las guardamos en la lista todas
for linea in todas:
    print(linea.strip('\n')) #mostramos cada línea sin \n
vacaTxt.close() #cerramos el archivo
'''
#ejemplo 2
'''
vacaTxt = open('arch1.txt') #abre arch1 con nombre vacaTxt, para lectura
todas = vacaTxt.readlines() #carga en la lista todas la totalidad de las líneas de vacaTxt. El numero entre parentesis es el numero de caracteres
print(todas)
vacaTxt.close() #cierra el archivo (las líneas siguen en todas)
for linea in todas:
    print(linea.strip('\n')) #muestra el contenido de todas (sin\n)
for i in range(len(todas)):
    todas[i]=todas[i].capitalize() #aplica capitalize a todas las líneas (unifica)
t=input('Ingresá un texto con vaca: ')
while (t.lower()).count('vaca')==0:
    t=input('Ingresá un texto con vaca: ') #solicita ingreso validado de un texto que contenga vaca
    t=t.capitalize() #le aplica capitalize
todas.append(t+'\n') #lo agrega a todas (al final, incluyendo el fin de línea)
todas.sort() #ordena la lista
vacaTxt=open('arch1.txt','w') #abre arch1, con nombre vacaTxt en modo sólo escritura, para regrabar completamente el archivo y guardar la versión ordenada con capitalize
vacaTxt.writelines(todas) #graba todas las líneas
vacaTxt.close() #cierra el archivo
vacaTxt=open('arch1.txt') #abre arch1 para lectura
todas=vacaTxt.readlines() #lee todas sus líneas y las carga en lista todas
for linea in todas:
    print(linea.strip('\n')) #muestra las líneas
vacaTxt.close() #cierra el archivo
'''
#ARCHIVOS CSV
#Ejemplo 1
'''
completo=open('datosCompletos.csv','w') #creará o reescribirá el archivo datosCompletos.csv en el directorio actual
b=[] #crea la lista b vacía
dat=open('datos1.csv') #abre datos1.csv para lectura
a=dat.readlines()#carga todas las líneas en la lista a
dat.close() #cierra datos1
for i in range(len(a)):
    a[i]=a[i].strip('\n') #ojo en el csv no se ve pero en la terminal si, cada \n es cada salto de linea
    a[i]=a[i].split(';')
    print(a[i])
    a[i][3]=int(a[i][3])
#para cada línea de a: saca fin de línea, arma lista separando campos (;), pasa a entero puntaje
#ejemplo  (a[i][3] pasa a ser el puntaje pues es el 4to elemento de c/lista)
b=b+a #agrega a a b #a es la lista q hago con los valores del csv de datos1
dat=open('datos2.csv')
a=dat.readlines()
dat.close()
for i in range(len(a)):
    a[i]=a[i].strip('\n')
    a[i]=a[i].split(';')
    print(a[i])
    a[i][3]=int(a[i][3])
b=b+a
dat=open('datos3.csv')
a=dat.readlines()
dat.close()
for i in range(len(a)):
    a[i]=a[i].strip('\n')
    a[i]=a[i].split(';')
    print(a[i])
    a[i][3]=int(a[i][3])
b=b+a
b.sort(reverse=True,key = lambda b:(b[3],b[2])) #ordena b por puntaje y luego provincia, descendente
for elemento in b:
    print(elemento) #muestra las filas de b
for elemento in b:
    elemento[3]=str(elemento[3])
    ele=';'.join(elemento)+'\n'
    completo.write(ele)
'''
#Ejemplo 1 mejorado
'''Una mejora: Como lo que empleamos para abrir un archivo en la función open() es una string 
que contenga el nombre, podemos editar esa string y automatizar, si cabe, la construcción del
nombre del archivo a abrir'''
'''
completo=open('datosCompletos.csv','w')
b=[]
for j in range(1,4): ##aquiii mejorado
    dat=open('datos'+str(j)+'.csv') #dat tiene un valor distinto xa cada csv
    a=dat.readlines()
    dat.close()
    for i in range(len(a)):
        a[i]=a[i].strip('\n')
        a[i]=a[i].split(';')
        a[i][3]=int(a[i][3])
    b=b+a   #a la lista incial le sumo cada "sublista a=dat.readlines correspondiente a cada archivo"
b.sort(reverse=True,key=lambda b:(b[3],b[2])) #recordar q key manda "filas", es decir, cada lista con nombre prov ciud ptos etc
for elemento in b:             # (puntaje, prov)
    print(elemento)
for elemento in b:  #elemento es cada fila con nombre apel prov y ptos
    elemento[3]=str(elemento[3]) #casteo a str el puntaje
    ele=';'.join(elemento)+'\n' #c/ fila la llamo ele(str), la conformo de cada ele de la fila separado con ; y con un \n al final 
    completo.write(ele) #en el archivo completo escribo la fila q acabo de conformar
completo.close() #cierro completo xa guardar los datos
'''
#Modulo pickle
#pickle.dump() pickle.load()
#Un ejemplo
'''
import pickle

# Podemos guardar lo que queramos, listas, diccionarios, tuplas...
lista = [1,2,3,4,5]

# Escritura en modo binario, vacía el fichero si existe
fichero = open('lista.pickl','wb') #creo el arhivo lista.pckl y lo guardo en el buffereader fichero
#fichero es como una MI q guarda durante la ejecucion del programa lo q hay en el archivo lista.pickl
# Escribe la colección en el fichero

print(fichero) #imprime <_io.BufferedWriter name='lista.pckl'>
print(type(fichero)) #<class '_io.BufferedWriter'>

pickle.dump(lista, fichero)  #meto en fichero la lista lista

fichero.close() #cierro fichero (guardo datos)

# Lectura en modo binario 
buenos_dias = open('lista.pickl','rb') #abro el archivo binario lista.pickl 
# en el bufferedreader buenosdias
# Cargamos los datos del fichero

lista_fichero = pickle.load(buenos_dias) #traigo lo q hay en buenos_dias
print(lista_fichero)        #y lo guardo bajo el alias lista_fichero
#ahora si la puedo imprimir
buenos_dias.close()
'''
#Conclusion modulo pickle, en gral usado en este orden

# random_data_object = lista

# archivo = open('file_name.pickl','operation') -> creacion archivo es un buffereader

# pickle.dump(random_data_objetc, archivo) #carga en archivo, el random..blabla. ojo es un pickle solo python lo sabe leer

# archivo.close() #cierro el archivo xa guardar los datos
# archivo_2 = open (file_name, operation) #abro el archivo en archivo_2

# random_data_object_archivo = pickle.load(archivo_2) -> Cargamos los datos del archivo
# print(random_data_object_archivo)
#archivo_2.close() #cierro xa no perder datos

#otro ejemplo

'''
import pickle

def agrega(l):
    complej=('baja','media','alta')
    nombre=input('Ingrese nombre plato ')
    print('1-',complej[0],'\n2-',complej[1],'\n3-',complej[2])
    c=input()
    while c not in ('1','2','3'):
        c=input()
    plato=[nombre,complej[int(c)-1],[]]
    ingre=input('Ingrediente, * para salir ')
    while ingre!='*':
        plato[2].append(ingre)
        ingre=input('Ingrediente, * para salir ')
    l.append(plato)

def selecciona(l):
    complej=('baja','media','alta')
    print('Selecciona Dificultad')
    print('1-',complej[0],'\n2-',complej[1],'\n3-',complej[2])
    c=input()
    while c not in ('1','2','3'):
        c=input()
    for plato in l:
        if plato[1]==complej[int(c)-1]:
            print(plato)

def menu():
    print('1-Agregar Plato a la Lista\n2-Seleccionar Menúes\n3-Crea/Vacía Lista')
    opcion=input()
    if opcion.isdigit():
        return int(opcion)
    else:
        return 0

opc=menu()
while opc in (1,2,3):
    if opc==1:
        menuTot=open('menus.dat','rb') #abro el archivo menus.dat y lo guardo en el bufferedreader menuTot
        lista=pickle.load(menuTot) #Ahora trabajo con ese Breader, guardo su contenido (nada esta vacio) en lista
        menuTot.close() #cierro el buffereader
        agrega(lista) #le aplico agrega a lista (no puedo hacerselo al bufferedreader)
        menuTot=open('menus.dat','wb') #abro bajo el nombre menutot el archivo
        pickle.dump(lista,menuTot)#y le cargo la lista
        menuTot.close() #lo cierro
    elif opc==2:
        menuTot=open('menus.dat','rb')
        lista=pickle.load(menuTot) #devuelvo lo q hay en menuTot, q es un Breader en lista
        menuTot.close()
        selecciona(lista)
    else:
        menuTot=open('menus.dat','wb')
        pickle.dump([],menuTot) #crea una lista vacia en el archivo menus.dat
        menuTot.close() #q esta en la variable menuTot
    opc=menu()
'''

#Guia de ejs
#Ej 1
'''Cargar un texto extenso de un archivo de texto y generar el resumen de
cantidad de veces que aparece cada palabra del texto en un archivo .csv; donde 
figure palabra y la cantidad de veces que aparece, ordenada de mayor a menor por
cantidad de apariciones en el texto.'''
'''
#OJO hay q tener el archivo parrafo.txt

def limpia(txt):
    txt=txt[:len(txt)-1]
    txt=txt.lower()
    txt=txt.strip()
    for car in txt:
        if car!=' ' and not car.isalpha():
            txt=txt.replace(car,' ')
    return txt

parr=open('parrafo.txt','r')
lineas=parr.readlines()
parr.close()
tabla=[]
for fila in lineas:
    fila=limpia(fila)
    lista=fila.split()
    tabla=tabla+lista #no la appendeo, las uno, qda una sola lista no una lista de listas
palabras=set() #muuuy bicho, al ser un conjunto solo agrega las plbras una sola vezz
for elemento in tabla:
    palabras.add(elemento)
pal=[]
for p in palabras:
    cant=tabla.count(p)
    pal.append([p,str(cant)])
pal.sort(reverse=True,key=lambda pal:pal[1])
total=open('totalPal.csv','w')
for fila in pal:
    linea=';'.join(fila)+'\n'
    total.write(linea)
total.close()
'''
#ej 2
'''Cargar una planilla Excel con dni, apellido, nombre, genero y provincia. Grabarla 
como archivo csv. Levantar el archivo en un programa python que edite los nombres
de provincia, dejándolos a todos en minúsculas, sin acentos y sin caracteres 
extraños (el blanco está aceptado). Generar otro archivo csv (que luego abrirás
en Excel, para hacer un gráfico, por ejemplo) con los nombres de las provincias 
ingresadas y la cantidad total de personas de esa provincia que estaban en la 
planilla original. También contabilizar la cantidad de personas de genero femenino, 
masculino y sin definir y generar un archivo resumen en .csv con estos datos. 
Considerar que la definición de genero puede venir diferente y sucia en cada caso
( Ej: F, femenino, **fem,  masc, m, otro)'''

#OJO! Se necesita datosProv.csv
'''
def limpia(txt,opc):
    txt=txt.lower()
    txt=txt.strip()
    if opc>0:
        txt=txt[:len(txt)-1]
        txt=sinAcento(txt)
    for car in txt:
        if car!=' ' and not car.isalpha():
            txt=txt.replace(car,'*')
    txt=txt.replace('*','')
    return txt

def sinAcento(txt):
    con='áéíóú'
    sin='aeiou'
    dicci=txt.maketrans(con,sin)
    txt=txt.translate(dicci)
    return(txt)

def unifica (txt):
    txt=limpia(txt,0)
    if txt>='f' and txt<'g':
        txt='F'
    elif txt>='m' and txt<'n':
        txt='M'
    else:
        txt='n/d'
    return txt

datos=open('datosProv.csv','r')
personas=datos.readlines()
datos.close()
tabla=[]
for fila in personas: #cada fila son los datos de una persona
    lista=fila.split(';')  #separo segun ; 
    tabla.append(lista) #y agrego ESA LINEA a la lista como una lista
for i in range(len(tabla)): #cada i es una persona
    tabla[i][4]=limpia(tabla[i][4],1) #[i][4] es la provincia 
    tabla[i][3]=unifica(tabla[i][3]) #[i][3] es el genero

#resumen provincias
provincias=set() #conjunto
for fila in tabla:
    provincias.add(fila[4]) #cada fila es una persona, fila[4] es su prov
provin=[]       #como s un conjunto, solo guarda las prov una sola vez
for p in provincias:
    cant=0
    for fila in tabla:  #para cada persona
        if fila[4]==p:  #si su prov es = a la prov q estoy contando,
            cant+=1
    provin.append([p,str(cant)])    #guardo el nombre de cada prov junto con cuantas eprsonas son de ella
provin.sort(reverse=True,key=lambda provin:provin[1]) #ordeno de mayor a menor segun personas x prov   
resumen=open('resumenProv.csv','w') #y aca creo el archivo de provs
for fila in provin:
    linea=';'.join(fila)+'\n'
    resumen.write(linea)
resumen.close()

#resumen generos
generos=[]
tiposSex=set() 
for fila in tabla:
    generos.append(fila[3]) #guardo todos los generos en una fila
    tiposSex.add(fila[3]) # como es un conjunto no se repiten...
generosRes=[]
for tipo in tiposSex: #xa cada genero q se ingreso,
    cant=generos.count(tipo) #cuento, y segun sea...
    if tipo=='F':
        generosRes.append('FEMENINO;'+str(cant)+'\n') 
    elif tipo=='M':
        generosRes.append('MASCULINO;'+str(cant)+'\n')
    else:   #otro
        generosRes.append('Sin Especificar;'+str(cant)+'\n')
genero=open('resumenGenero.csv','w') #creo resumen generos
genero.writelines(generosRes)
genero.close()
'''

#Ej 3
'''
Hacer un programa de carga y mantenimiento de datos de alumnos de un curso (ABM).
De cada alumno se deberá registrar: número de legajo (entero de 6 posiciones), 
apellido (máximo 15), nombre(máximo 15), nota primer parcial, recuperatorio, 
segundo, recuperatorio y examen final.
Ofrecer los siguientes servicios (opciones)
Agregar alumno
Eliminar alumno
Modificar datos personales del alumno
Descargar lista
Cargar nota de alumno
TIP: Hacer un programa aparte que genere el archivo.dat en el directorio donde
estará el programa. Generarlo con una lista vacía.'''

#crea curso.dat
'''
from pickle import dump

print('0- Editar curso')
print('1- Nuevo curso. ¡Cuidado, sobreescribirá y eliminara completamente el anterior!')
nuevo = input()
if nuevo not in ('0','1'):
    nuevo = False
else:
    nuevo = int(nuevo)
if nuevo:
    print('Seguro q quiere borrar la lista completa de alumnos? si/ confirmar otro/menu')
    nuevo = input()
    if nuevo == 'si':
        cursoArch=open('curso.dat','wb') #creo el pickle curso.dat y lo guardo en cursoArch
        dump([],cursoArch) #le cargo una lista
        cursoArch.close() # lo cierro xa guardar cambios

#Ej propiamente dicho
import pickle
def agrega (c):
    legajo=input('Ingresá legajo, 0 para salir  ')
    while len(legajo)>6 or len(legajo)<6 or not(legajo.isdigit()):
        legajo=input('Ingresá legajo, 0 para salir  ')
    while int(legajo)>0:
        apellido=input('Apellido:  ')
        nombre=input('Nombre de %s  '%apellido)
        alumno=[legajo,apellido[:15],nombre[:15],[0,0,0,0,0]]
        c.append(alumno)
        legajo=input('Ingresá legajo, 0 para salir  ')
        while len(legajo)>6 or not(legajo.isdigit()):
            legajo=input('Ingresá legajo, 0 para salir  ')

def elimina(c):
    lista=[] #lista de alumnos (cada alumno es una lista con t/'s sus datos) q deseo eliminar
    legajo=input('Ingresá legajo a eliminar, 0 para salir  ')
    while legajo!='0':
        for i in range(len(c)): #xa la lista de alumnos
            if legajo==c[i][0]: #(si esta EL LEGAJO ver agrega() )
                lista.append(i) #meto en lista TODOS LOS DATOS DE ESE ALUMNO (la lista entera correspondiente a ese legajo)
        legajo=input('Ingresá legajo a eliminar, 0 para salir  ')
    for elem in lista: #xa cada alumno (lista con datos) a eliminar de lista
        c.pop(elem) #lista.pop([índice]) quita de la lista el elemento de la posición índice
        #en este caso, elem es la lista de datos del alumno. ver lista.append(i)

def modifica(c):
    datos='','Apellido','Nombre'
    legajo=input('Ingresá legajo de alumno para modificar datos, 0 para salir  ')
    while legajo!='0':
        posicion=-1
        for i in range(len(c)):
            if legajo==c[i][0]:
                posicion=i #si no encuentra el legajo, esta no se ejecuta
        if posicion>=0:   #solo si encontro el legajo (posicion = i, >0), caso contraio....
            print('1-',c[posicion][1]) #aapellido
            print('2-',c[posicion][2]) #nombre
            print('3-ok')
            opc=input()
            while opc not in ('1','2','3'):
                opc=input()
            if opc!='3':
                dato=input('Ingresá %s  ' %datos[int(opc)]) #datp = apellido /nombre
            c[posicion][int(opc)]=dato[:15] #segun la opc, se modifica apel o nombre
        legajo=input('Ingresá legajo de alumno para modificar datos, 0 para salir  ') #pido legajo de nuevo
    
def cargaNota(c):       #en notas, primer elemento '' xa q imrima todo
    notas='','Primer Parcial','Recuperatorio + Primer Parcial','Segundo Parcial','Recuperatorio Segundo Parcial','Examen'
    legajo=input('Ingresá legajo de alumno para carga de nota, 0 para salir  ')
    while legajo!='0':
        lista=[]
        for i in range(len(c)): #xa cada alumno en curso
            if legajo==c[i][0]: #el legajo de un alumno
                lista=c[i] #guardo en lista la lista con todos los dayos del alumno c[i][0]
                lista.append(i) #agrego a lista un elemento mas, q es la pos del alumno en la lista curso (i)
        if len(lista)>0:
            for i in range (1,6):
                print(str(i),notas[i],lista[3][i-1])
            print('6-ok')
            opc=input()
            while opc not in ('1','2','3','4','5','6'):
                opc=input()
            if opc!='6':
                notaNueva=float(input('Ingresá nota de %s  ' %notas[int(opc)]))
                while notaNueva<=0:
                    notaNueva=float(input('Ingresá nota de %s  ' %notas[int(opc)]))
                lista[3][int(opc)-1] = notaNueva #recordar q en lista agregue al alumno completo correspondiente al padron q ingrese
                posicion=lista[4] #guardo la posicion del alumno en la lista curso (ver lista.append(i)) xa dsps poder agregarlo correctamente
                lista.pop() #saca el ultimo elemnto de la lista, en este caso la posicon del alumno en la lista curso
                c[posicion]=lista #una vez sacado el ele posicion de lista, agrego el alumno con la nueva nota cargada (q esta en lista)
        legajo=input('Ingresá legajo de alumno para carga de nota, 0 para salir  ')
    
def menu():
    print('0- Salir y mostrar lista de alumnos')
    print('1- Agrega Alumno')
    print('2- Elimina Alumno')
    print('3- Modifica Datos Personales')
    print('4- Carga de Nota')
    print('5- Vacía la Lista')
    opc=input()
    if opc not in ('1','2','3','4','5'):
        opc='0'
    return int(opc)

cursoArch = open('curso.dat','rb')
curso = pickle.load(cursoArch) #cargo el contenido (x ahora lista vacia) de cursoarch en la var curso
cursoArch.close()
print('Alumnos')
print(curso) #lista vacia (la primera vuelta dsps ya no)
opc=menu()
while opc!=0:
    if opc==1:
        agrega(curso)
    elif opc==2:
        elimina(curso)
    elif opc==3:
        modifica(curso)
    elif opc==4:
        cargaNota(curso)
    else:
        curso=[]
        cursoArch=open('curso.dat','wb') #creo el archivo curso.dat
        pickle.dump(curso,cursoArch) #carga la lista vacia curso en cursoArch (vacia la lista n casi de q exista xq la sobreescribe)
        cursoArch.close() #save
    opc=menu()
print('Alumnos')
print(curso)
cursoArch=open('curso.dat','wb')
pickle.dump(curso,cursoArch) #carga la lista curso en cursoArch (archivo curso.dat)
cursoArch.close() #lo salva
'''