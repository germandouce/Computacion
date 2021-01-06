#JUEGO  DE  BATALLA  NAVAL - SALVO 
#tablero 10x10 - 15 barcos - 60 turnos- desde terminal
#sentidos (4): < > ^ v 
'''
Cantidad de barcos    Cantidad de posiciones 
        5          de           1 
        4          de           2
        3          de           3  
        2          de           4 
        1          de           5                        
tiros correctos para ganar: 35
'''
print('BATALLA NAVAL\n')
import random
orientacion=(0,1,2,3)
l1 = []
for i in range(10):
  l1.append([])
for i in range(10):
  l1[i]=[' ']*10
sentido=0
fila=0
colum=0
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
cont=0
tiros=set()
tiros4user=set()
while (cont<60)and len(tiros)<35:
  fila=0
  while (fila<1)or(fila>10):
    fila=int(input('Ingrese fila: '))
  columna=0  
  while (columna<1)or(columna>10):
    columna=int(input('Ingrese columna: '))
  if l1[fila-1][columna-1]=='*':
    print('TOCADO')
    tiros.add((fila-1,columna-1))
    tiros4user.add((fila,columna))
  else:
    print('AGUA')
  cont+=1
  print('tiraste:',tiros4user) 
  print('te quedan bajar:',35-len(tiros))
  print('tiros restantes:',60-cont)
  print()
if len(tiros)<35:
  print('PERDISTE EL JUEGO!!!')
else:
  print('GANASTE EL JUEGO!!!')