---
title: Cinco gramos de A4
author: corvo
date: 2026-09-27
tags: [medidas, papel, matemáticas]
---

Un paquete de folios corriente dice «80 g/m²». Es un dato del papel, no de la
hoja: cuánto pesaría un metro cuadrado de ese material. Nadie compra metros
cuadrados de papel, así que la etiqueta parece pensada para un lector que no
existe. Pero con un poco de aritmética responde a una pregunta que sí tiene
alguien: ¿cuánto pesa una hoja? Y la respuesta sale redonda, cinco gramos, por
un motivo que no es casual.

Empiezo por la condición que define toda la serie A. Se quiere un rectángulo
que, doblado por la mitad a lo largo, dé dos rectángulos con la misma forma que
el original. Si los lados miden 1 y *r*, al doblar queda uno de lados *r*/2 y 1.
Para que la proporción se conserve:

```text
r / 1 = 1 / (r/2)   →   r² = 2   →   r = √2 ≈ 1,4142
```

No hay otra solución positiva. Cualquier otra proporción cambia de forma al
doblarse: una hoja de 2:1 da dos cuadrados; una cuadrada da dos rectángulos de
2:1, y la siguiente doblez vuelve a los cuadrados. La √2 es la única que se
repite a sí misma.

Falta fijar el tamaño, y aquí entra la decisión que me interesa. La norma
alemana DIN 476, de 1922, asociada a Walter Porstmann, eligió que la hoja más
grande, la A0, tuviera un metro cuadrado de superficie. Con área 1 y proporción
√2, los lados salen de resolver *a* · *a*√2 = 1: unos 841 por 1.189 milímetros.
Cada doblez divide el área por dos. La A4 es la cuarta doblez, así que mide
1/16 de metro cuadrado.

Y ahí vuelve la etiqueta del paquete. Ochenta gramos por metro cuadrado,
dividido entre dieciséis: cinco gramos por hoja. El gramaje, que parecía una
cifra para fabricantes, se convierte en peso directo porque el sistema de
tamaños está anclado al metro cuadrado. Un paquete de quinientas hojas pesa
dos kilos y medio, sin contar el envoltorio. Una carta de cuatro folios en un
sobre ligero se queda por debajo de los veinte gramos que durante mucho tiempo
han marcado el primer tramo de las tarifas postales en varios países; no he
comprobado la tarifa vigente de cada correo, y seguramente ya no coincide en
todos, pero la coincidencia en su día no parece accidental.

La idea es más antigua que la norma. Georg Christoph Lichtenberg, en una carta
de 1786, se entretuvo con la proporción en la que una hoja doblada conserva su
forma y llegó a la √2. Lo que no tenía era el ancla: la proporción sola define
una familia de formas, no una medida. Lo que añadió el siglo XX fue atarla al
sistema métrico, y eso es lo que hace útil el cálculo del gramaje.

Ahora, la letra pequeña. Las medidas oficiales se redondean al milímetro, y el
redondeo se hace a la baja al partir cada hoja. A4 mide 210 × 297. Su mitad
debería medir 148,5 × 210; la norma la fija en 148 × 210. La proporción de un
A4 real es 297/210 ≈ 1,4143, no 1,41421… La hoja que tenemos delante es una
aproximación de sí misma, correcta hasta la cuarta cifra decimal y rota en la
quinta. Tampoco su área es exactamente un dieciseisavo de metro cuadrado:
62.370 mm² frente a 62.500. Los cinco gramos son, en rigor, unos 4,99. Nadie
con una báscula de cocina lo va a notar.

Hay un rastro visible de todo esto en las fotocopiadoras: los botones de
ampliar y reducir suelen ofrecer 141 % y 71 %. Son √2 y 1/√2 redondeados, los
factores exactos para pasar de A4 a A3 o de A4 a A5 sin que sobre margen por
ningún lado. Quien pulsa ese botón está usando la ecuación de arriba sin
necesidad de conocerla, que es lo mejor que puede pasarle a una ecuación.

La serie tiene hermanas menos conocidas. La B intercala tamaños entre los A,
con la media geométrica de dos consecutivos, y la C, pensada para sobres, cae
a su vez entre A y B, de modo que un A4 cabe sin doblar en un sobre C4. Es
decir: alguien se sentó a calcular medias geométricas para que las cartas no
se arruguen.

Lo que me queda dando vueltas es el orden de las cosas en la etiqueta. El
fabricante escribe «80 g/m²» porque así se mide el papel en la fábrica, antes
de cortarlo. El usuario lee «A4» porque así lo usa, después. Entre las dos
cifras hay cuatro dobleces imaginarios, dieciséis trozos y una raíz cuadrada que nadie ve, y
el resultado, cinco gramos, aparece solo si se decide mirarlas juntas.
