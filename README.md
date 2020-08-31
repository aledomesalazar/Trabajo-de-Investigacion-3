## Trabajo-de-Investigacion - Tercer-Parcial
### Desarrollo de aplicaciones para el control del hardware de la placa Micro bit en https://create.withcode.uk/ con: Imágenes, Botones, Acelerómetro, Brújula, Sensor de temperatura, y Módulo de voz. 

**1. PLANTEAMIENTO DEL PROBLEMA**

**1.1. Contexto Y Antecedentes**

La placa Microbit es una pequeña tarjeta programable de 4x5 cm diseñada para aprender a programar diversas funciones de modo fácil y al alcance de todos. Esta placa a pesar de su tamaño es potente y permite realizar tareas múltiples con el objetivo de acercar a estudiantes especialmente de educación secundaria a la programación de manera sencilla.
Si bien es cierto, esta tarjeta es una computadora en miniatura de una sola placa con diferentes entradas para fusionar piezas de hardware y con un puerto Ethernet para conectarse a internet. Además, cuenta con sensores incorporados que permite recuperar datos del exterior y a su vez, reflejar la funcionalidad de la placa por una matriz de led.

Es importante recalcar que estas placas fueron creadas por la Fundación BBC de Londres en el 2014 con el objetivo de que los niños desarrollen proyectos a través de un entorno de programación amigable, que a pesar de existir otros tipos de placa en el mercado, ésta sea según Magela Fuzatti (jefa de Laboratorios Digitales del Plan Ceibal) fácil, traspasable y conveniente.

Ahora bien, Create.withcode.uk es una herramienta gratuita creada por Pete Dring profesor de una escuela de Fulford  en Reino Unido, con el fin de escribir, ejecutar, depurar y compartir programas en Python para cualquier navegador web. No es necesario descargar ni instalar ningún programa dado que, es un sitio web diseñado para programar al instante. 

Por otra parte, es importante resaltar que los programas en Python no pueden acceder a los archivos ni dañar el ordenador, por lo que resulta ser una forma segura de aprender a crear con códigos.

De manera que, esta herramienta además de permitir el programar de manera sencilla sin necesidad de una placa física, promueve la inclusión de hombres y mujeres en el aprendizaje de la informática sin importar el lugar, género o edad.


**1.2. Formulación del Problema**

¿Cómo las funciones de la herramienta https://create.withcode.uk/ permite programar y controlar los periféricos de la placa microbit desde cualquier navegador web?

**1.3. Hipótesis de Investigación**

La programación de funciones a través de la herramienta https://create.withcode.uk/  resulta ser una simulación que se asemeja al manejo y control de la placa física Micro bit.

**2. OBJETIVOS**

**2.1 Objetivo General**

Investigar acerca del control de periféricos de la placa Micro Bit en la página https://create.withcode.uk/ para el desarrollo de aplicaciones básicas y avanzadas.

**2.1 Objetivos Específicos**

- Definir las características principales de los siguientes módulos: Imágen, Botones; Acelerómetro; Brújula; Sensor de temperatura y Módulo de voz.
-	Analizar e interpretar los comandos básicos de programación para el control de los módulos de la placa.
-	Elaborar pequeños programas con la herramienta https://create.withcode.uk/ manipulando la placa para cumplir una determinada función

**3. ESTADO DEL ARTE**

*Experience with teaching with BBC micro:bit*

El artículo realizado en el 2020, por los profesores Patrik Voštinár y Jaroslav Knežník de la Universidad Matej Bel tiene el propósito enseñar informática en las escuelas primarias, secundarias y universidad de Eslovaquia. La investigación arrojó la experiencia educativa de estos profesores enseñando programación utilizando placas de Micro:bit en distintos centros educativos donde se pusieron en marcha varias tareas preparadas para la enseñanza de los conceptos básicos de programación.
(Vostinar & Kneznik, 2020) 

*The BBC Micro:bit in the international classroom: Learning experiences and first impressions*

El artículo realizado en el año 2018 por los profesores Maja Videnovik, Eftim Zdravevski, Petre Lameski y Vladimir Trajkovik mostraron las primeras impresiones de varios estudiantes y profesores de varias partes del mundo que tuvieron su primera experiencia con la placa Micro:bit. Los resultados arrojaron que los estudiantes y los profesores, después de un tutorial básico, comenzaron a utilizar esta placa desarrollando sus propios programas sencillos para comprender mejor el funcionamiento de la placa Micro:bit.
 (Videnovik, Zdravevski, Lameski, & Trajkovik, 2018)
 
*What children’s imagined uses of the BBC micro:bit tells us about designing for their IoT privacy, security and safety*
El artículo realizado por Bran Knowles, Joe Finney, Sophie Beck y James Devine, investigadores de la Universidad Lancaster en Reino Unido en el año 2018, tiene por objetivo mostrar la seguridad informática en los dispositivos eléctricos Micro:bit que son utilizados por niños de 9 a 10 años. Los investigadores enseñaron a niños el funcionamiento de la placa, además de mostrarles las seguridades que deben tener al momento de utilizarla. 
(Knowles, Finney, Beck, & Devine, 2018)

**4. MARCO TEÓRICO**

**4.1. Micro:Bit**

*4.1.1. Definición*

BBC microbit es una pequeña tarjeta programable de tan solo 4x5 [cm] diseñada para que el aprendizaje de la programación sea fácil, divertido y al alcance de todos. Tiene un entorno de programación gráfico propio: MakeCode de Microsoft, un sencillo editor gráfico online muy potente. También se puede programar con JavaScript, Python y Scratch (añadiendo una extensión). Gracias a la gran cantidad de sensores que incorpora, sólo con la tarjeta se pueden llevar a cabo centenares de proyectos. (“BBC Placa Micro:Bit - Controlador BricoGeek | BricoGeek.com,” n.d.)

*4.1.2. Partes que constituyen la Microbit*

-	Microcontrolador ARM Cortex-M0
-	Radio Bluetooth Nordic nRF51
-	25 LEDs programables individualmente
-	2 botones programables
-	5 pines de entrada y salida, 3 para entrada y salida de datos y 2 para alimentación (Vcc y GND).
-	Sensor de Luz y Temperatura
-	Sensores de movimiento (acelerómetro y brújula)
-	Comunicación inalámbrica, vía Radio y Bluetooth
-	USB y Conector para batería externa

![]()

**Figura 1: Vista previa de la placa Micro:Bit**

Fuente: http://rogerbit.com/wprb/2019/04/microbit-primeros-pasos-programacion-por-pc-x-cable-y-smartphone-x-bluetooth-dfrobot/

*4.1.3. Generación de Imágenes*

La función de imagen posee una cuadrícula de 5x5 de LED rojos, que permite tener un amplio control sobre la pantalla para crear todo tipo de efectos como imágenes integradas para mostrar en la pantalla. 

Ejemplo No. 1: 

Programación de emoticón feliz, se escribe:

![]()

Se obtiene:

![]()

**Figura 2: Visualización de la imagen por medio de datos ingresdados en una matriz**

Fuente: 

Adicional, se puede personalizar la figura que se requiere que aparezca de la siguiente manera:

![]()

El 0 representa el LED apagado y 5 prendido, podemos poner el número 7, 8 0 9 si se pretende que sea más iluminado el LED. Además, se puede observar cómo se encuentran distribuidos los números en una matriz de 5x5 al igual que los LED’s en las placas, es decir cada número representa cada LED respectivamente.

*4.1.4. Uso de botones*

Es fácil de recordar: la salida es lo que el dispositivo envía al mundo, mientras que la entrada es lo que ingresa al dispositivo para que lo procese. El medio de entrada más obvio en el microbit son sus dos botones, etiquetados como A y B. De alguna manera, necesitamos que MicroPython reaccione a las pulsaciones de botones. (“Buttons — BBC micro:bit MicroPython 1.0.1 documentation,” n.d.)

Esto es notablemente simple:

![]()

Todo lo que hace este script es dormir durante diez mil milisegundos (es decir, 10 segundos) y luego se desplaza la cantidad de veces que presionó el botón A. La función de suspensión hará que el micro: bit se suspenda durante una cierta cantidad de milisegundos. Si desea hacer una pausa en su programa, así es como se hace. Una función es como un método, pero no está unida por un punto a un objeto. Hay un objeto llamado button_a y te permite obtener la cantidad de veces que se ha presionado con el método get_presses. Dado que get_presses da un valor numérico y display.scroll solo muestra caracteres, necesitamos convertir el valor numérico en una cadena de caracteres. Hacemos esto con la función str(abreviatura de "cadena"). Este convierte cosas en cadenas de caracteres.(“Buttons — BBC micro:bit MicroPython 1.0.1 documentation,” n.d.).

![]()

**Figura 3: Visualización del logaritmo implementado en la consola**

Fuente: 

*4.1.5. Uso del acelerómetro*

Este objeto le da acceso al acelerómetro integrado. El acelerómetro también proporciona funciones de conveniencia para detectar gestos. Los gestos reconocidos son: arriba, abajo, izquierda, derecha, boca arriba, boca abajo, caída libre, 3g, 6g, 8g, agitar. De forma predeterminada, MicroPython establece el rango del acelerómetro en +/- 2g, actualmente no es posible cambiar el rango del acelerómetro en MicroPython. El acelerómetro devuelve un valor en el rango 0..1024 para cada eje, que luego se escala en consecuencia.

4.1.5.1. Funciones

***microbit.accelerometer.get_x ()***

Obtenga la medida de la aceleración en el eje x, como un número entero positivo o negativo, según la dirección. La medida se da en mili-seg. De forma predeterminada, el acelerómetro está configurado con un rango de +/- 2s, por lo que este método regresará dentro del rango de +/- 2000 ms.

***microbit.accelerometer.get_y ()***

Obtenga la medida de la aceleración en el eje y, como un número entero positivo o negativo, según la dirección. La medida se da en mili-seg. De forma predeterminada, el acelerómetro está configurado con un rango de +/- 2s, por lo que este método regresará dentro del rango de +/- 2000 ms.

***microbit.accelerometer.get_z ()***

Obtenga la medida de la aceleración en el eje z, como un número entero positivo o negativo, según la dirección. La medida se da en mili-seg. De forma predeterminada, el acelerómetro está configurado con un rango de +/- 2s, por lo que este método regresará dentro del rango de +/- 2000 ms.

***microbit.accelerometer.get_values ()***

Obtenga las medidas de aceleración en todos los ejes a la vez, como una tupla de tres elementos de números enteros ordenados como X, Y, Z. De forma predeterminada, el acelerómetro está configurado con un rango de +/- 2s, por lo que X, Y y Z estar dentro del rango de +/- 2000 ms.

***microbit.accelerometer.current_gesture ()***

Devuelve el nombre del gesto actual.

***microbit.accelerometer.is_gesture (nombre)***

Devuelve Verdadero o Falso para indicar si el gesto nombrado está activo actualmente.

***microbit.accelerometer.was_gesture (nombre)***

Devuelve Verdadero o Falso para indicar si el gesto nombrado estuvo activo desde la última llamada.

***microbit.accelerometer.get_gestures ()***

Devuelve una tupla del historial de gestos. El más reciente aparece en último lugar. También borra el historial de gestos antes de regresar.

![]()

**Figura 5: Gráfico que muestra el funcionamiento bpasico del acelerómetro**

Fuente: https://www.ingmecafenix.com/automatizacion/acelerometro/

*4.1.6. Uso de la brújula*

Este módulo le permite acceder a la brújula electrónica incorporada. Antes de usar, la brújula debe calibrarse; de lo contrario, las lecturas pueden ser incorrectas. La no calibración de la brújula hará que su programa se detenga hasta que se complete la calibración. La calibración consiste en un pequeño juego para dibujar un círculo en la pantalla LED girando el dispositivo.

4.1.6.1. Funciones

***microbit.compass.calibrate ()***

Inicia el proceso de calibración. Se le mostrará al usuario un mensaje instructivo, luego de lo cual deberá girar el dispositivo para dibujar un círculo en la pantalla LED

***microbit.compass.is_calibrated ()***

Devuelve Verdadero si la brújula se ha calibrado correctamente y devuelve Falso en caso contrario.

***microbit.compass.clear_calibration ()***

Deshace la calibración, haciendo que la brújula vuelva a estar sin calibrar.

***microbit.compass.get_x ()***

Da la lectura de la fuerza del campo magnético en el eje x en nano tesla, como un número entero positivo o negativo, dependiendo de la dirección del campo.

***microbit.compass.get_y ()***

Da la lectura de la fuerza del campo magnético en el eje y en nano tesla, como un número entero positivo o negativo, dependiendo de la dirección del campo.

***microbit.compass.get_z ()***

Da la lectura de la fuerza del campo magnético en el eje z en nano tesla, como un número entero positivo o negativo, dependiendo de la dirección del campo.

***microbit.compass.heading ()***

Da el rumbo de la brújula, calculado a partir de las lecturas anteriores, como un número entero en el rango de 0 a 360, que representa el ángulo en grados, en el sentido de las agujas del reloj, con el norte como 0.

***microbit.compass.get_field_strength ()***

Devuelve una indicación entera de la magnitud del campo magnético alrededor del dispositivo en nano tesla.

![]()

**Figura 6: Brújula como muestra**

Fuente: https://www.importancia.org/brujula.php

*4.1.7. Uso del sensor de temperatura*

Este módulo permite acceder al termómetto electrónico incorporado. Su implementación es sencilla por lo que en este diagrama de bloques da su explicación.

![]()

Se propone iniciar el programa usando el evento “para siempre”. Añadir el bloque, localizado en la categoría Básico, mostrar número. El valor obtenido del sensor de temperatura será mostrado por el comando del mismo nombre. A continuación, se borra la pantalla y se introduce una pausa de 1000 ms. Quedando el programa de la siguiente forma. En el simulador aparecerá una barra vertical que permite modificar la temperatura, siendo la temperatura marcada la mostrada en el panel LED.

![]()

**Figura 7: Visualización de la temperatura en los LEDs**

Fuente: 

*4.1.8. Generación de sonidos con el módulo de voz*

Micro: bit viene con un potente módulo de música y sonido. Es muy fácil generar pitidos y bloops desde el dispositivo si conecta un altavoz. Utilice pinzas de cocodrilo para conectar el pin 0 y GND a las entradas positivas y negativas del altavoz; no importa en qué sentido estén conectados al altavoz.

![]()

**Figura 8: Tono de música**

Fuente:

Se importa la siguiente librería

![]()

Y se puede reporducir algunas melodías:

![]()

Este es un ejemplo:

![]()

**5. DIAGRAMAS**

Se muestra los diagramas de flujo de los programas ejemplo desarrollados a continuación:

1. Para las imágenes

![]()

2. Para los botones

![]()

3. Para el acelerómetro

![]()

4. Para el sensor de temperatura

![]()

5. Para la brújula

![]()

6. Para el módulo de voz

![]()

**Figura 1: Vista previa de la placa Micro:Bit**

**6. LISTA DE COMPONENTES**

Principalmente, nos basamos en los siguientes sitios web para la realización de este trabajo:
-	https://create.withcode.uk/
-	https://makecode.microbit.org/#editor 

**7. EXPLICACIÓN DEL CÓDIGO FUENTE**

La placa Micro:bit posee distintos módulos que permiten realizar varias aplicaciones. De los módulos que ofrece la placa, a continuación, se mostrará un ejemplo para explicar el funcionamiento del módulo de Imágenes, Botones, Acelerómetro, Brújula, Sensor de temperatura y Módulo de voz. Para todos los programas, primero se debe importar la librería en create.withcode para poder utilizar la placa Micro:bit

![]()

*7.1.Imágen*

Para realizar imágenes utilizando esta placa es posible a través del manejo de los leds que conforman el display de la placa. La placa Micro:bit cuenta con 25 leds colocados en una matriz de 5x5. Se puede controlar la intensidad luminosa de cada uno de los leds del display; el rango de luminosidad va de 0 al 9, teniendo el numero 0 como la luminosidad mínima (apagado) y el 9 como luminosidad máxima (con mayor brillo). 
El display funciona como una matriz, como cada uno de los leds se comporta de forma independiente se puede colocar la intensidad luminosa que se desee.

![]()

El código anterior muestra como la variable boat (bote) se le es asignada el comando Image. Este comando permite utilizar los leds del display, donde la imagen se formará a partir de la matriz ingresada como argumento. Como se dijo el display se comporta como una matriz, para poder realizar la imagen de un bote se le asigna al segundo y al cuarto de la primera, segunda y tercera fila el valor de 5 en el rango de luminosidad, mientras que al resto de leds se le asignan un valor de cero para que estos no se prendan. En la cuarta fila todos los leds son asignados el valor de 9, que es el valor máximo en el rango de luminosidad, para la quinta y última fila el segundo, tercer y cuarto leds son asignados el valor de 9, mientras que el primer y último led de la fila de encuentran con el valor de cero, esto para que se mantengan apagados.

![]()

Para mostrar el valor de la variable boat en el display de la placa se debe utilizar el comando show del display. El comando show permite visualizar a través del display el valor de una variable. El código completo quedaría de la siguiente forma.

![]()

El resultado de la aplicación el código en la página create.withcode se puede visualizar a continuación.

![]()

**Figura 9: Simulación de la imagen de barco en el display de la placa MIcro:bit**

*7.2.Botones*

La placa Micro:bit posee dos botones denominados A y B, estos se encuentran uno en cada lado del display. 
Los botones funcionan de forma independiente; para poder utilizarlos después de haber importado la librería microbit, se debe utilizar el comando “button” seguido del nombre del botón que se desea utilizar. El comando button posee la funcionalidad is_pressed(), esta función permite ejecutar una acción mientras el botón es presionado. 

![]()

A continuación, una aplicación de los botones utilizando la funcion is_pressed().

![]()

Para mostrar el funcionamiento de los botones de recurrió a un bucle while, el cual se mantiene como un bucle infinito dado que no se cambia la condición. La primera validación que realiza el programa es cuando ninguno de los botones es presionado. Mientras ninguno de los botones es presionado se mostrará en el display la imagen de una carita triste, utilizando la función show del display y utilizando una de las imágenes predeterminadas del comando Image. 
La segunda validación que realiza el programa es con el botón A, cuando este botón sea presionado se mostrará en el display de la placa la imagen de una carita feliz. Esto se puede hacer a través de la función show del display y utilizando la imagen predeterminada del comando Image. 
La tercera y última validación que realiza el programa es con el botón B. Cuando este sea presionado ejecuta la función break(), esta función da por terminado el bucle while para dar paso a la última línea de código. La última línea utiliza la función clean(), la cual apaga todos los leds del display, dando por terminado el programa.
Los resultados del programa se muestran a continuación.

Esta imagen muestra el resultado del display cuando no se presiona ninguno de l

![]()

**Figura 10: Simulación de una carita triste en el display de la placa Micro:bit**

Cuando el botón A es presionado se cambia la carita triste por una carita feliz. 

![]()

**Figura 11: Simulación de una carita feliz en el display de la placa Micro:bit**

Cuando el botón B es presionado se limpia el display, dando por terminado su ejecución el programa.

![]()

**Figura 12: Simulación terminada después de pulsar el botón B**

*7.3. Acelerómetro*

Una de las funciones que posee el acelerómetro es la función shake. A continuación, una aplicación del acelerómetro utilizando la función shake.

![]()

El código mostrado es un programa que simula las predicciones de una bola 8. Antes de comenzar cualquier programa se deben importar las librerías a utilizar en el programa, en este caso de la bola 8 se procede a utilizar las librerías microbit y random. La primera permite acceder a la placa Micro:bit y la segunda permite seleccionar cualquier cosa de forma aleatoria.

![]()

La bola 8 cuenta con varias respuestas que cuando es agitada muestra una de ellas. De la misma forma a la variable answer se le asignó una matriz con todas las respuestas que tendrá el programa.

![]()

Para realizar todas las funciones se utilizó un ciclo while infinito donde no se cambia la condición. La primera función que ejecuta el programa es mostrar en el display la imagen de un 8 mientras que no se utilice la función shake del acelerómetro. 

![]()

Cuando se selecciona la función shake del acelerómetro, el programa limpia el display y muestra en el display la respuesta que fue seleccionada de forma aleatoria de la matriz asignada a la variable answer y lo hace utilizando la función scroll del display y la función choice de la librería random. La función scroll hace que el display se comporte como un letrero donde se muestra un mensaje completo por intervalos de tiempo. La función choice escoge, de forma aleatoria, un objeto dentro de un conjunto.

El programa seguirá ejecutándose hasta que se detenga la simulación. Los resultados del programa se pueden apreciar a continuación.

Como se puede observar, se muestra en la pantalla del display la imagen de un 8 mientras no se seleccione la función shake del acelerómetro. 

![]()

**Figura 12: Simulación de la bola 8 en la placa Micro:bit**

Cuando es selecciona la función shake del acelerómetro se comienza a visualizar el mensaje seleccionado de forma aleatoria. Una vez que el mensaje fue mostrado, el display vuelve a mostrar la imagen del 8 hasta que se vuelva a seleccionar la función shake.

![]()

**Figura 13: Despliegue de la respuesta después de pulsar el botón donde activa “shake”**

*7.4. Sensor de Temperatura*

La placa Micro:bit cuenta con un sensor de temperatura, la cual puede ser utilizada para poder leer la temperatura del ambiente. A continuación, un programa que permite leer la temperatura ambiente utilizando el sensor de temperatura de la placa Micro:bit.

![]()

Se utiiliza en bucle while infinito para que el programa se mantenga siempre en ejecución. El sensor de temperatura de la placa leer la temperatura del ambiente, el dato de la medición es obtenido utilizando la función temperature(). Este dato es guardado en la variable temp. 

![]()

Para poder mostrar el valor de la medición realizada por el sensor de temperatura en el display se debe convertir el dato de tipo numerico a tipo string, debido a que el display solo admite variables tipo string. Para realizar la conversion de utiliza la función str(). El valor de la temperatura se visualiza de forma de letrero gracias a la función scroll() del display. 

Los resultados de la simulación se muestran a continuación.

![]()

**Figura 14: Visualización de la temperatura a través del display de la placa Micro:bit**

Como no se tiene físicamente la placa, se realiza la ejecución del programa a través de la página web create.withcode. Aquí el sensor es reemplazado por una barra que permite variar el valor de la temperatura y ese mismo valor es mostrado en el display. 

*7.5. Brújula*

La placa Micro:bit cuenta con una brújula que puede ser utilizada para distintos propósitos, como por ejemplo para mostrar la ubicación en la que uno se encuentra a través del display. 

![]()

Para poder usar la brújula primero se la deba calibrar y esto se lo hace mediante la funcion calibrate(), es una funcion propia de la brujula. 

![]()

Se utiliza un bucle while infinito para que el programa se mantenga corriendo. La validación que realiza el programa es con el botón A, cuando se presiona este botón se mostrará en el display la ubicación en la que el usuario se encuentra. 
La ubicación es mostrada a través de la función heading() de la brújula, esta función da el rumbo que ha tomado la brújula a partir de mediciones anteriores como un número de tipo int en el rango de 0° a 360°, tomando como punto de referencia el Norte. Como el display solo admite variables tipo string se debe convertir la medición de la brújula de tipo int a tipo string utilizando la función str().

![]()

![]()

**Figura 15:Visualización de la posición a través del display de la placa Micro:bit**

*7.6. Brújula*

Para desarrollar el problema de la música, se debe implementar otro simulador llamado “micro:bit”. El presente simulador que permite programar la placa utilizando el lenguaje de programación Python y por medio de programación por bloques. Para poder utilizar el simulador se debe ingresar al siguiente link.

https://makecode.microbit.org/#editor

La placa Micro:bit cuenta con un radio y junto con este dispositivo se cuenta también con la librería “music”. Esta librería permite realizar programas que sean capaces de emitir sonido que va de la emisión de las notas musicales en forma de tonos hasta emisión de melodías completas. 

![]()

El programa empieza con un bucle while infinito, debido a que no se cambia la condición inicial. Una vez que ingresa en el bucle, el problema realiza la primera validación. El comando input.button_is_pressed(Button.A) permite obtener el estado en el que se encuentra el botón, en este caso el botón A. Si el botón A es presionado entonces se configura el volumen del dispositivo por medio del comando music.set_volume(50) que permite cambiar el valor del volumen predeterminado. En este caso se cambia el valor predeterminado de 127 al valor de 50. Por medio del comando music.play_melody("E D G F B A C5 B ", 200) se puede reproducir la melodía que se sea de las que se encuentran grabadas en la placa, para el caso del botón A se colocó la melodía Rising y para el botón B se colocó la melodía Mystery.  

En la imagen se puede observar la simulación del código de la música. Una forma de verificar que el programa funciona correctamente es visualizando en la parte baja de la placa. A lado del pin 0 se puede visualizar el número -8, este número demuestra que el programa funciona correctamente. 

![]()

**Figura 16: Simulación de la música en la plataforma makecode.microbit**

Al igual que con el botón A, en botón B se puede verificar su correcto funcionamiento por medio de número -8 que aparece cuando este es presionado. 

![]()

**Figura 17: Simulación de la música en la plataforma makecode.microbit**

Para una mejor comprensión del código, la plataforma permite la utilización de la programación por bloques convirtiendo el código de lenguaje Python a lenguaje por bloques. 

![]()

**Figura 18: Código del programa de música en lenguaje de programación por bloques**

**8. DESCRIPCIÓN DE PRERREQUISITOS Y CONFIGURACIÓN**

Para poder ejecutar de manera eficiente y sin ningún tipo de inconveniente, simplemente deberá tener una computadora con acceso a internet para ingresar a https://create.withcode.uk/ o a https://makecode.microbit.org/#editor.

**9. CONCLUSIONES**
1.	La investigación realizada mostró que los componentes periféricos de la placa son componentes sencillos de utilizar. La información encontrada para el presente documento fue precisa y concreta, además develó que la característica más importante de este dispositivo, el cual es su accesibilidad. La placa Micro:bit puede ser accesible tanto para personas expertas en electrónica como para niños de primaria. 
2.	Una de las características principales que ofrecen los módulos: Imágenes, Botones, Acelerómetro, Brújula, Sensor de Temperatura y Módulo de voz; es que todos ellos pueden ser programados a través del lenguaje de programación Python. Este lenguaje posee una sintaxis bastante sencilla, por lo cual sólo se necesita comprender la lógica de programación de cada uno de los módulos.
3.	Cada uno de los módulos posee sus propios comandos básicos los cuales permiten ejecutar distintas acciones. Estos comandos son bastante sencillos de entender y pueden ser utilizados para la realización de numerosos programas.
4.	La página web https://create.withcode.uk/. fue una página muy útil para poder simular el comportamiento de los módulos expuestos. El único inconveniente con la utilización de esta página fue en el módulo del Módulo de voz. Para poder realizar este módulo se utilizó la página web  https://makecode.microbit.org/ la cual permitió simular este código sin mayores dificultades.

**10. RECOMENDACIONES**
1.	Se recomienda realizar una investigación complementaria para conocer más sobre los demás módulos y componentes que posee la placa Micro:bit para un mejor manejo de la misma.
2.	Para realizar mejor los programas en la placa Micro:bit, se recomienda conocer el lenguaje de programación Python con la finalidad de comprender de mejor manera la lógica de programación de los módulos de la placa.
3.	Se recomienda consultar más a profundidad sobre los todos los comandos y acciones que poseen todos los módulos de la placa Micro:bit, esto con la finalidad de realizar programas con mayores capacidades que los propuestos en este documento. 
4.	Para utilizar la página web https://makecode.microbit.org se recomienda primero crear un nuevo proyecto, esto con la finalidad que la programación y los cambios realizados en este sean guardados. 


**11. CRONOGRAMA**

![]()

**12. BIBLIOGRAFÍA**

BBC Placa Micro:Bit - Controlador BricoGeek | BricoGeek.com. (n.d.).

Knowles, B., Finney, J., Beck, S., & Devine, J. (2018). What children’s imagined uses of the BBC micro:bit tells us about designing for their IoT privacy, security and safety. IET Conference Publications, 2018(CP740), 15 (6 pp.)-15 (6 pp.). https://doi.org/10.1049/cp.2018.0015

Videnovik, M., Zdravevski, E., Lameski, P., & Trajkovik, V. (2018). The BBC Micro:bit in the international classroom: Learning experiences and first impressions. 2018 17th International Conference on Information Technology Based Higher Education and Training, ITHET 2018, 1–5. https://doi.org/10.1109/ITHET.2018.8424786

Vostinar, P., & Kneznik, J. (2020). Experience with teaching with BBC micro:bit. IEEE Global Engineering Education Conference, EDUCON, 2020–April, 1306–1310. https://doi.org/10.1109/EDUCON45650.2020.9125278

**13. ANEXOS**

*13.1 Manual de Usuario*

15.1.1 Páginas Web y Archivos

Primero se debe descargar el archivo adjunto donde se encuentran el código de todos los programas que describen el funcionamiento básico de cada una de las siguientes funcionalidades de la placa Micro:bit; estas son Imágenes, Botones, Acelerómetro, Sensor de Temperatura, Brújula y Música. 
El archivo que contiene todos los programas es un archivo con extensión .txt llamado “Codigo Programas Micro:bit”. El archivo, además de tener el código de todos los programas para cada una de las funcionalidades, posee una pequeña descripción de lo que realiza cada programa.  
De todas las funcionalidades descritas, la única que debe ser ejecutada en otra página es la funcionalidad de la Música. Para el resto de funcionalidades se puede utilizar la página web de créate.withcode.uk.
Página web para las funcionalidades Imágenes, Botones, Acelerómetro, Brújula y Sensor de Temperatura:
https://create.withcode.uk/
Página web para la funcionalidad Música: 
https://makecode.microbit.org/

15.1.2 Ejecución de los programas para las funcionalidades Imágenes, Botones, Acelerómetro, Brújula y Sensor de Temperatura. 

Luego de haber descargado el archivo .txt que contiene todos los programas, se debe ingresar a la página web antes descrita. Cuando se haya ingresado debe aparecer la siguiente pantalla.

![]()

Primero se debe borrar el código que viene por defecto en la página web, esto con la finalidad de copiar y pegar uno de los códigos de cualquiera de las cinco funcionalidades. 

![]()

![]()

En las anteriores imágenes se ve un ejemplo del procedimiento descrito. Para este ejemplo se seleccionó el código de la función Botones del archivo .txt y el código fue pegado en la página web. Para poder correr el programa se debe hacer click en el botón play que hay en la parte inferior derecha de la página web (el botón que se encuentra encerrado en el cuadro rojo).

![]()

Cuando empiece a ejecutar el programa aparecerá la pantalla de ejecución que mostrará una imagen de la placa, la cual estará ejecutando el código correctamente como se puede apreciar en la imagen anterior. 

15.1.3 Ejecución del programa para la función Música 

Para poder ejecutar correctamente esta función primero se debe ingresar a la página web descrita, donde parecerá la siguiente pantalla. 

![]()

Para poder utilizar esta página no se necesita tener cuenta, es una página de libre acceso que permite realizar simular el comportamiento de la placa Micro:bit. Primero se debe crear un nuevo proyecto para poder acceder a la placa, y para eso se debe selecciona el recuadro morado con la imagen de un “+” que dice “Nuevo Poryecto”.

![]()

Cuando se selecciona la opción “Nuevo Proyecto”, aparecerá de inmediato una ventana de mensaje donde pide que se le ponga nombre al proyecto. Una vez puesto el nombre del proyecto se selecciona opción “Crear” y el proyecto es creado. 

![]()

Cuando el proyecto es creado aparece la pantalla como se muestra en la imagen anterior. La página web permite porgramar tanto el código de bloques como en lenguaje Python. Para poder utilizar el código del archivo .txt, primero se selecciona la opción Python (opción encerrada en el cuadro rojo). 

![]()

Luego de seleccionar la opción Python, se cambiará a la pantalla como se muestra en la imagen anterior. Como en las otras funcionalidades primero se borra el código que sale por defecto y se transcribe el código del archivo .txt. En esta página la ejecución es automática, es decir, que no debe ser inicializada porque la misma página la inicializa de forma automática. 

![]()

![]()

*15.2 Archivos .py*

Los archivos con extensión .py que contiene el código de todos los programas se encuentra ubicado en la carpeta Instaladores del repositorio. 
