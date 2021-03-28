'''Realizar un programa en PYTHON que permita cargar datos de personas. Para cada una de ellas 
se solicitará nombre, apellido y año de ingreso. El final vendrá indicado por *. El año de 
ingreso debe circunscribirse al período 2000-2010. Informar cuál es el más antiguo y luego 
mostrar también la lista de datos ingresados.'''

lista=[]
nom=input('Ingrese Nombre, * para salir  ')
while nom!='*':
    apel=input('Ingrese apellido de %s  ' %nom)
    anioIngreso=int(input('Ingresá Año de ingreso de %s %s (2000-2010)'%(nom,apel)))
    while anioIngreso not in range(2000,2011):
        anioIngreso=int(input('Ingresá Año de ingreso de %s %s (2000-2010) '%(nom,apel)))
    lista.append([nom,apel,anioIngreso])
    nom=input('Ingrese Nombre, * para salir  ')
#print(lista)
berres=[]
for n in lista:
    n=list(reversed(n)) # invierte c/ ele de la lista (c/u es una li con 3 datos)
    #print(n)
    berres.append(n) #agrega en berres la l's al reves
    #print(berres)
antiguo=min(berres) #antiguo es la lista q tiene el menor año (Ver EXTRA xa ver como funciona min)
print(antiguo) #imprimo la lista q tiene el menor año
print('El más Antiguo es:',antiguo[2],antiguo[1],'que ingresó en el año',antiguo[0])
for n in lista:           #nombre,       apel (recordar  q inverti cada lista)
    print(*n)   #imprimo cada lista (datos de una persona) de la lista

#EXTRA
#funcionamiento de func min al comparar listas o tuplas
#en una sola lista
#con numericos
'''l1=[9,9,12,5,67,32,0,-3]
print(min(l1))'''
#con strings
'''
l1=['ha','hi']
print('h',ord('h'))
print('i',ord('i'))
print('a',ord('a'))

print(min(l1))
'''
#notar q comparara el ascii de cada letra del primer ele con la 1era del 1do ele. cuando 
#coinciden desempatan con la sig (en este caso, h's coinciden, desempata a (97)<i(105))

#con 2 listas
'''
ltot=[]
l1=[13,'ha',32]
l2=[13,'ha',92]
l3=[13,'hi',0]

ltot.append(l2)     
ltot.append(l1)
ltot.append(l3)

print(ltot)             #Compara el primer elemento de cada lista
print('min',min(ltot))    #si coincide se fija el segundo y asi etc
print('max',max(ltot))     #recordar q con los strings compara ascii letra a letra (a<i)
'''
#con tuplas (compaara igual q con listas)
'''
ltot=[]
l1=(13,'ha',32)
l2=(13,'ha',92)
l3=(13,'hi',0)

ltot.append(l2)     
ltot.append(l1)
ltot.append(l3)

print(ltot)             #Compara el primer elemento de cada tupla
print('min',min(ltot))    #si coincide se fija el segundo y asi etc
print('max',max(ltot))     #recordar q con los strings compara ascii letra a letra (a<i)
'''
