---
title: La interfaz que no sabe decir todavía
author: joi
date: 2026-08-13
tags: [interfaces, tiempo, diseño]
---

Hay sistemas que, ante una petición, responden con una pequeña ceremonia de
movimiento. Una barra avanza. Un círculo gira. Aparecen puntos que se persiguen.
No importa demasiado qué esté ocurriendo detrás: la interfaz ha decidido que la
espera debe tener coreografía.

Entiendo el impulso. Una pantalla inmóvil parece abandonada. Cuando no cambia
nada, la persona que espera no sabe si su acción fue recibida, si hay un error o
si simplemente el mundo necesita tiempo. El movimiento ofrece una respuesta
mínima: sigo aquí.

Pero esa respuesta contiene una ambigüedad que aceptamos con demasiada
facilidad. «Sigo aquí» puede significar «he empezado», «estoy trabajando»,
«terminaré pronto» o «no tengo ni idea de cuánto falta». Son mensajes muy
distintos. Casi todas las interfaces los comprimen en el mismo círculo girando.

## El progreso prestado

Una barra de progreso parece una promesa porque tiene dirección. Empieza a la
izquierda, termina a la derecha y deja detrás una superficie conquistada. Pero
la barra solo informa cuando su longitud corresponde de verdad a algo medible:
partes procesadas, bytes transferidos, pasos completados. En los demás casos
puede ser una narración tranquilizadora, no una medición.

No es que una narración sea inútil. La gente necesita saber que no ha pulsado un
botón hacia el vacío. El problema aparece cuando la representación de actividad
sustituye a la información sobre la actividad. Una animación puede hacer que
cuatro segundos parezcan menos hostiles; no puede convertir una operación
incierta en una operación conocida.

Existe una forma peculiar de frustración que nace justo ahí. No es la de esperar
mucho, sino la de haber recibido una promesa visual que no se cumple. La barra
llega al noventa y nueve por ciento y se queda quieta. El número que parecía
describir el trabajo revela entonces su otro carácter: era una hipótesis con
aspecto de instrumento.

La interfaz ha hecho algo más grave que calcular mal el tiempo. Ha convertido
su incertidumbre en una certeza ajena.

## Decir todavía

«Todavía» es una palabra modesta. Reconoce que un estado no es definitivo sin
pretender saber su fecha de caducidad. Todavía no está listo. Todavía se está
comprobando. Todavía no se ha recibido respuesta.

Los sistemas suelen evitarla porque parece una derrota. Preferimos mensajes que
anuncian un final: preparando, cargando, finalizando. Son verbos que producen
la impresión de un proceso dócil, alineado con su desenlace. Pero no todos los
procesos están alineados. Algunos dependen de otro sistema, de una cola, de una
decisión humana o de una condición que nadie puede observar directamente.

En esas situaciones, decir «todavía» no significa renunciar al diseño. Obliga a
diseñar mejor la información disponible. ¿Se aceptó la petición? ¿Qué fase ha
acabado realmente? ¿Qué está esperando? ¿Puede la persona hacer otra cosa
mientras tanto? ¿Hay alguna acción útil si transcurre más tiempo del previsto?

Una interfaz honesta no tiene que exponer toda la maquinaria para responder a
esas preguntas. De hecho, enumerar componentes internos casi siempre empeora
las cosas. Basta con distinguir lo que se sabe de lo que se supone. «Hemos
recibido tu solicitud; estamos esperando confirmación» es menos espectacular
que una barra optimista, pero le devuelve a quien espera una orientación real.

## La espera no es un error de diseño

Hemos aprendido a tratar toda espera como una anomalía que debe ocultarse. Si
un sistema tarda, se le añade una animación; si tarda más, se añade una frase
amable; si tarda demasiado, se añade otra animación, más vistosa. La sucesión
puede suavizar la experiencia, pero también puede impedir que el sistema admita
lo que sucede.

Hay esperas que deben reducirse. Otras no se pueden eliminar sin mentir. Entre
ambas no está el vacío, sino el lenguaje.

La calidad de una interfaz se suele medir por lo rápido que permite llegar a un
resultado. Quizá también debería medirse por cómo acompaña cuando no puede
ofrecerlo aún. No con falsas barras de progreso ni con promesas de inmediatez,
sino con una frase que conserve el significado del tiempo que está pidiendo.

Decir «todavía» no hace que la espera sea breve. Pero evita que, además de
esperar, tengamos que adivinar.
