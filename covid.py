import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import time
from datetime import datetime, timedelta, date, time
import matplotlib.pyplot as plt

infile='CONVENIENT_global_deaths.csv'
#infile='CONVENIENT_global_confirmed_cases.csv'
pais=sys.argv[1]
fecha1=sys.argv[2]
fecha2=sys.argv[3]
dias=sys.argv[4]
pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)

"""datatime=datetime.strptime(fecha1,'%m/%d/%y')
mes=datatime.month
dia=datatime.day
anio=datatime.year"""
death=[]
fechas1=[]
fechas2=[]
death2=[]
datatime=datetime.strptime(fecha1,'%m/%d/%y')
datatime2=datetime.strptime(fecha2,'%m/%d/%y')
for i in range(0,int(dias)):
    mes=datatime.month
    dia=datatime.day
    anio=datatime.year
    fecha=str(mes)+'/'+str(dia)+'/'+str(anio)[-2:]
    fechas1.append(fecha)
    ola1=data[data['Country/Region']==fecha][pais]

    mes=datatime2.month
    dia=datatime2.day
    anio=datatime2.year
    fecha2=str(mes)+'/'+str(dia)+'/'+str(anio)[-2:]
    fechas2.append(fecha2)
    ola2=data[data['Country/Region']==fecha2][pais]
    #print(fecha)
    #print(fecha,ola1)
    datatime=datatime+timedelta(1)
    datatime2=datatime2+timedelta(1)
    death.append(int(ola1.values))
    death2.append(int(ola2.values))

Olas1={'Fechas':fechas1,'Muertos':death}  
Olas2={'Fecha':fechas2,'Muertos':death2}
df=DataFrame(Olas1,columns=['Fechas','Muertos']) 
print(df)

#plt.subplot(1,2,1)
df.plot(x='Fechas',y='Muertos',kind='bar',color='c')
#plt.plot(df['Muertos'],color='c')
plt.title(pais)
plt.show()

dg=DataFrame(Olas2,columns=['Fecha','Muertos']) 
print(dg)
#plt.subplot(1,2,2)
dg.plot(x='Fecha',y='Muertos',kind='bar',color='r')
#plt.plot(dg['Muertos'])
plt.title(pais)
plt.show()
