'''Realizar un programa en PYTHON que permita generar un “tablero” de números de 25x25 
conteniendo una serie aritmética en la triangular inferior de la diagonal secundaria y 0s 
en la otra triangular. La salida deberá verse así:'''

l1 = []
for i in range(25):
  l1.append([])
for i in range(25):
  l1[i]=['']*25

cont=1
for i in range(25):
    for j in range(25):
        if j<24-i:
            l1[i][j]=0
        else:
            l1[i][j]=cont
            cont+=1

for i in range(25):
    for j in range(25):
        print(str(l1[i][j]).rjust(3), end='')
    print()