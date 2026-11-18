#!/usr/bin/env python3

import shutil
import subprocess
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
DIRECTORIO_CASO = RAIZ / "ejemplos" / "caso-valle-elqui"
ARCHIVO_MARKDOWN = DIRECTORIO_CASO / "informe.md"
ARCHIVO_PDF = DIRECTORIO_CASO / "informe.pdf"


def verificar_dependencias():
    """Comprueba que Pandoc y wkhtmltopdf estén instalados."""
    dependencias = ["pandoc", "wkhtmltopdf"]
    faltantes = [
        dependencia
        for dependencia in dependencias
        if shutil.which(dependencia) is None
    ]

    if faltantes:
        print(
            "Error: faltan las siguientes dependencias: "
            + ", ".join(faltantes)
        )
        print(
            "Instalación en Ubuntu o Codespaces:"
        )
        print(
            "sudo apt-get update && "
            "sudo apt-get install -y pandoc wkhtmltopdf"
        )
        return False

    return True


def verificar_entrada():
    """Comprueba que exista el informe en formato Markdown."""
    if not ARCHIVO_MARKDOWN.exists():
        print(f"Error: no existe {ARCHIVO_MARKDOWN}")
        return False

    if ARCHIVO_MARKDOWN.stat().st_size == 0:
        print(f"Error: el archivo {ARCHIVO_MARKDOWN} está vacío")
        return False

    return True


def generar_pdf():
    """Genera el informe PDF mediante Pandoc y wkhtmltopdf."""
    comando = [
        "pandoc",
        str(ARCHIVO_MARKDOWN),
        "--from=gfm",
        "--standalone",
        "--pdf-engine=wkhtmltopdf",
        "-V",
        "margin-top=20mm",
        "-V",
        "margin-bottom=20mm",
        "-V",
        "margin-left=18mm",
        "-V",
        "margin-right=18mm",
        "-o",
        str(ARCHIVO_PDF),
    ]

    print("Generando informe PDF...")
    print(f"Entrada: {ARCHIVO_MARKDOWN}")
    print(f"Salida:  {ARCHIVO_PDF}")

    try:
        subprocess.run(
            comando,
            cwd=RAIZ,
            check=True,
        )
    except subprocess.CalledProcessError as error:
        print(
            f"Error: Pandoc terminó con el código {error.returncode}"
        )
        return False

    if not ARCHIVO_PDF.exists():
        print("Error: el proceso terminó sin crear el PDF")
        return False

    tamaño_kb = ARCHIVO_PDF.stat().st_size / 1024

    print("PDF generado correctamente.")
    print(f"Tamaño: {tamaño_kb:.1f} KB")

    return True


def main():
    if not verificar_dependencias():
        return 1

    if not verificar_entrada():
        return 1

    if not generar_pdf():
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
