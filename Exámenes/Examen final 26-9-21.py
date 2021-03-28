#Evaluación Final                                                       26 de marzo de 2021
'''El siguiente programa falla al realizar la salida esperada'''

def menu(s):
   for i in range(len(s)): ## error 1 mal range()
      print(i+1,'-',s[i],sep='') #error 2 mal numeracion
   print('0-Salir')
   opc=int(input())
   while opc not in range(len(s)+1): #error 3
      opc=int(input())  #(  5   + 1) -> 0,1,2,3,4,5
   return opc                 #6

def muestra(v,s):
   print('Ventas por Sucursal')
   for suc in v:
      print(suc[0][:12].ljust(12),end=' ')   #error 5 ljust(12)
      vent=suc[1:]                                        #error 4:
      vent.sort(key= lambda vent: (meses.index(vent[0]))) #para q ordene por mes (me costo)
      for i in range(len(vent)):
         print((vent[i][0]),':',vent[i][1],sep='',end=', ')
      print('***')

   
sucursal=('La Plata','CABA','San Fernando','Escobar','Pilar')
meses=('','ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic')
ventas=[]
print('Ingreso de Ventas por Sucursal, termina con 0')
suc=menu(sucursal)
while suc!=0:
   vtasSuc=[sucursal[suc-1]]  #error 3 para q coincida
   print('Ingresá ventas por mes (1-12), 0 para salir')
   mes=int(input('Mes: '))
   while mes not in range(13):
      mes=int(input('Mes: '))
   while mes!=0:
      tot=int(input('Total Vtas: '))
      while tot<0:
         tot=int(input('Total Vtas: '))
      vtasSuc.append((meses[mes],tot))
      mes=int(input('Mes: '))
      while mes not in range(13):
         mes=int(input('Mes: '))
   ventas.append(vtasSuc)
   suc=menu(sucursal)
muestra(ventas,sucursal)

'''
Para el siguiente ingreso:

Ingreso de Ventas por Sucursal, termina con 0
1-La Plata
2-CABA
3-San Fernando
4-Escobar
5-Pilar
0-Salir
3
Ingresá ventas por mes (1-12), 0 para salir
Mes: 9
Total Vtas: 23
Mes: 10
Total Vtas: 87
Mes: 0
1-La Plata
2-CABA
3-San Fernando
4-Escobar
5-Pilar
0-Salir
2
Ingresá ventas por mes (1-12), 0 para salir
Mes: 12
Total Vtas: 897
Mes: 11
Total Vtas: 33
Mes: 8
Total Vtas: 2
Mes: 0
1-La Plata
2-CABA
3-San Fernando
4-Escobar
5-Pilar
0-Salir
0

Debería producir:

Ventas por Sucursal
San Fernando sep:23, oct:87, ***
CABA ago:2, nov:33, dic:897, ***
>>>>>>

Y no lo consigue
Modificá el mismo para que produzca el resultado esperado
'''