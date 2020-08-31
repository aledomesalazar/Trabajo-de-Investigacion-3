#Descripción: El programa muestra el funcionamiento de una "Bola 8" a través de la utilizacion de la función "shake" del acelerómetro de la placa. Cuando se inicie el programa aparecerá 
#en el display de la placa la imagen del número 8, cuando se selecciona la función "shake" del acelerómetro se visualizará, de forma aleatoria, una de las respuestas que se encuentran en 
#el arreglo "answers".

#Código:

# Se importa la respectiva librería
from microbit import *   
# Librería para generar datos aleatorios
import random            

# Se le asigna una la variable answer una matriz con todas las posibles respuestas que puede tomar.
answers = [
    "Es cierto",
    "Es decididamente así",
    "Sin duda",
    "Sí, definitivamente",
    "Puedes confiar en ello",
    "Como yo lo veo, sí",
    "Más probable",
    "Buena perspectiva",
    "Sí",
    "Las señales apuntan que sí",
    "Respuesta confusa, intenta otra vez",
    "Pregúntamelo después",
    "Mejor no te lo digo ahora",
    "No puedo predecir ahora",
    "Concéntrate y pregunta otra vez",
    "No cuentes con ello",
    "Mi respuesta es que no",
    "Las señales dicen que no",
    "No hay buena perspectiva",
    "Muy dudoso",
]
 
while True:
  # Mientras no se utilice la función shake del acelerómetro de monstrará un ocho en el display
    display.show('8')
    #Cuando se utilice la función shake del acelerometro se limpiará la pantalla y se seleccionará una de las respuestas asignadas a la variable answer de forma aleatoria. 
    #Para esta luego ser mostrada en el display.
    if accelerometer.was_gesture('shake'):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
    sleep(10)
