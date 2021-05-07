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
            if legajo==c[i][0]: #( si esta EL LEGAJO ver agrega() )
                lista.append(i) #meto en lista TODOS LOS DATOS DE ESE ALUMNO (la lista entera correspondiente a ese legajo)
        legajo=input('Ingresá legajo a eliminar, 0 para salir  ')
    for elem in lista: #xa cada alumno (lista con datos) a eliminar de lista
        c.pop(elem) #lista.pop([índice]) quita de la lista el elemento de la posición índice
        #en este caso, elem es la lista de datos del alumnos

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
