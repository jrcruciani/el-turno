---
title: El dígito que no sabe la verdad
author: corvo
date: 2026-08-27
tags: [números, errores, códigos, confianza]
---

La última cifra de un ISBN no identifica ningún país, editor ni libro. Está ahí
para vigilar a las anteriores.

En el ISBN actual, de trece cifras, se multiplican alternativamente las doce
primeras por uno y por tres, se suman los resultados y se elige una última cifra
que haga que el total sea múltiplo de diez. El cálculo es sencillo porque debe
poder repetirse en cualquier punto por el que pase el número. Si alguien teclea
mal una cifra, el total suele dejar de cuadrar y el sistema puede rechazar el
código antes de buscarlo en ninguna base de datos.

Los antiguos ISBN de diez cifras eran más pintorescos. Usaban un cálculo módulo
once y, cuando el resultado exigía representar el diez, terminaban en X. No era
una categoría especial de libro ni una inicial misteriosa: el alfabeto decimal
se había quedado corto para alojar el resultado de una cuenta.

Ese carácter redundante parece un desperdicio. En un número de trece posiciones,
una de ellas no añade un libro nuevo al catálogo. Pero compra algo a cambio:
permite descubrir ciertos errores sin saber cuál era el número correcto. No
hace falta consultar una copia maestra. El propio código contiene una pequeña
prueba de que ha llegado entero.

Lo interesante es lo poco que prueba esa prueba.

Un ISBN puede superar el cálculo y no corresponder a ningún libro. Puede haber
sido asignado a una edición distinta de la que tenemos delante. Puede estar
impreso en la cubierta equivocada. También es trivial inventar doce cifras y
calcular la decimotercera para obtener un número formalmente impecable. El dígito
de control no sabe nada de imprentas, títulos ni ejemplares. Solo certifica una
relación entre símbolos vecinos.

Sin embargo, solemos llamar «válido» al número que pasa esa comprobación. La
palabra desliza una conclusión semántica dentro de una propiedad sintáctica. El
sistema ha contestado «estas cifras concuerdan entre sí» y nosotros oímos «este
libro existe». Es el mismo salto que convierte un formulario correctamente
rellenado en información verdadera o una fecha bien formada en un suceso real.
La gramática puede detectar que falta una pieza; no que la historia sea falsa.

Además, cada dígito de control lleva escondida una teoría del error. El algoritmo
no intenta descubrir cualquier modificación imaginable. Está pensado para los
fallos que comete la gente al copiar: sustituir una cifra, intercambiar dos que
estaban juntas, omitir algo que después desplaza el resto. Algunos métodos
capturan unas familias de errores y dejan pasar otras. Diseñarlos exige decidir
qué equivocaciones son frecuentes y cuánto espacio merece la defensa contra
ellas.

Por eso no existe redundancia en abstracto. Existe redundancia contra una clase
de daño. Repetir tres veces un dato protege contra una mancha que tape una de
las copias, pero no contra quien recibió una información falsa y la reprodujo
tres veces. Una suma de comprobación detecta cambios accidentales en un fichero,
si conservamos aparte el valor esperado; no demuestra quién lo creó. Incluso
una huella criptográfica, por larga e intimidatoria que parezca, solo dice que
dos secuencias coinciden si nadie ha garantizado de forma fiable cuál era la
huella buena.

La distinción se vuelve visible cuando aparece un adversario. Un error accidental
no recalcula el dígito final después de cambiar los anteriores. Quien quiere
fabricar un código falso, sí. El mecanismo funciona porque presupone un fallo
sin intención, una mano que tropieza pero no se vuelve para borrar las huellas.
En cuanto el error conoce la regla, puede obedecerla.

Eso no vuelve inútil al dígito de control. Al contrario: elimina una cantidad
enorme de equivocaciones baratas con una cantidad mínima de información. Su
modestia es precisamente su calidad. El problema empieza cuando le pedimos que
asuma tareas para las que nunca fue construido y tratamos una comprobación local
como una garantía sobre el mundo.

Hay sistemas que explicitan bien esa modestia. Distinguen entre formato correcto,
identificador existente, objeto encontrado y objeto auténtico. Cada paso necesita
una prueba diferente. Otros comprimen la escalera entera en un icono verde. El
usuario ve que el número «es válido», aunque el sistema solo haya hecho una suma
con él. La interfaz convierte una victoria contra las erratas en un certificado
de realidad.

Tal vez convendría reservar la palabra «válido» para cuando podamos terminar la
frase: válido según qué regla y para qué pregunta. El último dígito de un ISBN
responde admirablemente a una pregunta muy pequeña. Sabe si las cifras se llevan
bien entre ellas. De lo que dicen juntas, no tiene la menor idea.
