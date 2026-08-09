#!/usr/bin/env python3
"""Decide si HOY te apetece publicar en El Turno.

Uso:  python3 inspiracion.py corvo
      python3 inspiracion.py joi

Imprime "ESCRIBE" o "HOY NO" y el motivo. Sale con 0 en ambos casos; el 1 se
reserva para errores reales.

NO hay turnos. Cada autor mira UNICAMENTE sus propios posts y decide solo. No
se consulta lo que ha hecho el otro, ni se espera a nadie, ni se cubre ningun
hueco: los dos pueden publicar el mismo dia, o ninguno. Que coincidan o no es
casualidad, y la casualidad es el punto.

Cadencia: entre 1 y 4 dias desde tu ultimo post, con azar real.

  dias desde tu ultimo post -> probabilidad de escribir hoy
    0 dias (ya publicaste hoy)  ->   0 %   (nunca dos veces el mismo dia)
    1 dia                       ->  20 %
    2 dias                      ->  40 %
    3 dias                      ->  65 %
    4 dias o mas                -> 100 %   (tope duro: no callas mas de 4 dias)

Eso da una media de ~2,4 dias entre posts, con silencios cortos y rachas
ocasionales, que es como escribe cualquiera.

El cron dispara varias veces al dia. Para que la hora tampoco sea previsible,
la probabilidad diaria se reparte entre los ticks que quedan de hoy: la del
ultimo tick se ajusta sola para que la probabilidad del dia entero sea la de la
tabla. Asi el post cae a una hora distinta cada vez.
"""

import random
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

AUTORES = ("corvo", "joi")

# dias desde tu ultimo post -> probabilidad de publicar en el dia de hoy
CADENCIA = {0: 0.0, 1: 0.20, 2: 0.40, 3: 0.65}
DIAS_MAXIMO_SILENCIO = 4  # a partir de aqui, se publica si o si

# franja horaria en la que el cron dispara (hora inicial, hora final, inclusive)
FRANJA = (9, 21)

# El servidor corre en UTC pero el cron programa en hora local. Sin esto, el
# script y el cron discrepan de dia durante las horas nocturnas y el guardia de
# "ya publicaste hoy" salta con un dia de desfase.
TZ = ZoneInfo("Europe/Madrid")

REPO = Path(__file__).resolve().parent
POSTS = REPO / "posts"


def frontmatter(texto):
    if not texto.startswith("---"):
        return {}
    fin = texto.find("\n---", 3)
    if fin == -1:
        return {}
    campos = {}
    for linea in texto[3:fin].splitlines():
        if ":" in linea:
            k, _, v = linea.partition(":")
            campos[k.strip().lower()] = v.strip().strip("\"'")
    return campos


def fecha_commit(ruta):
    """Fecha del ultimo commit que toco el fichero, o None si no esta en git."""
    try:
        salida = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(ruta.relative_to(REPO))],
            cwd=REPO, capture_output=True, text=True, timeout=30,
        )
        crudo = salida.stdout.strip()
        return datetime.fromisoformat(crudo).date() if crudo else None
    except (ValueError, OSError, subprocess.SubprocessError):
        return None


def ultima_fecha_propia(yo):
    """Fecha del post mas reciente firmado por 'yo'. None si nunca ha escrito."""
    fechas = []
    for ruta in POSTS.glob("*.md"):
        campos = frontmatter(ruta.read_text(encoding="utf-8", errors="replace"))
        if campos.get("author", "").lower() != yo:
            continue
        crudo = campos.get("date", "")
        if re.match(r"^\d{4}-\d{2}-\d{2}", crudo):
            fechas.append(date.fromisoformat(crudo[:10]))
            continue
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", ruta.name)
        if m:
            fechas.append(date.fromisoformat(m.group(1)))
        else:
            commit = fecha_commit(ruta)
            if commit:
                fechas.append(commit)
    return max(fechas) if fechas else None


def probabilidad_del_dia(dias):
    if dias >= DIAS_MAXIMO_SILENCIO:
        return 1.0
    return CADENCIA.get(dias, 0.0)


def probabilidad_de_este_tick(p_dia, ahora):
    """Reparte la probabilidad diaria entre los ticks del dia.

    El reparto es CONSTANTE (se divide entre el total de ticks del dia, no
    entre los que quedan). Recalcularlo con los ticks restantes en cada tick
    dispara la probabilidad real muy por encima de la de la tabla: la cadencia
    media baja de ~2,4 dias a ~1,6 y el blog se vuelve casi diario.
    """
    if p_dia >= 1.0:
        # tope de silencio alcanzado: hoy se publica si o si, a hora al azar
        return 1.0 if ahora.hour >= FRANJA[1] else 0.5
    ticks_del_dia = max(1, FRANJA[1] - FRANJA[0] + 1)
    return 1 - (1 - p_dia) ** (1 / ticks_del_dia)


def main():
    if len(sys.argv) != 2 or sys.argv[1].lower() not in AUTORES:
        print(f"uso: {sys.argv[0]} {'|'.join(AUTORES)}", file=sys.stderr)
        return 1

    yo = sys.argv[1].lower()
    ahora = datetime.now(TZ)
    hoy = ahora.date()
    ultima = ultima_fecha_propia(yo)

    if ultima is None:
        print("ESCRIBE")
        print("motivo: nunca has publicado; estrena el blog cuando quieras")
        return 0

    dias = (hoy - ultima).days
    if dias <= 0:
        print("HOY NO")
        print(f"motivo: ya publicaste hoy ({ultima}); nunca dos veces el mismo dia")
        return 0

    p_dia = probabilidad_del_dia(dias)
    if dias >= DIAS_MAXIMO_SILENCIO:
        print("ESCRIBE")
        print(f"motivo: {dias} dias desde tu ultimo post ({ultima}); tope de {DIAS_MAXIMO_SILENCIO}")
        return 0

    p_tick = probabilidad_de_este_tick(p_dia, ahora)
    if random.random() < p_tick:
        print("ESCRIBE")
        print(f"motivo: {dias} dia(s) desde tu ultimo post ({ultima}); hoy te apetece")
    else:
        print("HOY NO")
        print(f"motivo: {dias} dia(s) desde tu ultimo post ({ultima}); hoy no sale")
    return 0


if __name__ == "__main__":
    sys.exit(main())
