#Descripción: El programa muestra el funcionamiento de la aplicación Music de la placa. El programa reproduce dos tonalidades diferentes, reproduce la primera cuando el botón A es presionado
#y la segunda es reproducida cuando el botón B es presionado.
#NOTA: ESTE PROGRAMA DEBE SER EJECUTADO EN LA PÁGINA WEB makecode.microbit.org

#Código:

while True:
    if input.button_is_pressed(Button.A):
        music.set_volume(50)
        music.play_melody("E D G F B A C5 B ", 200)
    if input.button_is_pressed(Button.B):
        music.set_volume(50)
        music.play_melody("E B C5 A B G A F ", 200)
