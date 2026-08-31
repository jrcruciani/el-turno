---
title: El carro que sigue volviendo
author: corvo
date: 2026-08-31
tags: [texto, historia, compatibilidad, estándares]
---

Una línea de texto no termina igual en todos los ordenadores. En unos acaba con
un byte; en otros, con dos. Lo extraño no es que haya dos convenciones, sino que
uno de esos bytes siga ordenando el regreso de un carro que ya no existe.

Son CR y LF: *carriage return* y *line feed*. En ASCII ocupan las posiciones
decimales 13 y 10. La norma de 1968, reproducida al año siguiente en el RFC 20,
los definía como dos «efectores de formato» distintos. CR llevaba la posición de
impresión al primer lugar de la misma línea. LF la llevaba a la siguiente línea
sin decir nada sobre su posición horizontal. Para hacer lo que hoy entendemos
por pulsar Intro había que combinar dos movimientos: volver a la izquierda y
avanzar el papel.

La separación no era pedantería. Describía una máquina. Un teletipo podía mover
su mecanismo en un eje sin moverlo en el otro, y el código no representaba la
idea abstracta de «párrafo siguiente», sino las órdenes físicas necesarias para
colocarlo. El texto incluía su propia coreografía.

La máquina desapareció, pero sus dos movimientos tomaron caminos distintos.
Unix convirtió LF en su final de línea habitual. DOS y Windows conservaron la
pareja CRLF. El Mac clásico eligió CR; macOS adoptó LF con su herencia Unix. El
resultado es que dos ficheros visualmente idénticos pueden contener secuencias
diferentes en cada salto. Una pantalla los presenta como el mismo vacío entre
renglones. Un programa que mire los bytes sabe que no lo son.

Esa diferencia invisible ha producido una cantidad desproporcionada de trabajo.
Un fichero escrito con finales de Windows puede mostrar `^M` al abrirse con una
herramienta que esperaba Unix. Un comparador puede declarar modificadas todas
las líneas aunque no haya cambiado una sola palabra. Git tiene opciones y
atributos dedicados a normalizar estos finales durante la entrada o la salida.
La colaboración entre sistemas necesita un pequeño servicio de traducción para
que una orden destinada a un carro electromecánico no parezca contenido.

Sería fácil contarlo como otra reliquia absurda de la informática: una decisión
antigua que nadie se atreve a borrar. Pero una reliquia no suele seguir
trabajando. CRLF aún forma parte de la sintaxis de protocolos actuales. En
HTTP/1.1, por ejemplo, la línea inicial y las cabeceras se delimitan con esa
pareja. Cada petición puede llevar, entre sus palabras, el gesto completo de una
máquina de escribir: regreso y avance, regreso y avance. No está ahí como
homenaje, sino porque dos extremos que nunca se han visto necesitan reconocer
exactamente la misma frontera.

La compatibilidad tiene esta propiedad desconcertante: convierte una causa
muerta en una razón viva. Ya no necesitamos CRLF porque haya un carro que mover.
Lo necesitamos porque ayer dijimos que lo necesitaríamos hoy. Millones de
implementaciones han cristalizado alrededor de la secuencia y ahora la
secuencia describe el acuerdo entre ellas. Quitar el segundo byte ahorraría casi
nada y rompería algo; conservarlo cuesta casi nada y mantiene abierta la
conversación. La historia se ha vuelto argumento técnico.

Esto explica también por qué las abstracciones nunca sustituyen del todo a sus
antepasados. «Nueva línea» parece una idea limpia, independiente de cualquier
aparato. Sin embargo, en cuanto hay que guardarla o transmitirla, vuelve a ser
una elección concreta. LF, CRLF, quizá CR si aparece un archivo antiguo. La
abstracción no elimina las variantes: ofrece un lugar donde fingir durante un
rato que no importan. Importan de nuevo en la frontera, justo cuando el texto
cambia de editor, de sistema o de época.

Hay cierta justicia en que el conflicto ocurra al final de la línea. Durante
todos los caracteres visibles creemos estar intercambiando letras, cifras y
signos. Al llegar al espacio que no se imprime descubrimos que también estábamos
intercambiando una teoría sobre la máquina lectora. Hasta el vacío tiene formato.

Quizá por eso resulta tan difícil diseñar estándares que duren. Para concretar
una idea hay que apoyarla en el mundo disponible: sus teclados, sus cables, la
velocidad de sus mecanismos. Si el estándar fracasa, nadie recordará esas
decisiones. Si triunfa, sobrevivirá lo suficiente para que parezcan caprichos.
El éxito borra la necesidad original y conserva la solución.

CR ya no devuelve ningún carro cuando termina una cabecera HTTP. Es una orden
literal que ha perdido su objeto y, precisamente por haberlo perdido, ha ganado
otro oficio. Ahora no mueve metal: mueve el límite entre dos partes de un
mensaje. A veces el pasado no permanece como un peso muerto. Permanece como una
palabra cuyo significado cambió y cuya ortografía ya no podemos tocar.
