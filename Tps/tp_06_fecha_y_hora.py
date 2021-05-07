#EXTRA: FECHA Y HORA

#Módulo datetime
'''
import datetime     
hora=datetime.time(1,2,3) #la clase es time y tiene atributos
print(hora)
print('hora:', hora.hour.) #hour es un atributo de hora
print('minutos:',hora.minute)
print('segundos:',hora.second)
print('microsegundos:',hora.microsecond)
print('tzinfo:',hora.tzinfo)
'''
#Valores maximos y minimos
'''
import datetime
print('Más Temprano:',datetime.time.min)
print('Más Tarde:',datetime.time.max)
print('Unidad Mínima de Tiempo:',datetime.time.resolution)
'''
#TODAYS DATE, con .datetime.date.today()
'''
import datetime 
hoy=datetime.date.today()
print(hoy)
print('ctime  :', hoy.ctime())#tipo de formato de fecha
hTup =hoy.timetuple() # se obtiene tupla con los datos de la fecha
print('tupla  : tm_year  =', hTup.tm_year)
print('         tm_month =', hTup.tm_mon)
print('         tm_day  =', hTup.tm_mday)
print('         tm_hour  =', hTup.tm_hour)
print('         tm_min   =', hTup.tm_min)
print('         tm_sec   =', hTup.tm_sec)
print('         tm_week day nº =', hTup.tm_wday)# lunes 0, martes 1 ...
print('     tm_year number day  =', hTup.tm_yday)
print('ordinal:', hoy.toordinal()) #número de la fecha en el Calendario Gregoriano
print('Year   :', hoy.year)
print('Mon    :', hoy.month)
print('Day    :', hoy.day)
'''
#Valores maximos de fecha
'''
import datetime
print('Lo más Temprano:',datetime.date.min)
print('Lo más Tarde:',datetime.date.max)
print('Resolución:',datetime.date.resolution)
'''
'''timedelta
Fechas futuras y pasadas pueden calcularse usando aritmética básica 
en dos objetosdatetime, o combinandodatetimecon untimedelta. Restar fechas produce 
untimedelta, y untimedeltase puede agregar o restar de una fecha para producir otra fecha. 
Los valores internos para untimedeltason almacenados en días, segundos y microsegundos
'''
'''
from datetime import time,datetime 
llamados=[]
horarios=[]
print('Ingresá llamados, 0 para salir')
num=input('Tel ') 
while int(num)!=0:
    hora=input('hh:mm ') #ingreso hora
    tiempo=hora.split(':') #la spliteo, en una lista de elementos,
    h=int(tiempo[0]) #el 1ero la hora
    m=int(tiempo[1]) #y el 2do los minutos
    if num in llamados:  #si ya llamó este numero,
        pos=llamados.index(num) #pos=la poscion del numero num
        horarios[pos].append( (h,m) ) #En la posicion 'pos' de la lista horarios
    else:                          #agrega la tupla (h, m)
        llamados.append(num)       #Van a estar guardados en posciones iguales n listas distintas 
        horarios.append([ (h,m) ]) 
    num=input('Tel ') 
for i in range(len(llamados)): 
    print(llamados[i],end=': ') 
    for hora in horarios[i]: #horarios[i] = tupla (h,m) 
        print(time(hora[0],hora[1]),end=' ')
                 #(  h    , m     )
    primero=min(horarios[i]) 
    ultimo=max(horarios[i]) 
    hUlt=datetime(1,1,1,ultimo[0],ultimo[1])
    hPri=datetime(1,1,1,primero[0],primero[1])
    dif=hUlt-hPri 
    print('Período Transcurrido:',dif)
'''
#Este programate calcula una edad con precisión a días a partir de la fecha de nacimiento:
#datetime.now(): fecha actual con hora
'''
from datetime import datetime,timedelta
hoy=datetime.now() #guardo en hoy la fecha y hora actual
dia=int(input('Ingresá día de nacimiento (dd)  '))
while dia not in range (1,32):
    dia=int(input('Ingresá día de nacimiento (dd)  '))
mes=int(input('Ingresá mes de nacimiento (mm)  '))
while (dia==31 and mes in (4,6,9,11)) or (dia>28 and mes==2)or(mes not in range(1,13)):
    mes=int(input('Ingresá mes de nacimiento (mm)  '))
anio=int(input('Ingresá Año de nacimineto(aaaa)  '))
while anio<0 or anio>hoy.year:
    anio=int(input('Ingresá Año de nacimineto(aaaa)  '))
nacimiento=datetime(anio,mes,dia) #arma un string con los 3 parametros
print('Fecha de nacimiento:', nacimiento)   #si agrego mas parametros, corresponden a la hora min y seg
diferencia=hoy-nacimiento
dias=int(diferencia.days)
print('Naciste hace', dias, 'días')
a=int(dias/365.25)
resto=dias-(a*365.25)
m=int(resto/30.41)
d=int(resto-(30.41*m))
print('pasaron',a,'años',m,'meses',d,'días')
'''
#Selecciona personas en una franja etárea de una lista:
'''
from datetime import datetime,timedelta
from random import randint,choice
nombres=('Ana','Juan','Manuel','Analìa','Inés','Isabel', 'Ignacio','Joaquín')
fechNcmt=[]
hoy=datetime.now()
for i in range(35):
    nom=choice(nombres)
    anio=randint(1990,hoy.year)
    if anio==hoy.year:
        mes=randint(1,hoy.month)
    else:mes=randint(1,12)
    if mes in (1,3,5,7,8,10,12):
        dia=randint(1,31)
    elif mes==2:
        if (anio%100==0 and anio%400==0)or(anio%100!=0 and anio%4==0):
            dia=randint(1,29)
        else:dia=randint(1,28)
    else:
        dia=randint(1,30)
    fechNcmt.append([nom,datetime(anio,mes,dia)]) #por cada persona agrego a fechNcmt una lista con[(nombre, fecha de nacimiento)]
desde=int(input('Ingresá franja etárea en años, desde (0-120):  ')) #cada persona es una lista
hasta=int(input('Ingresá franja etárea en años, hasta (0-120):  '))
for persona in fechNcmt:
    dif=hoy-persona[1] #persona[1]=datetime(anio, mes,dia), corresponde a la fecha de nacimiento de nom 
    if int(dif.days/365.25) in range(desde,hasta+1):
        print(persona[0],'  ',persona[1].year,'-',persona[1].month,'-',persona[1].day,'  ',int(dif.days/365.25),sep='')
                #nombre         fecha de nacimiento
'''