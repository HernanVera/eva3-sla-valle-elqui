PYTHON ?= python3

CASO := ejemplos/caso-valle-elqui
MEDICIONES := $(CASO)/mediciones.csv
SALIDA := $(CASO)/salida_calc.txt
INFORME_MD := $(CASO)/informe.md
INFORME_PDF := $(CASO)/informe.pdf

CALCULADORA := herramientas/calc_sla.py
GENERADOR := herramientas/generar_informe.py

.PHONY: ayuda calcular informe todo verificar limpiar

ayuda:
	@echo "Comandos disponibles:"
	@echo "  make calcular  - Ejecuta la calculadora y genera salida_calc.txt"
	@echo "  make informe   - Genera informe.pdf desde informe.md"
	@echo "  make todo      - Ejecuta cálculos y genera el PDF"
	@echo "  make verificar - Comprueba los archivos principales"
	@echo "  make limpiar   - Elimina los archivos generados"

calcular:
	$(PYTHON) $(CALCULADORA) $(MEDICIONES) > $(SALIDA)
	@echo "Resultados guardados en $(SALIDA)"

informe:
	$(PYTHON) $(GENERADOR)

todo: calcular informe
	@echo "Proceso completo finalizado."

verificar:
	@test -f $(MEDICIONES)
	@test -f $(CASO)/objetivos.yaml
	@test -f $(CASO)/sla.md
	@test -f $(SALIDA)
	@test -f $(INFORME_MD)
	@test -f $(INFORME_PDF)
	@$(PYTHON) -m py_compile $(CALCULADORA)
	@$(PYTHON) -m py_compile $(GENERADOR)
	@echo "Verificación completada correctamente."

limpiar:
	rm -f $(SALIDA) $(INFORME_PDF)
	@echo "Archivos generados eliminados."
