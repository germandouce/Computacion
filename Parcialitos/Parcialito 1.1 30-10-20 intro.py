'''Hacer un programa que ingrese un número entero de cuatro cifras y obtenga la diferencia entre la suma de las cifras de los extremos y la suma de las cifras de los dígitos internos. Luego obtenga el número de cuatro cifras formado por los complementos a 10 de los dígitos del número leído.
Ej:
Ingrese número de 4 cifras: 1228
(1+8)-(2+2)=5
Compl(1228)=9882

Ingrese número de 4 cifras: 4512
(4+2)-(5+1)=0
Compl(4512)=6598'''

num1= int(input('Ingrese un numero de 4 cifras: ')) #4 cifras x y z k
num=num1

d1 = num//1000      #primer cifra x
num = num%1000      #redefino el numero me queda solo y z k
d2 = num//100       #segunda cifra y
num = num%100       #redefino me queda z k
d3 = num//10        #tercera cifra z
d4 = num%10         #cuarta cifra k, resto de la division por 10

operacion = (d1+d4)-(d2+d3)
print('(',d1,'+', d4,')','-','(',d2,'+',d3,')','=',operacion) 

c1 = 10-d1          #obtengo cx  
c2 = 10-d2          #obtengo cy 
c3 = 10-d3          #obtengo cz
c4 = 10-d4          #obtengo ck         

print ('compl','(',num1,')','=','%i%i%i%i'  %(c1, c2, c3, c4))

#alternativa para complemento (falla en casos con ceros)
'''
c1 = (10-d1)*1000   #obtengo cx 0  0  0 
c2 = (10-d2)*100    #obtengo 0  cy 0  0 
c3 = (10-d3)*10     #obtengo 0  0  cz 0
c4 = (10-d4)*1      #obtengo 0  0  0  ck

compl = (c1 + c2 + c3 + c4)
print (compl)
'''

