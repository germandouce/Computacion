'''Realizar un programa en PYTHON que permita generar aleatoriamente 50 números  enteros entre 
-500 y 500 inclusive. El programa deberá mostrar la lista de los negativos primero y luego 
la de los positivos. La cantidad de veces que salió el 0 y la cantidad de números no repetidos 
que se generaron.
Ej:
Números Negativos
-150 -418 -136 -173 -79 -247 -352 -30 -263 -196 -454 -246 -166 -97 -87 -306 
-127 -403 -115 -362 -418 -326 -142 -465 -494 -444 -327 -160 -63 -135 -83 -410 
Números Positivos
489 241 80 393 240 179 122 143 149 78 207 70 484 470 222 43 200 252 
Cero vino 0 veces
Vinieron 49 números diferentes
'''

#lo comentado fue útil para corroborar resultado

import random
l1=[]
lneg=[]
lpos=[]
cero=0
dif=0
for i in range(50):
    num=random.randint(-500,500)
    l1.append(num)
for num in l1:
    if num<0:
        lneg.append(num)
    elif num >0:
        lpos.append(num)
    else:
        cero+=1
    if l1.count(num)==1:
        dif+=1
    #else:
    #    print(num)
#print('lista 1')
#print(l1)
print('Números negativos: ')
print(lneg)
print()
print('Números positivos:')
print(lpos)
print()
print('Cero vino',cero,'veces')
print('Vinieron', dif, 'numeros diferentes')
