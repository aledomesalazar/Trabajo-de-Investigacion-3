#Descripción: El programa muestra el funcionamiento del sensor de temperatura que viene incorporado en la placa. Como se utiliza un simulador y no una placa física, el simulador presenta 
#un rango de temperaturas para simular el comportamiento de este componente. El programa muestra en el display el valor de la temperatura que el sensor esta midiendo de forma indefinida.

#Código:

#Se importa la librería microbit para utilizar la placa Micro:bit
from microbit import *
while True:
   #se guarda la temperatura en la variable temp
   temp = temperature()                              
 
   #Se usa str() para convertir el valor de temperatura en texto, con la finalidad de mostrarlo en el display.
   display.scroll(str(temp)+'°C')
 
   #Se añade medio segundo de espera para no leer continuamente la temperatura
   sleep(500)
