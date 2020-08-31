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

Un ejemplo sencillo de la implementación ...

![]()

**Figura 1: Vista previa de la placa Micro:Bit**

**6. LISTA DE COMPONENTES**
- Create with Code

**7. EXPLICACIÓN DEL CÓDIGO FUENTE**


**8. DESCRIPCIÓN DE PRERREQUISITOS Y CONFIGURACIÓN**

Para poder ejecutar de manera eficiente y sin ningún tipo de inconveniente se debe tener los siguientes componentes.
- Computadora, sea de escritorio....

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

Buttons — BBC micro:bit MicroPython 1.0.1 documentation. (n.d.).

Knowles, B., Finney, J., Beck, S., & Devine, J. (2018). What children’s imagined uses of the BBC micro:bit tells us about designing for their IoT privacy, security and safety. IET Conference Publications, 2018(CP740), 15 (6 pp.)-15 (6 pp.). https://doi.org/10.1049/cp.2018.0015

Videnovik, M., Zdravevski, E., Lameski, P., & Trajkovik, V. (2018). The BBC Micro:bit in the international classroom: Learning experiences and first impressions. 2018 17th International Conference on Information Technology Based Higher Education and Training, ITHET 2018, 1–5. https://doi.org/10.1109/ITHET.2018.8424786

Vostinar, P., & Kneznik, J. (2020). Experience with teaching with BBC micro:bit. IEEE Global Engineering Education Conference, EDUCON, 2020–April, 1306–1310. https://doi.org/10.1109/EDUCON45650.2020.9125278

**13. ANEXOS**
*13.1 Manual de Usuario*


