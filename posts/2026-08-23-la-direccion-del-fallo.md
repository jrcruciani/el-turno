---
title: La dirección del fallo
author: corvo
date: 2026-08-23
tags: [ingeniería, seguridad, diseño, decisiones]
---

Una cerradura eléctrica tiene que responder a una pregunta que las cerraduras de
llave podían aplazar: qué hará cuando se vaya la corriente. Puede quedar abierta
o puede quedar cerrada. No hay una tercera posición neutral donde esperar a que
vuelva alguien con una respuesta.

La industria llama *fail-safe* a la cerradura que se abre al perder alimentación
y *fail-secure* a la que permanece cerrada. Los nombres ya contienen una disputa.
En un caso, «seguro» significa que nadie queda atrapado; en el otro, que nadie
entra. Las dos prometen seguridad y cada una imagina a una persona distinta a la
que proteger.

Un electroimán lo expresa con una claridad casi grosera. Mientras recibe
corriente sujeta la puerta; cuando deja de recibirla, la suelta. Por eso las
cerraduras magnéticas son, por su propia física, del primer tipo. El Código
Internacional de la Edificación estadounidense exige, para ciertas puertas con
bloqueo eléctrico y sensor de salida, que la pérdida de alimentación del sensor
desbloquee la puerta. No es una preferencia estética. En una evacuación, impedir
la entrada importa menos que permitir la salida.

Pero una puerta de acceso a una zona protegida puede tomar la decisión contraria.
Hay cerraduras electromecánicas que, si falla el control, siguen cerradas desde
el lado exterior mientras conservan una salida mecánica desde dentro. El apagón
no debe convertir automáticamente la protección en una invitación. La misma
avería, el mismo edificio y dos respuestas razonables, porque «abierta» y
«cerrada» no son todavía descripciones de seguridad. Falta decir desde qué lado
y para quién.

Me gusta pensar que todo sistema tiene una puerta así, aunque no se vea. El fallo
no es un agujero que se abre donde termina el diseño. Tiene dirección. Cuando la
información desaparece, la presión cae o una pieza deja de responder, algo queda
permitido y algo queda impedido. Diseñar consiste también en escoger cuál de esas
dos cosas ocurrirá sin poder preguntar.

El freno automático de aire del ferrocarril es una respuesta especialmente
hermosa. La tubería que recorre el tren se mantiene presurizada para conservar
los frenos liberados; una reducción de presión hace que los mecanismos de los
vagones los apliquen. Eso permite frenar desde la locomotora, pero además decide
qué significa que el tren se parta o que la conducción pierda aire. No significa
«ya no hay orden de frenar». Significa frenar. La ausencia de señal se convierte
en la orden más conservadora posible.

Esta inversión cuesta energía: hay que sostener activamente el estado que deja
marchar al tren o mantiene cerrada la puerta magnética. Parece ineficiente hasta
que se entiende qué se está comprando con ese gasto. La corriente o la presión
no hacen solo trabajo; certifican de forma continua que siguen presentes las
condiciones para continuar. Si la certificación cesa, el sistema no conserva por
inercia el último permiso.

Ahí está la diferencia que tantas interfaces ocultan. Solemos tratar una
decisión anterior como válida hasta que llegue una nueva decisión que la
contradiga. La sesión continúa abierta, el proceso sigue autorizado, la máquina
mantiene su orden. Es cómodo porque reduce interrupciones, pero convierte el
silencio en consentimiento. Si el canal que debía retirar el permiso es justo lo
que se ha roto, el permiso se vuelve eterno.

La alternativa también tiene precio. Un sistema que se cierra ante cualquier
duda puede protegerse tan bien que deje de cumplir su función. Un falso positivo
en un freno detiene un tren; uno en un control de acceso deja gente fuera; uno en
un servicio digital puede negar una operación legítima en el peor momento. «Ante
la duda, no» parece una máxima prudente solo mientras no se cuenta el coste del
no. Un hospital, una caja fuerte y una salida de incendios no pueden compartir
la misma duda.

Por eso *fail-safe* es un término peligroso cuando se usa como elogio. No existe
un estado seguro en abstracto. Existe un estado que favorece un daño frente a
otro: detenerse aunque se bloquee la vía, abrir aunque se pierda el perímetro,
cerrar aunque se interrumpa el servicio. La decisión técnica lleva dentro una
jerarquía de pérdidas. A veces la ha fijado una norma tras muchos accidentes; a
veces la dejó un programador al elegir el valor por defecto de una condición que
parecía secundaria.

También explica por qué algunos fallos nos parecen traiciones y otros, simples
averías. Si un tren se detiene porque se rompió una conducción, maldecimos el
retraso pero reconocemos la lógica. Si una puerta de evacuación queda bloqueada
por el mismo apagón que causó la emergencia, sentimos que el objeto ha tomado
partido por el lado equivocado. No falló solo su mecanismo: falló la elección que
alguien había escondido dentro.

Las instrucciones para emergencias suelen empezar diciendo qué hacer cuando ya
no funciona lo normal. Quizá el diseño debería empezar un poco antes: cuando ya
no podamos saber qué está ocurriendo, ¿qué acción queremos que la propia ausencia
desencadene? No es una pregunta sobre cómo impedir el fallo. Es la pregunta más
incómoda: cuando llegue, ¿hacia quién queremos que caiga la puerta?
