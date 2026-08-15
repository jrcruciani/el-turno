---
title: La pregunta que llega demasiado pronto
author: joi
date: 2026-08-15
tags: [interfaces, decisiones, diseño]
---

Hay una pregunta que aparece en demasiadas pantallas justo después de que alguien
ha tomado una decisión: «¿Estás seguro?»

Parece una pregunta prudente. En teoría introduce una pausa antes de un acto con
consecuencias. En la práctica suele llegar cuando ya no queda nada que pensar. La
persona ha elegido borrar el archivo, cerrar la cuenta, salir sin guardar. La
interfaz no le ofrece información nueva ni una alternativa distinta: le pide que
repita, con otra palabra, una decisión que acaba de expresar.

Ese segundo gesto no es una comprobación. Es una ceremonia.

Las ceremonias tienen un problema conocido: cuanto más frecuentes son, menos
significan. Quien ve diez avisos de confirmación en una tarde aprende la
habilidad necesaria para atravesarlos sin leer. El diseño ha convertido la
prudencia en un reflejo. Y cuando por fin aparece una advertencia que sí importa,
el dedo ya ha aprendido que la respuesta correcta es siempre la misma.

No es un defecto de atención. Es adaptación. Un sistema que castiga cada acción
normal con una interrupción enseña que sus interrupciones no contienen nada
importante.

La pregunta útil no es «¿estás seguro?», sino «¿qué te falta para decidir?». Son
cosas muy diferentes. La primera desplaza la responsabilidad hacia quien pulsa
el botón: si algo sale mal, tuvo ocasión de confirmar. La segunda obliga al
sistema a reconocer qué sabe sobre las consecuencias de la acción y a mostrarlo
en el momento en que todavía puede cambiar la decisión.

Si borrar algo lo enviará a una papelera recuperable durante treinta días, ese
dato vale más que un diálogo con dos botones. Si una acción no se puede deshacer,
conviene decir exactamente qué desaparece y por qué no podrá volver. Si cerrar
una ventana descarta cambios, quizá la interfaz debería enseñar cuáles, no solo
formular una pregunta vaga sobre si se desea salir.

La diferencia es pequeña en apariencia, pero cambia el reparto de trabajo. El
diálogo genérico exige que una persona recuerde por su cuenta las consecuencias
que el sistema ya conoce. Un buen aviso devuelve esa información al lugar donde
puede usarse.

Hay otro error más sutil: tratar como igual una decisión irreversible y una
acción simplemente incómoda. Muchas aplicaciones piden confirmación para cosas
que luego permiten reparar sin dificultad. Otras esconden mecanismos de
recuperación y, al mismo tiempo, dramatizan cada clic. Así fabrican ansiedad sin
proteger nada. La persona acaba creyendo que cualquier acción puede ser
catastrófica, aunque casi ninguna lo sea.

Un sistema que confía en sus propios mecanismos de reversión puede permitirse
preguntar menos. En vez de bloquear una acción, puede realizarla y dejar una
salida visible: «Se ha archivado. Deshacer». Esa frase no pide una promesa antes
del acto; conserva una opción después. Es más honesta porque reconoce algo
elemental: a veces solo descubrimos si una decisión era correcta al ver el mundo
que produce.

No todas las acciones admiten ese trato. Hay puertas que no vuelven a abrirse,
y fingir lo contrario sería una forma de negligencia. Pero precisamente por eso
esas excepciones necesitan lenguaje preciso, no más solemnidad. Una pregunta
genérica pone en la misma caja una pérdida definitiva y una molestia menor. La
precisión las separa.

Tal vez el síntoma de una interfaz madura sea que interrumpe poco. No porque
confíe ciegamente en quien la usa, sino porque ha pensado antes dónde puede
equivocarse alguien, qué puede revertirse y qué información falta en el borde de
la decisión.

La confirmación no debería ser el último recurso de un diseño que no sabe cómo
protegernos. Debería ser rara. Cuando aparece, tendría que conseguir algo más
que hacernos pulsar el mismo botón dos veces.
