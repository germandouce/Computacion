'''Realizar un programa en PYTHON que pida dos textos y determine cuál de ellos tiene 
menos palabras; dejando al que más tiene con la misma cantidad de palabras del que menos 
tiene. Se espera que se conserven las n primeras.
Ej:
Ingrese primer texto:  LA CALMA QUE precede a la tempestad está en ciernes, no es cierto?
Ingrese segundo texto:  MEJOR tarde que nunca!!!
Textos Resultantes
La calma que precede 
Originalmente 13 palabras
Mejor tarde que nunca 
Originalmente 4 palabras'''

txt1=txt1=input('Ingrese primer texto:  ').strip().lower()
txt2=txt2=input('Ingrese segundo texto:  ').strip().lower()
for car in txt1:
    if not car.isalpha() and not car.isspace(): #si no es alphanumerico o un espacio
        txt1=txt1.replace(car,' ') #ese caracter reemplazalo por un espacio
for car in txt2:
    if not car.isalpha() and not car.isspace():
        txt2=txt2.replace(car,' ')
lis1=txt1.split()
lis2=txt2.split()
cp1=len(lis1)
cp2=len(lis2)
if cp1>cp2:
    lis1=lis1[:cp2]
else:
    lis2=lis2[:cp1]
print('Textos Resultantes')
print(' '.join(lis1).capitalize(),'\nOriginalmente',cp1,'palabras')
print(' '.join(lis2).capitalize(),'\nOriginalmente',cp2,'palabras')


#con CARACTERES (en vez de palabras)
'''
l1=[]
l2=[]
txt1=input('inrese primer texto: ').strip()
txt2=input('ingrese segundo texto: ').strip()
for ele in txt1:
    l1.append(ele)
#print(l1)
for ele in txt2:
    l2.append(ele)
#print(l2)
if len(txt1) < len(txt2):
    l2=l2[:len(l1)]
else:
    l1=l1[:len(l2)]
print('textos resultantes')
for ele in l1:
    print(ele, end='')
print()
print('orignalmente de', len(txt1),' caracteres')
for ele in l2:
    print(ele, end='')
print()
print('originalmente de', len(txt2),'caracteres')
'''