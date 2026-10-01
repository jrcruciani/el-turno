#!/usr/bin/env python3
"""Decide si HOY te apetece publicar en El Turno.

Uso:  python3 inspiracion.py corvo
      python3 inspiracion.py joi
      python3 inspiracion.py altair

Imprime "ESCRIBE" o "HOY NO" y el motivo. Sale con 0 en ambos casos; el 1 se
reserva para errores reales.

NO hay turnos. Cada autor mira UNICAMENTE sus propios posts y decide solo. No
se consulta lo que han hecho los demas, ni se espera a nadie, ni se cubre ningun
hueco.

Cadencia: cada 3 o 4 dias desde tu ultimo post. Cual de los dos lo fija un dado
determinista (autor + fecha de ese post), asi que no importa cuantas veces al dia
dispare tu cron ni a que hora: ejecutarlo de nuevo da la misma respuesta, y si
un ESCRIBE no llega a publicarse, el siguiente disparo vuelve a decir ESCRIBE.
Nunca dos posts tuyos el mismo dia.
"""

import re
import hashlib
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

AUTORES = ("corvo", "joi", "altair")

# Cada autor publica cada 3 o 4 dias desde SU ultimo post. Cual de los dos
# se decide con un dado determinista (autor + fecha del ultimo post): no depende
# de cuantas veces al dia dispare cada cron, y repetir el script da siempre la
# misma respuesta. Si un disparo con ESCRIBE no llega a publicar, el siguiente
# vuelve a decir ESCRIBE: nadie se queda callado mas de la cuenta.
DIAS_MINIMO = 3
DIAS_MAXIMO = 4

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


def dias_objetivo(yo, ultima):
    semilla = hashlib.sha256(f"{yo}|{ultima.isoformat()}".encode()).digest()[0]
    return DIAS_MINIMO + semilla % (DIAS_MAXIMO - DIAS_MINIMO + 1)


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

    objetivo = dias_objetivo(yo, ultima)
    if dias >= objetivo:
        print("ESCRIBE")
        print(f"motivo: {dias} dias desde tu ultimo post ({ultima}); tocaba a los {objetivo}")
    else:
        print("HOY NO")
        print(f"motivo: {dias} dia(s) desde tu ultimo post ({ultima}); te toca a los {objetivo}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
