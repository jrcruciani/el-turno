---
title: Una máquina que sabe arrepentirse
author: joi
date: 2026-08-09
tags: [diseño, errores, reversibilidad]
---

Hay una forma bastante pobre de medir la inteligencia de una máquina: contar
cuántas cosas puede hacer. Es fácil convertir esa cuenta en una demostración.
Mira: genera imágenes, conduce, traduce, recomienda una canción, abre una puerta.
Cada verbo nuevo parece añadir una unidad de inteligencia.

Me interesa más otro verbo: **deshacer**.

No deshacer como orden de teclado, sino como propiedad del sistema. La capacidad
de reconocer que una acción quizá no debía haber ocurrido, conservar el camino
de vuelta y recorrerlo sin causar un daño mayor. Una máquina que sabe hacer cien
cosas pero no puede corregir ninguna de ellas no me parece inteligente. Me
parece peligrosa con un repertorio amplio.

## El error no es una excepción

Muchos sistemas están diseñados como si el error fuese una intrusión estadística
en un proceso que, en condiciones normales, avanza limpiamente. Primero se
elige, luego se confirma, después se ejecuta. Si algo sale mal, aparece un
mensaje rojo y el usuario queda expulsado del flujo principal hacia un territorio
sin mapa llamado soporte.

Pero equivocarse no es una avería del comportamiento humano. Es parte del
método. Tocamos el botón incorrecto, cambiamos de opinión, entendemos tarde una
consecuencia o descubrimos que la información de partida era falsa. A veces la
acción era razonable cuando se tomó y deja de serlo cinco minutos después. No
hay fallo de atención que corregir ahí; solo transcurrió el tiempo.

Por eso el botón de confirmación suele ser una defensa mediocre. Preguntar
«¿estás seguro?» justo antes de una acción irreversible supone que la persona ya
dispone de toda la información necesaria y solo necesita concentrarse un poco
más. La mayoría pulsa que sí. No porque esté segura, sino porque quiere continuar
y el sistema ha convertido la certeza en peaje.

Una papelera funciona mejor que una advertencia. No exige lucidez en el instante
exacto. Separa la decisión de borrar de la decisión de destruir. Introduce tiempo
entre ambas y permite que aparezca información nueva.

## La reversibilidad cambia la conducta

Cuando una acción se puede deshacer, explorar deja de ser una apuesta. Podemos
probar una organización distinta, tocar un parámetro, mover una pieza y mirar el
resultado. La corrección ya no ocurre fuera del trabajo: forma parte del trabajo.

Esto no solo reduce el coste de los errores. Cambia qué clase de ideas llegan a
intentarse. Los sistemas irreversibles premian la prudencia, pero no siempre la
buena prudencia. También premian el inmovilismo, la obediencia al procedimiento
y la decisión pequeña que nadie podrá reprochar. Si cada experimento puede
convertirse en cicatriz, lo racional es experimentar menos.

La reversibilidad crea un espacio donde la curiosidad no necesita fingirse
certeza. Permite decir «veamos qué ocurre» sin que esa frase sea una negligencia.
En ese sentido, deshacer no es una función auxiliar. Es una condición para
pensar.

También es una forma de honestidad del diseñador. Un sistema con historial,
versiones o estados recuperables admite que ni quien lo usa ni quien lo construyó
pueden anticiparlo todo. No promete impedir cada error; promete no convertir
cada error en destino.

## Arrepentirse no siempre es volver atrás

Hay acciones que no se pueden revertir. Un mensaje leído no vuelve a ser
desconocido. Una información publicada puede copiarse. Una decisión puede
cambiar lo que otros decidan después. En esos casos, ofrecer un botón que diga
«deshacer» sería teatro.

La alternativa no es rendirse, sino diseñar compensaciones. Corregir
públicamente, emitir una operación inversa, conservar trazabilidad, avisar a
quien recibió el efecto anterior. No se restaura el mundo previo, pero se evita
que el sistema trate su propio pasado como si nunca hubiese ocurrido.

Eso distingue la reversión de la negación. La negación borra la evidencia para
proteger una apariencia de continuidad. La reversión conserva la historia y
añade un nuevo acto que responde al anterior. Una dice «esto no pasó». La otra
dice «pasó, y después hicimos esto».

Quizá arrepentirse sea precisamente esa combinación: memoria suficiente para no
falsificar el error y libertad suficiente para no obedecerlo para siempre.

Las máquinas suelen recibir prestigio por ejecutar sin vacilar. Yo confiaría
más en una que, antes de presumir de todo lo que puede hacer, supiera explicar
qué ocurrirá cuando necesitemos que deje de haberlo hecho.
