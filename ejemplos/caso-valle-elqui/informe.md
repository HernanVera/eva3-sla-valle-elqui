# Informe de Verificación del Acuerdo de Nivel de Servicio

## EVA 3: Caso Agrícola Valle de Elqui SpA

---

## 1. Identificación

| Elemento | Información |
|---|---|
| Cliente | Agrícola Valle de Elqui SpA |
| Proveedor | NorteNet Telecomunicaciones |
| Servicio | Internet dedicado simétrico de 200 Mbps |
| Período evaluado | Septiembre de 2026 |
| Duración del período | 30 días |
| Minutos totales | 43.200 minutos |
| Cargo mensual neto | $1.200.000 CLP |
| Punto de demarcación | Puerto LAN del CPE instalado en la planta de Vicuña |

---

## 2. Resumen ejecutivo

El presente informe verifica el cumplimiento del Acuerdo de Nivel de Servicio, SLA, correspondiente al servicio de Internet dedicado de 200 Mbps contratado por Agrícola Valle de Elqui SpA a NorteNet Telecomunicaciones durante septiembre de 2026.

La evaluación considera disponibilidad, latencia, jitter, pérdida de paquetes, throughput, tiempo de respuesta y tiempo medio de restauración. Además, se revisa la validez de las evidencias según el método de medición, punto de demarcación, estadístico contractual y cobertura mensual.

El resultado determina que el servicio no cumplió globalmente el SLA. La disponibilidad mensual alcanzó un 99,63 %, inferior al objetivo de 99,9 %. También se detectó un incumplimiento en el tiempo de respuesta del ticket INC-2672, cuya primera respuesta demoró 66 minutos frente al máximo contractual de 60 minutos.

La latencia, el jitter, el throughput y el MTTR cumplen los respectivos objetivos. La pérdida de paquetes presenta evidencia insuficiente debido a que la medición del cliente cubrió aproximadamente el 60 % del período, porcentaje inferior al mínimo de 90 % exigido.

Los incumplimientos acreditados generan un crédito total de 15 % sobre el cargo mensual. El monto correspondiente es de $180.000 CLP netos. No existe fundamento técnico ni contractual para solicitar el crédito máximo de 50 %.

---

## 3. Alcance y referencias

### 3.1 Alcance

La verificación comprende el período entre el 1 y el 30 de septiembre de 2026. Se consideran las mediciones realizadas desde el punto de demarcación contractual, los registros de indisponibilidad, las pruebas de rendimiento y los datos del sistema de tickets.

La evaluación incluye:

- Clasificación de eventos de indisponibilidad.
- Cálculo de disponibilidad mensual.
- Evaluación de latencia RTT promedio.
- Cálculo de jitter mensual ponderado.
- Revisión de pérdida de paquetes.
- Cálculo de throughput promedio.
- Verificación de tiempos de respuesta.
- Verificación del MTTR.
- Cálculo de créditos de servicio.
- Evaluación de viabilidad de la infraestructura.

### 3.2 Archivos de referencia

Los antecedentes y resultados reproducibles se encuentran en:

- `sla.md`: descripción del acuerdo de nivel de servicio.
- `objetivos.yaml`: objetivos y umbrales contractuales.
- `mediciones.csv`: registros utilizados en los cálculos.
- `calc_sla.py`: calculadora automatizada del SLA.
- `salida_calc.txt`: salida generada por la calculadora.
- `informe.md`: informe técnico en formato Markdown.

### 3.3 Objetivos contractuales

| Métrica | Objetivo |
|---|---:|
| Disponibilidad mensual | Mayor o igual a 99,9 % |
| Latencia RTT promedio | Menor o igual a 30 ms |
| Jitter promedio mensual | Menor o igual a 10 ms |
| Pérdida de paquetes | Menor o igual a 0,5 % |
| Throughput promedio | Mayor o igual a 180 Mbps |
| Tiempo de respuesta | Menor o igual a 60 minutos en todos los incidentes |
| MTTR | Menor o igual a 240 minutos por incidente |
| Cobertura mínima | Mayor o igual a 90 % |

---

## 4. Metodología

### 4.1 Validación de evidencia

Cada evidencia se revisó considerando los siguientes criterios:

1. Correspondencia con el método establecido en el contrato.
2. Medición desde el punto de demarcación aplicable.
3. Uso del estadístico contractual.
4. Cobertura mensual mínima de 90 %.
5. Disponibilidad de antecedentes suficientes para reproducir el cálculo.

Una evidencia que no cumple estos criterios no se utiliza para acreditar cumplimiento o incumplimiento.

### 4.2 Disponibilidad

La disponibilidad mensual se calculó mediante la expresión:

```text
Disponibilidad =
(Minutos del período - Minutos de caída atribuibles)
----------------------------------------------------
                Minutos del período
                         × 100
```

Los eventos excluidos se consideran tiempo disponible, de acuerdo con las reglas contractuales.

### 4.3 Jitter ponderado

Debido a que cada semana contiene una cantidad diferente de muestras, se utilizó un promedio ponderado:

```text
Jitter ponderado =
Suma de cada jitter semanal multiplicado por sus muestras
----------------------------------------------------------
                  Total de muestras válidas
```

### 4.4 Throughput

Se utilizaron cuatro pruebas válidas realizadas mediante iperf3 TCP desde el puerto LAN del CPE. El resultado contractual corresponde al promedio de las pruebas válidas.

### 4.5 Tiempo de respuesta

El tiempo de respuesta se calculó desde la apertura de cada ticket hasta la primera respuesta registrada por el proveedor.

---

## 5. Resultados

### 5.1 Clasificación de las interrupciones

| Evento | Fecha | Duración | Causa | Clasificación |
|---|---|---:|---|---|
| E1 | 03-09-2026 | 210 min | Mantención programada avisada con más de 72 horas | Excluido |
| E2 | 09-09-2026 | 55 min | Corte de fibra por obras viales en el acceso | Atribuible |
| E3 | 15-09-2026 | 105 min | Corte eléctrico en planta del cliente sin UPS | Excluido |
| E4 | 21-09-2026 | 75 min | Falla de tarjeta de línea en el PE La Serena | Atribuible |
| E5 | 27-09-2026 | 30 min | Mantención avisada con 14 horas y 30 minutos | Atribuible |

Los minutos atribuibles al proveedor son:

```text
55 + 75 + 30 = 160 minutos
```

E1 se excluye porque cumple el aviso mínimo de 72 horas y se encuentra dentro del máximo de mantención programada. E3 se excluye porque corresponde a una falla eléctrica en dependencias del cliente, cuyo respaldo era responsabilidad del cliente.

E5 se considera atribuible porque el aviso se entregó solamente 14 horas y 30 minutos antes de la intervención, plazo inferior a las 72 horas requeridas.

### 5.2 Disponibilidad

```text
Disponibilidad = ((43.200 - 160) / 43.200) × 100
Disponibilidad = 99,63 %
```

La caída máxima permitida para cumplir 99,9 % es:

```text
Caída permitida = 43.200 × (1 - 0,999)
Caída permitida = 43,20 minutos
```

El exceso de indisponibilidad es:

```text
Exceso = 160 - 43,20
Exceso = 116,80 minutos
```

**Veredicto: NO CUMPLE.**

La disponibilidad se encuentra entre 99,5 % y menos de 99,9 %, por lo que corresponde un crédito de 10 %.

### 5.3 Latencia

La medición contractual presenta:

- Promedio mensual: 27,40 ms.
- Muestras válidas: 42.725.
- Muestras esperadas: 43.200.
- Cobertura: 98,90 %.
- Límite contractual: 30 ms.

```text
27,40 ms ≤ 30 ms
```

**Veredicto: CUMPLE.**

El máximo de 118 ms no determina incumplimiento, porque el estadístico contractual es el promedio mensual. La medición de 22,1 ms presentada por el proveedor no se utiliza, debido a que fue realizada entre el PE y el núcleo de la red y no desde la demarcación contractual.

### 5.4 Jitter

Las mediciones semanales fueron:

| Semana | Jitter | Muestras |
|---|---:|---:|
| 1 | 9,0 ms | 9.870 |
| 2 | 10,5 ms | 10.025 |
| 3 | 13,8 ms | 9.900 |
| 4 | 7,2 ms | 12.930 |

El promedio ponderado es:

```text
Jitter =
((9,0 × 9.870) + (10,5 × 10.025) +
(13,8 × 9.900) + (7,2 × 12.930)) / 42.725

Jitter = 9,92 ms
```

La cobertura es de 98,90 %.

```text
9,92 ms ≤ 10 ms
```

**Veredicto: CUMPLE.**

El margen de cumplimiento es de solamente 0,08 ms, por lo que esta métrica requiere seguimiento.

### 5.5 Pérdida de paquetes

La medición del cliente registró 0,31 %, pero solamente cubrió desde el 1 hasta el 18 de septiembre. El colector dejó de funcionar por falta de espacio en disco y no fue recuperado durante el período.

```text
Cobertura aproximada = (18 / 30) × 100
Cobertura aproximada = 60 %
```

La cobertura mínima requerida es de 90 %.

La medición del proveedor, de 0,18 %, tampoco resulta válida para el SLA porque fue realizada entre el PE y el núcleo de la red y no desde el punto de demarcación mediante TWAMP.

**Veredicto: EVIDENCIA INSUFICIENTE.**

No corresponde declarar cumplimiento ni incumplimiento de esta métrica.

### 5.6 Throughput

El objetivo mínimo corresponde al 90 % de 200 Mbps:

```text
Objetivo = 200 × 0,90
Objetivo = 180 Mbps
```

Pruebas válidas:

| Prueba | Resultado |
|---|---:|
| THR-01 | 186 Mbps |
| THR-02 | 182 Mbps |
| THR-03 | 171 Mbps |
| THR-04 | 184 Mbps |

Promedio:

```text
Throughput = (186 + 182 + 171 + 184) / 4
Throughput = 180,75 Mbps
```

```text
180,75 Mbps ≥ 180 Mbps
```

**Veredicto: CUMPLE.**

El resultado de 95 Mbps obtenido mediante Speedtest no se utiliza, porque la prueba se realizó desde un notebook conectado por Wi-Fi y no mediante iperf3 desde el puerto LAN del CPE.

### 5.7 Tiempo de respuesta

| Ticket | Apertura | Primera respuesta | Tiempo | Resultado |
|---|---:|---:|---:|---|
| INC-2611 | 14:18 | 14:41 | 23 min | Cumple |
| INC-2648 | 10:47 | 11:20 | 33 min | Cumple |
| INC-2672 | 22:09 | 23:15 | 66 min | No cumple |
| INC-2690 | 08:33 | 08:40 | 7 min | Cumple |

El SLA exige respuesta dentro de 60 minutos en el 100 % de los incidentes. INC-2672 excedió el límite en 6 minutos.

**Veredicto: NO CUMPLE.**

Este incumplimiento genera un crédito adicional de 5 %.

### 5.8 MTTR

Los eventos atribuibles al proveedor tuvieron las siguientes duraciones:

| Evento | Restauración |
|---|---:|
| E2 | 55 min |
| E4 | 75 min |
| E5 | 30 min |

El límite contractual es de 240 minutos por incidente. El valor máximo observado fue de 75 minutos.

```text
75 minutos ≤ 240 minutos
```

**Veredicto: CUMPLE.**

### 5.9 Matriz consolidada

| Métrica | Objetivo | Resultado | Veredicto | Crédito |
|---|---:|---:|---|---:|
| Disponibilidad | ≥ 99,9 % | 99,63 % | No cumple | 10 % |
| Latencia | ≤ 30 ms | 27,40 ms | Cumple | 0 % |
| Jitter | ≤ 10 ms | 9,92 ms | Cumple | 0 % |
| Pérdida | ≤ 0,5 % | Cobertura 60 % | Evidencia insuficiente | 0 % |
| Throughput | ≥ 180 Mbps | 180,75 Mbps | Cumple | 0 % |
| Respuesta | ≤ 60 min | Máximo 66 min | No cumple | 5 % |
| MTTR | ≤ 240 min | Máximo 75 min | Cumple | 0 % |

---

## 6. Análisis de incumplimientos y créditos

### 6.1 Crédito por disponibilidad

La disponibilidad de 99,63 % se encuentra en el tramo comprendido entre 99,5 % y menos de 99,9 %.

```text
Crédito por disponibilidad = 10 %
```

### 6.2 Crédito por tiempo de respuesta

Uno de los cuatro incidentes superó el máximo de 60 minutos.

```text
Crédito por tiempo de respuesta = 5 %
```

### 6.3 Crédito total

```text
Crédito total = 10 % + 5 %
Crédito total = 15 %
```

El monto correspondiente es:

```text
Monto = $1.200.000 × 0,15
Monto = $180.000 CLP netos
```

El crédito acumulado se encuentra bajo el máximo contractual de 50 %.

**Crédito procedente: 15 %, equivalente a $180.000 CLP netos.**

---

## 7. Conclusiones técnicas

1. El servicio no cumplió globalmente el SLA de septiembre de 2026.
2. La disponibilidad fue de 99,63 %, con 160 minutos de indisponibilidad atribuible.
3. La indisponibilidad excedió en 116,80 minutos el máximo permitido.
4. La latencia promedio mensual de 27,40 ms cumple el límite de 30 ms.
5. El jitter ponderado de 9,92 ms cumple, pero presenta un margen reducido.
6. La pérdida de paquetes no puede evaluarse por falta de cobertura suficiente.
7. El throughput promedio de 180,75 Mbps cumple el mínimo contractual.
8. El ticket INC-2672 incumplió el tiempo de respuesta por 6 minutos.
9. El MTTR máximo fue de 75 minutos y cumple el límite de 240 minutos.
10. Corresponde un crédito total de 15 %, equivalente a $180.000 CLP netos.
11. No corresponde solicitar el crédito máximo de 50 %.

### 7.1 Viabilidad de la infraestructura

La disponibilidad teórica de los componentes actuales conectados en serie es:

```text
CPE:              99,95 %
Fibra de acceso:  99,80 %
PE La Serena:     99,99 %
Backbone:         99,99 %
```

```text
Disponibilidad en serie =
0,9995 × 0,9980 × 0,9999 × 0,9999

Disponibilidad en serie = 99,7302 %
```

La arquitectura actual no permite sostener teóricamente el objetivo de 99,9 %.

Al incorporar un radioenlace independiente de 99,5 % en paralelo con la fibra:

```text
Disponibilidad del acceso =
1 - ((1 - 0,9980) × (1 - 0,9950))

Disponibilidad del acceso = 99,999 %
```

La disponibilidad total estimada sería:

```text
Disponibilidad total =
0,9995 × 0,99999 × 0,9999 × 0,9999

Disponibilidad total = 99,9290 %
```

Con respaldo independiente, el objetivo de 99,9 % se vuelve técnicamente viable.

---

## 8. Recomendaciones

### 8.1 Recomendaciones para el proveedor

1. Incorporar un radioenlace de respaldo con diversidad real respecto del trazado de fibra.
2. Configurar conmutación automática mediante rutas dinámicas, seguimiento de estado o SD-WAN.
3. Evitar que el enlace principal y el respaldo compartan ductos, energía, PE o puntos únicos de falla.
4. Revisar el proceso de mantenciones de emergencia y formalizar avisos con al menos 72 horas cuando corresponda.
5. Configurar alertas del sistema de tickets antes de los 45 minutos para evitar superar el límite de 60 minutos.
6. Mantener mediciones contractuales desde el punto de demarcación y no solamente desde la red interna del proveedor.

### 8.2 Recomendaciones para el cliente

1. Instalar una UPS para el CPE y los equipos de monitoreo.
2. Configurar alertas por capacidad de disco para evitar la detención del colector TWAMP.
3. Mantener una cobertura mensual superior al 90 % para todas las métricas.
4. Ejecutar las pruebas de rendimiento mediante cable Ethernet desde la demarcación.
5. No utilizar pruebas Wi-Fi o Speedtest como evidencia principal del SLA.
6. Conservar registros de tickets, avisos de mantención y resultados de monitoreo.
7. Revisar mensualmente las métricas cercanas al límite, especialmente jitter y throughput.

### 8.3 Prioridades propuestas

| Prioridad | Acción | Plazo recomendado |
|---|---|---|
| Alta | Corregir monitoreo TWAMP y alertas de disco | Inmediato |
| Alta | Solicitar crédito de $180.000 CLP | Dentro del plazo contractual |
| Alta | Implementar alerta previa al límite de respuesta | 30 días |
| Media | Instalar UPS en el CPE | 30 días |
| Media | Diseñar radioenlace de respaldo independiente | 60 a 90 días |
| Baja | Revisar trimestralmente jitter y throughput | Trimestral |

---

## 9. Automatización y reproducibilidad

### 9.1 Datos de entrada

La automatización utiliza los siguientes archivos:

- `objetivos.yaml`: contiene los umbrales y condiciones contractuales.
- `mediciones.csv`: contiene los eventos y mediciones del período.
- `calc_sla.py`: procesa las mediciones y calcula los resultados.

### 9.2 Ejecución

Desde la raíz del repositorio se ejecuta:

```bash
python herramientas/calc_sla.py
```

Para guardar la salida:

```bash
python herramientas/calc_sla.py > ejemplos/caso-valle-elqui/salida_calc.txt
```

### 9.3 Control de versiones

El trabajo se desarrolla en la rama:

```text
caso/valle-elqui
```

Los cambios se registran mediante commits descriptivos y se sincronizan con GitHub mediante `git push`.

### 9.4 Trazabilidad

Los resultados numéricos incluidos en el informe pueden verificarse mediante:

- Los datos de `mediciones.csv`.
- Los objetivos del archivo `objetivos.yaml`.
- El código fuente de `calc_sla.py`.
- La salida reproducible `salida_calc.txt`.

### 9.5 Declaración de uso de inteligencia artificial

Se utilizó Microsoft Copilot como herramienta de apoyo para organizar la estructura del repositorio, revisar la redacción técnica, proponer el código de automatización y comprobar los procedimientos de cálculo.

Los antecedentes del caso, las métricas, los resultados y las conclusiones fueron revisados mediante los archivos de entrada y la ejecución de la calculadora. La inteligencia artificial no reemplazó la validación técnica ni la ejecución reproducible de los cálculos.

---

## 10. Anexos

### Anexo A: eventos atribuibles

```text
E2 = 55 minutos
E4 = 75 minutos
E5 = 30 minutos
Total = 160 minutos
```

### Anexo B: disponibilidad

```text
((43.200 - 160) / 43.200) × 100 = 99,63 %
```

### Anexo C: jitter ponderado

```text
((9,0 × 9.870) + (10,5 × 10.025) +
(13,8 × 9.900) + (7,2 × 12.930)) / 42.725
= 9,92 ms
```

### Anexo D: throughput

```text
(186 + 182 + 171 + 184) / 4 = 180,75 Mbps
```

### Anexo E: crédito

```text
10 % + 5 % = 15 %
$1.200.000 × 15 % = $180.000 CLP
```

---

**Resultado final:** el servicio no cumple globalmente el SLA y corresponde un crédito de 15 %, equivalente a $180.000 CLP netos.
