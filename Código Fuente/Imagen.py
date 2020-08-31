
#Descripción: El programa describe el funcionamiento de los leds en el display de la placa. Además de mostrar el funcionamiento de la luminosidad de cada uno de ellos a traves de la 
#realización de gráfico de un barco utilizando la caracteristica de la luminosidad''

#Código:
#Se importa la respectiva librería
from microbit import *  
#La matriz representa el display de forma que cada led es independiente y se le puede asignar el valor de luminosidad que se desee dentro de un rango de 0 a 9
boat = Image("05050:"  # Se asigna el valor de la imagen a una variable 
             "05050:" 
             "05050:" 
             "99999:"
             "09990")
# Visualizamos la matriz en la placa
display.show(boat) 
