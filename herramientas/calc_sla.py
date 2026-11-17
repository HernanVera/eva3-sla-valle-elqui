#!/usr/bin/env python3

import csv
import sys
from pathlib import Path


MINUTOS_PERIODO = 43200
DISPONIBILIDAD_OBJETIVO = 99.9
LATENCIA_MAXIMA_MS = 30.0
JITTER_MAXIMO_MS = 10.0
PERDIDA_MAXIMA_PORCENTAJE = 0.5
THROUGHPUT_MINIMO_MBPS = 180.0
RESPUESTA_MAXIMA_MINUTOS = 60
MTTR_MAXIMO_MINUTOS = 240
COBERTURA_MINIMA_PORCENTAJE = 90.0
CARGO_MENSUAL_CLP = 1200000


def cargar_mediciones(ruta_csv):
    """Carga las mediciones desde el archivo CSV."""
    with open(ruta_csv, "r", encoding="utf-8-sig", newline="") as archivo:
        return list(csv.DictReader(archivo))


def seleccionar(registros, tipo=None, clasificacion=None):
    """Selecciona registros de acuerdo con su tipo y clasificación."""
    resultado = []

    for registro in registros:
        if tipo is not None and registro["tipo"] != tipo:
            continue

        if (
            clasificacion is not None
            and registro["clasificacion"] != clasificacion
        ):
            continue

        resultado.append(registro)

    return resultado


def calcular_disponibilidad(registros):
    eventos_atribuibles = seleccionar(
        registros,
        tipo="evento",
        clasificacion="atribuible",
    )

    minutos_caida = sum(
        int(evento["duracion_minutos"])
        for evento in eventos_atribuibles
    )

    disponibilidad = (
        (MINUTOS_PERIODO - minutos_caida)
        / MINUTOS_PERIODO
        * 100
    )

    minutos_permitidos = (
        MINUTOS_PERIODO
        * (1 - DISPONIBILIDAD_OBJETIVO / 100)
    )

    exceso_minutos = max(0, minutos_caida - minutos_permitidos)

    return {
        "minutos_caida": minutos_caida,
        "disponibilidad": disponibilidad,
        "minutos_permitidos": minutos_permitidos,
        "exceso_minutos": exceso_minutos,
        "cumple": disponibilidad >= DISPONIBILIDAD_OBJETIVO,
    }


def calcular_latencia(registros):
    mediciones = [
        registro
        for registro in seleccionar(registros, tipo="latencia")
        if registro["id"] == "LAT-01"
    ]

    if not mediciones:
        return None

    medicion = mediciones[0]
    valor = float(medicion["valor"])
    muestras = int(medicion["muestras"])
    cobertura = muestras / MINUTOS_PERIODO * 100

    return {
        "valor": valor,
        "muestras": muestras,
        "cobertura": cobertura,
        "evidencia_valida": cobertura >= COBERTURA_MINIMA_PORCENTAJE,
        "cumple": (
            cobertura >= COBERTURA_MINIMA_PORCENTAJE
            and valor <= LATENCIA_MAXIMA_MS
        ),
    }


def calcular_jitter(registros):
    mediciones = seleccionar(
        registros,
        tipo="jitter",
        clasificacion="valida",
    )

    total_muestras = sum(
        int(medicion["muestras"])
        for medicion in mediciones
    )

    suma_ponderada = sum(
        float(medicion["valor"]) * int(medicion["muestras"])
        for medicion in mediciones
    )

    jitter_ponderado = suma_ponderada / total_muestras
    cobertura = total_muestras / MINUTOS_PERIODO * 100

    return {
        "valor": jitter_ponderado,
        "muestras": total_muestras,
        "cobertura": cobertura,
        "evidencia_valida": cobertura >= COBERTURA_MINIMA_PORCENTAJE,
        "cumple": (
            cobertura >= COBERTURA_MINIMA_PORCENTAJE
            and jitter_ponderado <= JITTER_MAXIMO_MS
        ),
    }


def calcular_perdida(registros):
    mediciones = [
        registro
        for registro in seleccionar(registros, tipo="perdida")
        if registro["id"] == "PER-CLIENTE"
    ]

    if not mediciones:
        return None

    medicion = mediciones[0]
    valor = float(medicion["valor"])
    muestras = int(medicion["muestras"])
    cobertura = muestras / MINUTOS_PERIODO * 100
    evidencia_valida = cobertura >= COBERTURA_MINIMA_PORCENTAJE

    return {
        "valor": valor,
        "muestras": muestras,
        "cobertura": cobertura,
        "evidencia_valida": evidencia_valida,
        "cumple": evidencia_valida and valor <= PERDIDA_MAXIMA_PORCENTAJE,
    }


def calcular_throughput(registros):
    mediciones = seleccionar(
        registros,
        tipo="throughput",
        clasificacion="valida",
    )

    valores = [
        float(medicion["valor"])
        for medicion in mediciones
    ]

    promedio = sum(valores) / len(valores)

    return {
        "cantidad_pruebas": len(valores),
        "valores": valores,
        "promedio": promedio,
        "cumple": (
            len(valores) >= 4
            and promedio >= THROUGHPUT_MINIMO_MBPS
        ),
    }


def calcular_respuesta(registros):
    mediciones = seleccionar(
        registros,
        tipo="respuesta",
        clasificacion="valida",
    )

    tiempos = [
        int(medicion["duracion_minutos"])
        for medicion in mediciones
    ]

    incumplimientos = [
        tiempo
        for tiempo in tiempos
        if tiempo > RESPUESTA_MAXIMA_MINUTOS
    ]

    return {
        "cantidad_incidentes": len(tiempos),
        "tiempos": tiempos,
        "maximo": max(tiempos),
        "incumplimientos": incumplimientos,
        "cumple": len(incumplimientos) == 0,
    }


def calcular_mttr(registros):
    eventos = seleccionar(
        registros,
        tipo="evento",
        clasificacion="atribuible",
    )

    duraciones = [
        int(evento["duracion_minutos"])
        for evento in eventos
    ]

    return {
        "duraciones": duraciones,
        "maximo": max(duraciones),
        "cumple": max(duraciones) <= MTTR_MAXIMO_MINUTOS,
    }


def calcular_credito(disponibilidad, respuesta):
    credito_disponibilidad = 0.0
    credito_respuesta = 0.0

    valor_disponibilidad = disponibilidad["disponibilidad"]

    if 99.5 <= valor_disponibilidad < 99.9:
        credito_disponibilidad = 10.0

    if not respuesta["cumple"]:
        credito_respuesta = 5.0

    credito_total = min(
        credito_disponibilidad + credito_respuesta,
        50.0,
    )

    monto_credito = CARGO_MENSUAL_CLP * credito_total / 100

    return {
        "disponibilidad": credito_disponibilidad,
        "respuesta": credito_respuesta,
        "total": credito_total,
        "monto": monto_credito,
    }


def texto_veredicto(cumple):
    return "CUMPLE" if cumple else "NO CUMPLE"


def generar_salida(registros):
    disponibilidad = calcular_disponibilidad(registros)
    latencia = calcular_latencia(registros)
    jitter = calcular_jitter(registros)
    perdida = calcular_perdida(registros)
    throughput = calcular_throughput(registros)
    respuesta = calcular_respuesta(registros)
    mttr = calcular_mttr(registros)
    credito = calcular_credito(disponibilidad, respuesta)

    if perdida["evidencia_valida"]:
        veredicto_perdida = texto_veredicto(perdida["cumple"])
    else:
        veredicto_perdida = "EVIDENCIA INSUFICIENTE"

    lineas = [
        "RESULTADOS DE VERIFICACION DEL SLA",
        "=" * 40,
        "",
        "1. DISPONIBILIDAD",
        f"Caida atribuible: {disponibilidad['minutos_caida']} minutos",
        f"Disponibilidad: {disponibilidad['disponibilidad']:.2f} %",
        f"Caida permitida: {disponibilidad['minutos_permitidos']:.2f} minutos",
        f"Exceso: {disponibilidad['exceso_minutos']:.2f} minutos",
        f"Veredicto: {texto_veredicto(disponibilidad['cumple'])}",
        "",
        "2. LATENCIA",
        f"Promedio mensual: {latencia['valor']:.2f} ms",
        f"Cobertura: {latencia['cobertura']:.2f} %",
        f"Veredicto: {texto_veredicto(latencia['cumple'])}",
        "",
        "3. JITTER",
        f"Promedio ponderado: {jitter['valor']:.2f} ms",
        f"Muestras: {jitter['muestras']}",
        f"Cobertura: {jitter['cobertura']:.2f} %",
        f"Veredicto: {texto_veredicto(jitter['cumple'])}",
        "",
        "4. PERDIDA DE PAQUETES",
        f"Valor observado: {perdida['valor']:.2f} %",
        f"Cobertura: {perdida['cobertura']:.2f} %",
        f"Veredicto: {veredicto_perdida}",
        "",
        "5. THROUGHPUT",
        f"Cantidad de pruebas: {throughput['cantidad_pruebas']}",
        f"Promedio: {throughput['promedio']:.2f} Mbps",
        f"Veredicto: {texto_veredicto(throughput['cumple'])}",
        "",
        "6. TIEMPO DE RESPUESTA",
        f"Tiempo maximo: {respuesta['maximo']} minutos",
        f"Incumplimientos: {len(respuesta['incumplimientos'])}",
        f"Veredicto: {texto_veredicto(respuesta['cumple'])}",
        "",
        "7. MTTR",
        f"Mayor restauracion: {mttr['maximo']} minutos",
        f"Veredicto: {texto_veredicto(mttr['cumple'])}",
        "",
        "8. CREDITO",
        f"Credito por disponibilidad: {credito['disponibilidad']:.0f} %",
        f"Credito por respuesta: {credito['respuesta']:.0f} %",
        f"Credito total: {credito['total']:.0f} %",
        f"Monto neto: ${credito['monto']:,.0f} CLP".replace(",", "."),
    ]

    return "\n".join(lineas)


def main():
    if len(sys.argv) > 1:
        ruta_csv = Path(sys.argv[1])
    else:
        raiz = Path(__file__).resolve().parent.parent
        ruta_csv = (
            raiz
            / "ejemplos"
            / "caso-valle-elqui"
            / "mediciones.csv"
        )

    if not ruta_csv.exists():
        print(f"Error: no se encontro el archivo {ruta_csv}")
        return 1

    registros = cargar_mediciones(ruta_csv)
    salida = generar_salida(registros)
    print(salida)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
