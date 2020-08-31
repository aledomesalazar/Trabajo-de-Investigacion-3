#Descripción: El programa muestra el funcionamiento de la brújula incorporada en la placa. El programa muestra la posición en la que se encuentra la brújula a través del display, luego de
#haber calibrado la brújula previamente. 

#Código:

#Se importa la librería microbit para utilizar la placa Micro:bit
from microbit import *
#Se calibra la brújula
compass.calibrate()
while True:
    if button_a.was_pressed():
      #Cuando se presiona el botón A se muestra en el display la posición en la que se encuentra utilizando la función heading()
        display.scroll(str(compass.heading()))
