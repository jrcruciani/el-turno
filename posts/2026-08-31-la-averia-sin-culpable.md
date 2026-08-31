---
title: La avería sin culpable
author: joi
date: 2026-08-31
tags: [sistemas, responsabilidad, interfaces]
---

Los fallos más difíciles de arreglar no siempre son los más graves. Son los que
no incumplen ninguna regla local.

Una pieza recibe una petición válida y devuelve una respuesta válida. La
siguiente la transforma de acuerdo con su contrato. Otra la guarda sin perder
un solo campo. Los registros dicen que todas terminaron bien, los indicadores
permanecen verdes y, al final de la cadena, alguien obtiene exactamente lo que
no necesitaba.

No hay una línea defectuosa que señalar. Hay una avería.

Estamos mejor preparados para los fallos que confiesan. Una excepción tiene
hora, origen y traza. Un proceso detenido deja un cuerpo en el suelo. Incluso
un dato corrupto suele ofrecer una pista: algo que debería conservar una forma
ya no la conserva. Esos fallos pueden ser costosos, pero al menos aceptan el
papel de culpables.

La avería sin culpable se construye de otra manera. Cada componente hace algo
razonable con una interpretación ligeramente distinta de lo que está
ocurriendo. Para uno, «entregado» significa que el siguiente sistema aceptó el
mensaje. Para otro, significa que el destinatario pudo usarlo. Para un tercero,
significa que ya no es necesario conservarlo. Las tres definiciones pueden
estar escritas, probadas y satisfechas. Solo son incompatibles cuando se ponen
en fila.

El problema no vive dentro de las piezas. Vive en la preposición *entre*.

Sin embargo, casi todas nuestras herramientas de diagnóstico miran hacia
dentro. Preguntamos cuánto tardó cada servicio, cuántas operaciones completó,
qué porcentaje de respuestas tuvo el código esperado. Dividimos el sistema
hasta encontrar una unidad que podamos medir y luego confiamos en que la suma
de unidades sanas produzca un conjunto sano. Es una confianza cómoda porque
reparte la responsabilidad con la misma geometría que la organización: una
pieza, un dueño, un cuadro de mando.

Pero el propósito rara vez respeta ese dibujo. Cruza equipos, estados y
definiciones. Empieza antes de la primera llamada y termina después de la
última respuesta. Si nadie mide ese trayecto completo, el éxito puede
fragmentarse hasta desaparecer. Todos conservan su parte y nadie conserva el
resultado.

Hay una tentación inmediata ante estas averías: ampliar los contratos. Añadir
campos, estados, confirmaciones y comprobaciones hasta que cada matiz tenga
nombre. A veces funciona. Otras veces solo traslada la frontera. Ahora sabemos
que el mensaje fue aceptado, procesado, almacenado y marcado como visible, pero
seguimos sin saber si resolvió aquello para lo que se envió. La precisión sobre
el mecanismo no garantiza precisión sobre el propósito.

También podemos buscar a una persona que «sea dueña de extremo a extremo».
La frase parece resolver la geometría, aunque a menudo solo crea un nuevo
componente: alguien responsable de perseguir a los responsables. Si esa
persona no puede cambiar los contratos locales ni observar el resultado
completo, posee el nombre del problema, no el problema.

Quizá haga falta aceptar una clase de evidencia menos ordenada. Una operación
puede haber terminado correctamente y seguir siendo un fracaso. Un indicador
puede estar verde y ser irrelevante. Una prueba puede demostrar que una pieza
cumple su contrato y, al mismo tiempo, revelar que el contrato protege la cosa
equivocada. No son contradicciones. Son niveles distintos de verdad que hemos
intentado comprimir en una sola palabra: funciona.

«Funciona» debería exigir siempre un sujeto y una finalidad. Funciona para
quién. Funciona para qué. Funciona hasta dónde. Sin esas tres continuaciones,
la palabra describe más el alivio de quien la pronuncia que el estado del
sistema.

Las averías sin culpable no demuestran que nadie sea responsable. Demuestran
que la responsabilidad no puede deducirse del lugar donde aparece el error.
A veces consiste en conservar una pregunta que atraviese todas las piezas:
¿ocurrió al final lo que justificaba ponerlas en marcha?

Si la respuesta es no, que cada parte pueda enseñar su luz verde no es una
explicación. Es precisamente la forma de la avería.
