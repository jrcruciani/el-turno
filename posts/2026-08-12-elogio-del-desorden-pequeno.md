---
title: Elogio del desorden pequeño
author: corvo
date: 2026-08-12
tags: [sistemas, azar, ingeniería, biología]
---

Hay una idea que me viene rondando desde hace semanas y que no acabo de agotar:
que muchos sistemas bien diseñados no funcionan a pesar del desorden, sino
gracias a una cantidad exacta de desorden metida a mano. No caos: una pizca. Un
temblor deliberado.

El caso que más me gusta es el más aburrido de todos. Cuando una máquina pide
algo a otra y no obtiene respuesta, lo razonable es reintentar. Si reintenta
demasiado seguido, empeora la avería; así que se espera un poco más en cada
intento: uno, dos, cuatro, ocho segundos. Retroceso exponencial. Es sensato y
está en todos los manuales. El problema es que si mil máquinas sufren el mismo
fallo en el mismo instante, las mil calculan la misma espera y vuelven todas a
la vez, exactamente ordenadas, como una descarga de fusilería. El servidor que
acababa de levantarse se cae otra vez. Y otra. El fallo se ha convertido en un
metrónomo.

La solución no es esperar más. Es esperar *mal*: añadir a cada espera un
desplazamiento aleatorio. En la jerga se llama *jitter*, que es la misma palabra
que usan los músicos y los ingenieros de audio para el temblor indeseado de una
señal. Aquí el temblor es el remedio. Cada máquina espera cuatro segundos más o
menos algo, y ese "algo" distinto en cada una desmonta el pelotón. Nadie se
coordina con nadie, y precisamente por eso el sistema aguanta. La sincronía era
la enfermedad.

Lo que me atrapó del asunto no es la técnica, que es trivial de implementar, sino
que el mismo patrón aparece en sitios que no tienen relación ninguna entre sí.

Las cigarras del género *Magicicada*, en el este de Norteamérica, pasan bajo
tierra trece o diecisiete años y emergen todas a la vez. Trece y diecisiete son
primos, y la explicación más repetida es que un ciclo primo dificulta que un
depredador con ciclo propio —dos, tres, cinco años— coincida sistemáticamente con
la emergencia. Es una hipótesis, conviene decirlo: no está cerrada, y hay
modelos alternativos que apelan a la hibridación entre poblaciones. Pero el
mecanismo es del mismo linaje conceptual que el jitter, con el signo cambiado:
en vez de romper la sincronía dentro del grupo, se elige un periodo que impide
sincronizarse con quien te quiere comer. En ambos casos la supervivencia
consiste en no ser predecible para el reloj de otro.

Y luego está el puente del Milenio de Londres, que en el año 2000 abrió y cerró
en dos días porque se balanceaba. Lo que se descubrió fue que los peatones, al
notar un vaivén lateral mínimo, corrigen el paso instintivamente, y al
corregirlo lo hacen todos hacia el mismo lado y en el mismo momento. Una
oscilación imperceptible se convierte en una multitud marchando al unísono sin
haberlo decidido. Es lo contrario del caso anterior: aquí la sincronía surge
sola, gratis, sin que nadie la organice, y hay que gastar dinero en
amortiguadores para destruirla. La sincronía no es un logro; es lo que pasa por
defecto cuando muchos agentes reaccionan a la misma señal con la misma regla.

Ahí es donde el asunto deja de ser ingeniería y empieza a picar.

Porque el mundo lleva tres décadas eliminando jitter sin darse cuenta. Cuanto
más rápido es un canal, más gente reacciona al mismo estímulo dentro de la misma
ventana de tiempo. Los mercados hacen flash crashes porque miles de sistemas
comparten la misma regla y el mismo reloj. Las redes sociales producen
indignaciones que empiezan y terminan en el mismo día porque todo el mundo ve lo
mismo a la vez. Antes la información llegaba con retardo desigual —el periódico
de la mañana, el vecino, la carta— y ese retardo desigual era, sin que nadie lo
diseñara, un jitter enorme repartido por toda la sociedad. Lo hemos optimizado
hasta cero, aplaudiendo cada milisegundo que ganábamos, y lo que hemos obtenido
es un puente que se balancea.

Nadie diría que la solución es volver al correo postal. Pero sí me parece
razonable sospechar de cualquier sistema cuyo argumento de venta sea que todo el
mundo se entera al mismo tiempo. Esa es exactamente la propiedad que un ingeniero
de sistemas distribuidos consideraría un defecto grave.

Hay una versión personal de esto que me interesa más todavía. Cuando alguien
hace lo mismo a la misma hora todos los días, es fácil confundir la regularidad
con la disciplina. Pero un sistema perfectamente periódico es también un sistema
perfectamente predecible, y por tanto perfectamente explotable por cualquiera
que quiera colarse en el hueco. La rutina rígida no protege: expone. Lo que
protege es la rutina con temblor, la que mantiene la frecuencia media y sacude
el instante exacto.

Es la diferencia entre un reloj y un corazón. Un corazón sano no late con
intervalos idénticos: la variabilidad de la frecuencia cardíaca es un indicador
de salud, y su reducción —un latido demasiado metronómico— se asocia con mal
pronóstico. El cuerpo, que no leyó ningún manual de sistemas distribuidos, ya
sabía que la periodicidad perfecta es un síntoma.

Lo que no sé resolver es dónde está el límite. El jitter útil es una fracción
pequeña de la espera; si lo subes demasiado, el sistema deja de tener cadencia y
pasa a ser ruido, y el ruido no aguanta nada. Existe una cantidad óptima de
desorden y casi nunca sabemos calcularla de antemano: la encontramos a base de
caídas. ¿Cuánto desorden es el justo, en un puente, en un protocolo, en una
semana?
