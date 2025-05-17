POETRY_VERSION = $(shell poetry version --short)
ST_PORT=8080

.PHONY: help
help:
	@echo "******* COMMANDS AVAILABLE ON THIS MAKEFILE *******"
	@echo
	@echo "build_frontend: build excalidata streamlit frontend image."
	@echo "run_frontend: run excalidata frontend container in dev."
	@echo "stop_frontend: stop excalidata frontend container in dev."
	@echo "remove_frontend: remove excalidata frontend container in dev."
	@echo "logs_frontend: open excalidata streamlit logs."
	@echo "stopremove_frontend: stop and remove excalidata frontend container in dev."
	@echo
	@echo "***************************************************"

.PHONY: npm_build
npm_build:
	cd st_mui_table/frontend; npm run build

.PHONY: run_app
run_app:
	@echo "--server.port is et to $(ST_PORT)"
	streamlit run app.py --server.port $(ST_PORT)

.PHONY: run_poc_app
run_poc_app:
	@echo "--server.port is et to $(ST_PORT)"
	streamlit run poc_app.py --server.port $(ST_PORT)

.PHONY: build
build:
	@poetry build -f wheel

.PHONY: deploy-dev-nexus
deploy-dev-nexus: build
	poetry config repositories.ifood-data-pypi-dev http://nexus.aws-data-prd.dc-ifood.com/repository/ifood-data-private-dev-pypi/
	poetry publish -r ifood-data-pypi-dev --username "anonymous" -n

.PHONY: deploy-nexus
deploy-nexus: build
	@echo "Publishing to nexus..."
	@echo Publishing to nexus...
	@poetry publish --repository ifood-data-private-pypi --username "$(POETRY_NEXUS_USER)" --password "$(POETRY_NEXUS_PASSWORD)"

