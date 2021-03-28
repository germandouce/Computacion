'''Solicitar la altura para dibujar la siguiente figura.
Ej:
Altura=5
*           *
    *    *
       *
    *    *
*            *
Altura=7
*               *
   *         *
      *   *
         *
      *   *
   *         *
*               *
Nota: La altura y la base miden igual
Altura=3
*		*
	*	
*		*
'''
alto=int(input('Ingrese alto del cuadrado (debe ser impar y entre 3 - 19): '))
while not(alto%2)or alto not in range(3,20):
    alto=int(input('Ingrese alto del cuadrado (debe ser impar y entre 3 - 19): '))
for i in range(alto):
    for j in range(alto):
        if j==i or j==alto-1-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
exit()
