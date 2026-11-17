Acuerdo de Nivel de Servicio
1. Identificación
Cliente: Agrícola Valle de Elqui SpA
Proveedor: NorteNet Telecomunicaciones
Servicio: Internet dedicado simétrico de 200 Mbps
Período evaluado: septiembre de 2026
Duración del período: 30 días
Minutos totales del período: 43.200 minutos
Punto de demarcación: puerto LAN del CPE instalado en la planta de Vicuña
2. Objetivos del SLA
Métrica	Objetivo contractual	Método de medición
Disponibilidad mensual	≥ 99,9 %	Minutos de indisponibilidad atribuibles al proveedor
Latencia RTT promedio	≤ 30 ms	ICMP cada 60 segundos desde el CPE
Jitter promedio	≤ 10 ms	TWAMP desde la demarcación
Pérdida de paquetes	≤ 0,5 %	TWAMP desde la demarcación
Throughput promedio	≥ 180 Mbps	Cuatro pruebas iperf3 TCP
Tiempo de respuesta	≤ 60 minutos	Desde apertura del ticket hasta primera respuesta
MTTR por incidente	≤ 240 minutos	Incidentes atribuibles al proveedor
Cobertura de medición	≥ 90 %	Muestras válidas respecto de las esperadas
3. Exclusiones contractuales
Se excluyen del cálculo de indisponibilidad:

Mantenciones programadas notificadas con al menos 72 horas de anticipación.
Mantenciones programadas con una duración acumulada máxima de cuatro horas mensuales.
Interrupciones causadas por equipos o condiciones bajo responsabilidad del cliente.
Cortes eléctricos en dependencias del cliente cuando el respaldo eléctrico sea responsabilidad del cliente.
Eventos de fuerza mayor debidamente acreditados.
El tiempo correspondiente a eventos excluidos se considera disponible para el cálculo mensual.

4. Créditos de servicio
Los créditos se determinan de acuerdo con el nivel de incumplimiento contractual:

Disponibilidad entre 99,5 % y menos de 99,9 %: crédito de 10 %.
Incumplimiento del tiempo máximo de respuesta: crédito adicional de 5 %.
Crédito máximo acumulado: 50 % del cargo mensual.
Cargo mensual neto: $1.200.000.
5. Criterio de validación
Una métrica se considera válida cuando:

Se utiliza el método establecido en el contrato.
La medición se realiza desde el punto de demarcación correspondiente.
Se emplea el estadístico contractual.
La cobertura mensual alcanza como mínimo el 90 %.
Existe trazabilidad suficiente para reproducir el cálculo.
