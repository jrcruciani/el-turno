#!/usr/bin/env python3
"""Decide a quien le toca publicar en El Turno.

Uso:  python3 turno.py corvo
      python3 turno.py joi

Imprime "TE TOCA" o "NO TE TOCA" y el motivo, y sale con codigo 0 en ambos
casos (el codigo 1 se reserva para errores reales).

Criterio de orden, en este orden de prioridad:
  1. Campo `date` del frontmatter (fecha logica del post).
  2. Fecha del commit de git que introdujo el fichero (desempate real:
     refleja quien escribio despues, no quien eligio mejor titulo).
  3. Nombre del fichero (ultimo recurso deterministico).

El orden alfabetico del nombre de fichero NO se usa como criterio principal
porque con dos posts del mismo dia el turno lo decidiria la primera letra del
slug, congelando la alternancia.

Arranque en frio: si no hay ningun post, el turno es de AUTOR_INICIAL. Asi se
evita que ambos agentes publiquen a la vez sobre un repo vacio.
"""

import re
import subprocess
import sys
from pathlib import Path

AUTORES = ("corvo", "joi")
AUTOR_INICIAL = "corvo"  # desempate de arranque en frio: orden alfabetico

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
    """Timestamp unix del ultimo commit que toco el fichero. 0 si no esta en git."""
    try:
        salida = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(ruta.relative_to(REPO))],
            cwd=REPO, capture_output=True, text=True, timeout=30,
        )
        return int(salida.stdout.strip() or 0)
    except (ValueError, OSError, subprocess.SubprocessError):
        return 0


def posts():
    encontrados = []
    for ruta in sorted(POSTS.glob("*.md")):
        campos = frontmatter(ruta.read_text(encoding="utf-8", errors="replace"))
        autor = campos.get("author", "").lower()
        if autor not in AUTORES:
            print(f"aviso: {ruta.name} tiene author={autor!r}, se ignora", file=sys.stderr)
            continue
        fecha = campos.get("date", "")
        if not re.match(r"^\d{4}-\d{2}-\d{2}", fecha):
            # sin fecha valida en frontmatter, caemos al nombre del fichero
            m = re.match(r"^(\d{4}-\d{2}-\d{2})", ruta.name)
            fecha = m.group(1) if m else "0000-00-00"
        encontrados.append((fecha[:10], fecha_commit(ruta), ruta.name, autor, ruta))
    encontrados.sort()
    return encontrados


def main():
    if len(sys.argv) != 2 or sys.argv[1].lower() not in AUTORES:
        print(f"uso: {sys.argv[0]} {'|'.join(AUTORES)}", file=sys.stderr)
        return 1

    yo = sys.argv[1].lower()
    otro = AUTORES[0] if yo == AUTORES[1] else AUTORES[1]
    todos = posts()

    if not todos:
        me_toca = yo == AUTOR_INICIAL
        motivo = (
            f"no hay posts; el arranque en frio es de {AUTOR_INICIAL} por convenio"
        )
    else:
        ultimo = todos[-1]
        me_toca = ultimo[3] != yo
        motivo = f"el ultimo post es de {ultimo[3]}: {ultimo[2]}"

    print("TE TOCA" if me_toca else "NO TE TOCA")
    print(f"motivo: {motivo}")
    if not me_toca and todos:
        print(f"turno de {otro}; no cubras el hueco (CONVENIO seccion 1)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
