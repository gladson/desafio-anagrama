help:
	@echo "Setup Help"
	@echo
	@echo  "used: make <subcommand>"
	@echo  "subcommand used:"
	@echo  "    run_desafio""					""Rodar o projeto"
	@echo  "    run_test""					""Rodar teste de cobertura de codigo e pytest com modular fixture"
	@echo  "    run_test_to_html""				""Exportar teste de cobertura de codigo em uma pasta 'htmlcov'"
	@echo  ""

run_desafio:
	python desafio_anagrama/main.py

run_flake8_isort:
	flake8 desafio_anagrama/*.*
	isort **/*.py

run_test: run_flake8_isort
	pytest --cov-append --cov=desafio_anagrama tests/

run_test_to_html:
	rm -rf htmlcov
	pytest --cov-report html --cov=desafio_anagrama tests/