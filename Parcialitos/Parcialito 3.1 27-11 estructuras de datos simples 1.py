'''Realizar un programa en PYTHON que permita leer un texto de no más de 100 
caracteres y luego una palabra de longitud máxima 15. Se deberán eliminar en el 
primer texto todas las ocurrencias de los caracteres que estén en la palabra ingresada 
en segundo término. Salvo que el carácter aparezca una única vez en el texto inicial.  
Eliminar además, blancos innecesarios.
Ej:
Ingrese un texto, máximo 100 caracteres   La práctica de la PACIENCIA     Y LA   CONCORDIA son actitudes vitales en el gobierno de LOS ESTAdos Naciones, a lo largo   de todo el Planeta.
Ingrese palabra de eliminación, máximo 15 caracteres  viáTIco
Palabra de Eliminación
viáTIco
Texto Resultante
La práta de la PACENCA Y LA CONCORDA sn attudes vtales en el gbern de LOS ESTAds'''


txt=input('ingrese un texto, máximo 100 cracteres: ')
txt=txt[0:100]
#txt=txt.strip()   #si se considera el espacio inicial como espacio innecesario
word=input('ingrese palabra de eliminación, máximo 15 caracteres: ')
word=word[0:15]
for car in word:
    if txt.count(car)>1:
        txt=txt.replace(car,'')   
while txt.count('  ')>0:      
    txt=txt.replace('  ',' ')
print('Palabra de Eliminacion: ')
print(word)
print('Texto Resultante: ')
print(txt)