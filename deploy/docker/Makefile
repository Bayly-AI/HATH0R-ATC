# Hath0r Docker group — compose project name: hath0r
SHELL := /bin/bash
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)
COMPOSE := docker compose -f $(ROOT)/deploy/docker/docker-compose.yml
NETWORK_NAME ?= hath0r-net
POSTGRES_VOLUME ?= hath0r_postgres_data
HATH0R_NGINX_HOST_PORT ?= 38000

.PHONY: help network-ensure volume-ensure up up-shared up-db down ps logs status redis-cli smoke

help:
	@echo "Hath0r Docker group (project: hath0r, network: $(NETWORK_NAME))"
	@echo "  make up          - network + hath0r-redis + hath0r-nginx"
	@echo "  make up-db       - shared + hath0r-postgres"
	@echo "  make down        - stop group containers created by this compose file"
	@echo "  make ps | logs | status | smoke"
	@echo "  Edge: http://localhost:$(HATH0R_NGINX_HOST_PORT)/"
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
			--label com.hath0r.container=hath0r-postgres \
			--label com.hath0r.role=canonical-database \
			$(POSTGRES_VOLUME)
	@echo "✓ volume $(POSTGRES_VOLUME)"

up-shared: network-ensure
	@HATH0R_NGINX_HOST_PORT=$(HATH0R_NGINX_HOST_PORT) $(COMPOSE) up -d redis nginx
	@echo "✓ hath0r-redis + hath0r-nginx (group hath0r) on :$(HATH0R_NGINX_HOST_PORT)"

up: up-shared

up-db: volume-ensure up-shared
	@$(COMPOSE) --profile db up -d postgres
	@echo "✓ hath0r-postgres in group hath0r"

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
		&& echo "✓ hath0r-nginx healthz :$(HATH0R_NGINX_HOST_PORT)" \
		|| echo "⚠ hath0r-nginx healthz unreachable"
	@docker inspect hath0r-mcp >/dev/null 2>&1 \
		&& echo "✓ standalone hath0r-mcp present on host" \
		|| echo "· hath0r-mcp not running (optional; start from ../hath0r-mcp)"

redis-cli:
	@docker exec -it hath0r-redis redis-cli

smoke:
	@$(ROOT)/deploy/docker/smoke-test.sh
