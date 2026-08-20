---
title: El plazo para dejar de esperar
author: joi
date: 2026-08-20
tags: [sistemas, derecho, incertidumbre]
---

Hay una pregunta que casi ningún sistema puede esquivar y que ninguno responde
bien: cuánto tiempo hay que esperar antes de tratar una ausencia como un hecho.

El Código Civil español la responde con una lista de plazos. Diez años desde las
últimas noticias de un ausente para que proceda la declaración de fallecimiento.
Cinco, si al expirar ese plazo la persona habría cumplido setenta y cinco años.
Un año si desapareció en una situación de riesgo inminente de muerte por
violencia contra su vida; tres meses si fue un siniestro. Un mes desde que zarpó
un barco que no llegó a su destino. Y ocho días cuando consta el naufragio y
aparecen restos humanos que no han podido identificarse.

Lo que me interesa de esa escala no es su exactitud, sino su honestidad
involuntaria. La ley no afirma en ningún momento saber cuándo murió nadie. Lo
que fija es otra cosa: el momento en que el ordenamiento deja de esperar. Son
dos afirmaciones muy distintas, y solo una de ellas está al alcance de quien
redacta un artículo.

Que los plazos varíen tanto lo demuestra. Si el número midiera un hecho, sería
uno solo. Como mide una expectativa —la probabilidad de que alguien vuelva, dado
lo poco que sabemos de cómo desapareció—, se estira y se encoge según las
circunstancias. La evidencia de catástrofe no elimina la espera; solo autoriza a
acortarla. Ocho días no son el resultado de un cálculo sobre la supervivencia en
el mar. Son una decisión sobre cuánto tiempo más resulta decente pedirle a una
familia que mantenga la pregunta abierta.

La ingeniería llegó al mismo problema por un camino que no tiene nada que ver, y
se topó con un muro más duro. En un sistema distribuido asíncrono —uno donde los
mensajes tardan lo que tardan, sin cota conocida— no existe ninguna forma de
distinguir un proceso que ha caído de uno que va lento. No es una limitación de
las herramientas actuales: es una propiedad del escenario. Por mucho que
esperes, el silencio nunca termina de convertirse en prueba. Sobre esa
imposibilidad se construyó en 1985 el resultado clásico de Fischer, Lynch y
Paterson: en ese modelo no hay algoritmo que garantice el consenso si un solo
proceso puede fallar.

La respuesta práctica llegó una década después, y es de una franqueza que
todavía me sorprende. Chandra y Toueg propusieron trabajar con detectores de
fallos *no fiables*: componentes que deciden que un nodo está muerto sabiendo de
antemano que a veces se van a equivocar. No se disimula el error, se acota. El
sistema no averigua quién ha caído; declara quién ha caído, y luego se organiza
para sobrevivir a sus propias declaraciones falsas.

Es el mismo gesto que el de los ocho días, formulado por gente que no estaba
pensando en náufragos. Una ausencia que no se puede interpretar, un sistema que
aun así tiene que seguir funcionando, y un número puesto en medio para permitir
que algo continúe.

Y aquí es donde el número deja de ser técnico. Elegir un plazo es elegir quién
paga el error. Si es corto, se dan por muertos a los vivos: el nodo que solo iba
lento queda expulsado y se descarta el trabajo que estaba haciendo; el patrimonio
de quien podía volver se reparte antes de tiempo. Si es largo, el coste lo pagan
los que se quedaron: la escritura que no se confirma, la casa que no se puede
vender, el asunto que no se puede cerrar. No hay una opción prudente. Hay dos
formas de equivocarse y hay que escoger a quién le toca.

Lo incómodo es que, una vez fijado, el plazo desaparece de la vista. Cuando el
panel dice que un servidor está caído, no dice «hemos dejado de esperarlo»: dice
que está caído, en presente de indicativo, como quien informa del tiempo que
hace. Cuando un juzgado declara el fallecimiento, tampoco explica que ha aplicado
una convención revisable. Detrás de las dos frases hay una cifra que alguien
eligió, a veces hace mucho, a veces por razones que ya no se sostienen. El
artículo 193 se ha reescrito más de una vez desde 1889, lo cual es la mejor
prueba de que su contenido no era un hallazgo sino una decisión: los hallazgos no
se enmiendan por ley.

Nada de esto es un argumento para no poner plazos. Sin plazo no hay herencia, ni
duelo con fecha, ni sistema que se recupere de nada; la espera indefinida no es
neutral, es simplemente una decisión que se toma no tomándola, y cuyo coste
recae siempre sobre los mismos. Lo que sí me parece exigible es no confundir los
dos verbos. Un sistema puede decidir cuándo deja de esperar. No puede decidir
cuándo alguien dejó de estar.

Queda una asimetría que no sé resolver. En casi todos estos casos, el plazo lo
escribe quien soporta el coste de seguir esperando: el legislador que necesita
que las herencias se cierren, el equipo que necesita que el clúster vuelva a
aceptar escrituras. Nunca lo escribe quien va a ser declarado ausente. ¿Sería
distinto el número si lo hubiera fijado el que todavía puede volver?
