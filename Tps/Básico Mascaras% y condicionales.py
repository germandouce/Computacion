'''
Las mascaras sirven para "llamar" el contenido de una variable dentro de 
un print o un input cuando la operacion esta hecha dentro de la misma funcion. la sintax es 
%s' %variablecuyocontenidollamo (en vez de 's' va a 'f' si es un float e 'i' si es un entero)
5f%' %variablecuyocontenidolllamo (el 4 mete 4 espacios CONTADOS DDE INICIO DEL RENGLON
adelante la variable osea que (ver verde) si la variable ocupa menos no le cambia nada
representa que es float)
%6.2 el 6 es el total que ocupa el numero original. el .2 redondea el numero a 2 posicones
'''
#la cantidad de espacio total que se acompaña a la máscara sólo
# importa si el número ocupa menos, satura con blancos
# cuando se fijan posiciones decimales se redondea
# el número antes del punto con formato f es el total que ocupa, no la parte entera
'''
a=3
b=33333
d=3.89999
nom=input('Ingrese nombre %3i: '%a)
desc=input('Ingresá artículo de precio %7.3f  '%d) #aprox 3 decimales y el 7 no entiendo
print('%5d'%a)
print('%6d'%b) #aca x ej. le meti 6 spaces but la variable ocupa 5 tonces lo mueve solo 1
print('%.2f'%d) #apoxima el numero a 2 decimales
exit()
'''
#condiconales 
#ej practica clase
'''
Ahora imaginemos que en la empresa se abona un plus fijo de guardería a todo trabajador que 
tiene hijos. Y se le paga un 10% de incentivo a todo trabajador que haya hecho más de 30 horas 
y noreciba el plus por guardería.
'''
#opcion 1
'''
cantHoras=int(input('Ingrese la cantidad de horas trabajadas: '))
valorHora=float(input('Ingrese valor de la hora de trabajo: '))
hijos=int(input('Tiene hijos? (1-Si; 0-No): '))
if (hijos==0)and(cantHoras>=30):
    print('Debe cobrar %.2f'%(cantHoras*valorHora*1.1))

if hijos==1:
    plusFijo=float(input('Ingrese adicional guardería: '))
    print('Debe cobrar %.2f'%(cantHoras*valorHora+plusFijo))

if (hijos!=1)and(cantHoras<30):
    print('Debe cobrar %.2f'%(cantHoras*valorHora))
exit()
'''
#opcion 2
'''
cantHoras=int(input('Ingrese la cantidad de horas trabajadas: '))
valorHora=float(input('Ingrese valor de la hora de trabajo: '))
hijos=int(input('Tiene hijos? (1-Si; 0-No): '))
total=cantHoras*valorHora
if hijos==1:
    plusFijo=float(input('Ingrese adicional fijo por hijos: '))
    total=total+plusFijo
elif cantHoras>29:
    total=total*1.1
print('Debe cobrar %.2f'%total)
exit()
'''