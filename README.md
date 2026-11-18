# EVA 3: Verificación de SLA

Repositorio académico para verificar el cumplimiento del Acuerdo de Nivel de Servicio del caso **Agrícola Valle de Elqui SpA**, correspondiente a septiembre de 2026.

## Resultado principal

- Disponibilidad mensual: **99,63 %**, no cumple.
- Latencia promedio: **27,40 ms**, cumple.
- Jitter ponderado: **9,92 ms**, cumple.
- Pérdida de paquetes: evidencia insuficiente por cobertura de 60 %.
- Throughput promedio: **180,75 Mbps**, cumple.
- Tiempo máximo de respuesta: **66 minutos**, no cumple.
- MTTR máximo: **75 minutos**, cumple.
- Crédito procedente: **15 %**.
- Monto del crédito: **$180.000 CLP netos**.

## Archivos principales

- `herramientas/calc_sla.py`: calcula los indicadores.
- `herramientas/generar_informe.py`: genera el PDF.
- `ejemplos/caso-valle-elqui/objetivos.yaml`: objetivos contractuales.
- `ejemplos/caso-valle-elqui/mediciones.csv`: mediciones del caso.
- `ejemplos/caso-valle-elqui/salida_calc.txt`: resultados generados.
- `ejemplos/caso-valle-elqui/informe.md`: informe técnico.
- `ejemplos/caso-valle-elqui/informe.pdf`: entrega final.

## Requisitos

- Python 3
- GNU Make
- Pandoc
- wkhtmltopdf

## Ejecución

```bash
make ayuda
make calcular
make informe
make todo
make verificar
