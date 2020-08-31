#Descripción: El programa muestra el funcionamiento de los botones que posee la placa. Cuando el programa recien empieza muestra en el display la imagen de una "carita triste", cuando se 
#presiona el botón A la imagen se cambia por la imagen de una "carita feliz". Cuando el botón B es presionado el programa termina.

#Código:

#Se importa la respectiva librería
from microbit import *   
while True:
    if button_a.is_pressed():     # Cuando el botón A es presionado
        display.show(Image.HAPPY) # Se muestra una carita feliz
    elif button_b.is_pressed():   # Cuando el botón B es presionado
        break                    # El programa se cambia la condición del bucle, terminando su ejecución               
    else:
        display.show(Image.SAD)   # Se muestra una carita triste
# Al final se limpia el display apagando todos los leds
display.clear()
