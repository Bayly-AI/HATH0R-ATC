# Hath0r Docker group — compose project name: hath0r
SHELL := /bin/bash
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)
COMPOSE := docker compose -f $(ROOT)/deploy/docker/docker-compose.yml
NETWORK_NAME ?= hath0r-net
POSTGRES_VOLUME ?= hath0r_postgres_data
PHOENIX_VOLUME ?= hath0r_phoenix_data
MLFLOW_VOLUME ?= hath0r_mlflow_data
HATH0R_NGINX_HOST_PORT ?= 38000

.PHONY: help network-ensure volume-ensure up up-shared up-db down ps logs status redis-cli smoke

help:
	@echo "Hath0r Docker group (project: hath0r, network: $(NETWORK_NAME))"
	@echo "  make up          - network + Hath0r-Sessions + Hath0r-Edge + Hath0r-phoenix + Hathor-MLFLOW"
	@echo "  make up-db       - shared + Hath0r-Data"
	@echo "  make down        - stop group containers created by this compose file"
	@echo "  make ps | logs | status | smoke"
	@echo "  Edge: http://localhost:$(HATH0R_NGINX_HOST_PORT)/"
	@echo "  Phoenix: http://localhost:$(HATH0R_NGINX_HOST_PORT)/phoenix/ (direct :36006)"
	@echo "  MLflow: http://localhost:$(HATH0R_NGINX_HOST_PORT)/mlflow/ (direct :35000)"
	@echo "  MCP (standalone): make -C ../hath0r-mcp docker-up"

network-ensure:
	@docker network inspect $(NETWORK_NAME) >/dev/null 2>&1 || \
		docker network create \
			--label com.hath0r.org=bayly-ai \
			--label com.hath0r.project=hath0r-opensource \
			--label com.hath0r.component=network \
			$(NETWORK_NAME)
	@echo "✓ network $(NETWORK_NAME)"

volume-ensure:
	@docker volume inspect $(POSTGRES_VOLUME) >/dev/null 2>&1 || \
		docker volume create \
			--label com.hath0r.component=postgres \
			--label com.hath0r.container=Hath0r-Data \
			--label com.hath0r.role=canonical-database \
			$(POSTGRES_VOLUME)
	@echo "✓ volume $(POSTGRES_VOLUME)"
	@docker volume inspect $(PHOENIX_VOLUME) >/dev/null 2>&1 || \
		docker volume create \
			--label com.hath0r.component=phoenix \
			--label com.hath0r.container=Hath0r-phoenix \
			--label com.hath0r.role=observability \
			$(PHOENIX_VOLUME)
	@echo "✓ volume $(PHOENIX_VOLUME)"
	@docker volume inspect $(MLFLOW_VOLUME) >/dev/null 2>&1 || \
		docker volume create \
			--label com.hath0r.component=mlflow \
			--label com.hath0r.container=Hathor-MLFLOW \
			--label com.hath0r.role=mlops-experiment-tracking \
			$(MLFLOW_VOLUME)
	@echo "✓ volume $(MLFLOW_VOLUME)"

up-shared: network-ensure volume-ensure
	@HATH0R_NGINX_HOST_PORT=$(HATH0R_NGINX_HOST_PORT) $(COMPOSE) up -d redis nginx phoenix mlflow
	@echo "✓ Hath0r-Sessions + Hath0r-Edge + Hath0r-phoenix + Hathor-MLFLOW (group hath0r) on :$(HATH0R_NGINX_HOST_PORT)"

up: up-shared

up-db: volume-ensure up-shared
	@$(COMPOSE) --profile db up -d postgres
	@echo "✓ Hath0r-Data in group hath0r"

down:
	@$(COMPOSE) --profile db down
	@echo "✓ compose stack stopped (named volumes retained)"

ps:
	@$(COMPOSE) ps -a
	@echo "--- group filter ---"
	@docker ps -a --filter label=com.docker.compose.project=hath0r --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'

logs:
	@$(COMPOSE) logs -f --tail=200

status:
	@echo "=== Hath0r Docker group ==="
	@docker network inspect $(NETWORK_NAME) >/dev/null 2>&1 && echo "✓ $(NETWORK_NAME)" || echo "✗ $(NETWORK_NAME) missing"
	@docker ps -a --filter label=com.docker.compose.project=hath0r --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'
	@curl -fsS "http://localhost:$(HATH0R_NGINX_HOST_PORT)/healthz" >/dev/null 2>&1 \
		&& echo "✓ Hath0r-Edge healthz :$(HATH0R_NGINX_HOST_PORT)" \
		|| echo "⚠ Hath0r-Edge healthz unreachable"
	@(docker inspect Hath0r-MCP >/dev/null 2>&1 || docker inspect hath0r-mcp >/dev/null 2>&1) \
		&& echo "✓ standalone Hath0r-MCP present on host" \
		|| echo "· Hath0r-MCP not running (optional; start from ../hath0r-mcp)"

redis-cli:
	@(docker exec -it Hath0r-Sessions redis-cli 2>/dev/null || docker exec -it hath0r-redis redis-cli)

smoke:
	@$(ROOT)/deploy/docker/smoke-test.sh
