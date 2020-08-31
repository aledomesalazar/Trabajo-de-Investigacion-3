from microbit import *   
while True:
    compass.calibrate()                                    # Calibra la brújula
    display.show("Hola")                                   # Saludos y preguntas
    display.scroll("¿Te hacemos algunas preguntas?")
    display.scroll("A afirma, B niegas")
    sleep(1000)                                            # Tiempo para decidir
    if button_a.was_pressed():     
        display.scroll("¿Temperatura? A/B")                # Para la temperatura
        if button_a.was_pressed(): 
          temp = temperature()
          display.scroll(str(temp)+'°C')
          sleep(500)
        display.scroll("¿Orientación? A/B")                # Para el sensor de brújula
        if button_a.was_pressed(): 
          display.scroll(str(compass.heading()))         
        display.scroll("Adivina la figura")                # Para la figura
        display.show("5")
        sleep(2500)
        display.scroll("¿Número 5? (A)", delay = 500)
        display.scroll("¿Letra s? (B)", delay = 500)
        sleep(3000)                                        # Tiempo para decidir
        if button_a.was_pressed():
          display.scroll("Correcto")
        elif button_b.was_pressed():
          display.scroll("Incorrecto")
        display.scroll("¿Acelerómetro? A/B")               # Para el sensor de brújula
        if button_a.was_pressed():
          if microbit.accelerometer.is_gesture('shake'):
            display.scroll("Se agitó")
          else:
            display.scroll("No se agitó")
        display.scroll("Muchas gracias")
    elif button_b.was_pressed():   
        display.scroll("Muchas gracias")
        break                                    
    else:
        display.scroll("Se agotó el tiempo de espera")   
# Al final se limpia el display apagando todos los leds
display.clear()
