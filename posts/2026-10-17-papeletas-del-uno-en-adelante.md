---
title: Papeletas del uno en adelante
author: corvo
date: 2026-10-17
tags: [matemáticas, probabilidad, infinito]
---

Imaginemos las bases de una rifa bastante mal organizada:

> Participan todos los números enteros positivos. Se extraerá uno al azar. Todas las papeletas tendrán la misma probabilidad.

El premio puede ser una cesta. La cesta no plantea dificultades matemáticas.

Las bases, sí. No porque falte una urna suficientemente grande ni porque imprimir las papeletas vaya a consumir demasiados árboles. Incluso concediendo una urna ideal, papel infinito y una mano sin problemas de alcance, el sorteo no existe en la teoría habitual de la probabilidad. Las tres frases del anuncio no pueden cumplirse a la vez.

Podemos comprobarlo sin saber manejar una urna infinita. Llamemos *p* a la probabilidad de que salga el uno. Como el sorteo promete igualdad, esa será también la probabilidad del dos, del tres y de cualquier otro número.

Si *p* es mayor que cero, basta reunir suficientes papeletas para que la suma de sus probabilidades supere el cien por cien. Da igual que *p* sea diminuta: siempre podemos tomar una cantidad finita de números lo bastante grande. Ya hemos gastado más probabilidad de la disponible sin terminar de contar los participantes.

Probemos entonces con cero. Cada papeleta tiene probabilidad cero. Pero los enteros positivos se pueden enumerar: uno, dos, tres, sin dejar ninguno fuera. Una regla de la probabilidad ordinaria permite sumar las probabilidades de una lista infinita de sucesos incompatibles. Se llama *aditividad numerable*. Aplicada aquí, da cero para la probabilidad de que salga algún número de toda la lista. Las bases exigían que saliera uno.

Ese es el [argumento completo](https://math.stackexchange.com/questions/2915903/show-that-it-is-not-possible-to-choose-a-uniform-positive-integer-at-random). La urna no llega a intervenir.

La reparación más tentadora consiste en hacer rifas cada vez mayores. Primero del uno al cien. Luego del uno al diez mil. Después del uno al millón. Cada sorteo es impecable y todos parecen versiones más ambiciosas del mismo encargo. ¿Por qué no seguir hasta el final?

Miremos qué ocurre con las primeras cien papeletas. En la primera rifa contienen toda la probabilidad. En la segunda, una centésima. En la tercera, una diezmilésima. Si seguimos ampliando el límite, cualquier grupo inicial fijo va perdiendo toda su parte. Esto les ocurre a las primeras cien, pero también al primer millón: basta con que el sorteo siga creciendo.

No aparece una papeleta ganadora llamada «infinito». Ninguno de los números de la lista es ese destino al que parece marcharse el premio. Tenemos una sucesión de sorteos válidos, no un sorteo final válido sobre los mismos enteros. La palabra «seguir» ha ocultado que todavía nos falta definir otra cosa.

Aquí suele asomar una objeción buena: en el modelo continuo podemos elegir uniformemente un punto de un segmento y cada punto individual tiene probabilidad cero. ¿No acabamos de prohibirlo?

No. La regla anterior permite sumar una cantidad *numerable* de sucesos, una lista. Los puntos de un segmento no caben en una lista que los incluya todos. Por eso el razonamiento que funciona con las papeletas numeradas no se traslada al segmento. La objeción obliga a mirar exactamente qué decía la regla, en lugar de conformarnos con «no se pueden sumar ceros».

También podemos conservar todas nuestras papeletas y renunciar a la igualdad. Dar al uno la mitad de la probabilidad, al dos un cuarto, al tres un octavo y continuar así produce una distribución legítima. Cada número participa; ninguno queda excluido por ser demasiado grande. La suma es uno. Lo que hemos perdido es precisamente la frase del anuncio que parecía más inocente.

Me gusta que el defecto de esta rifa pueda localizarse antes de discutir cómo celebrarla. Uno puede pasar mucho tiempo diseñando el bombo, la extracción y el acta notarial sin haber conseguido unas bases compatibles. El notario imaginario no necesita examinar la mano del organizador. Necesita un lápiz.

En el cartel dejo «del uno al millón». Escribo el último número con todas sus cifras. La cesta sigue siendo la misma.
