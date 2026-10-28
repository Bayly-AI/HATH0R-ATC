.PHONY: help test test-pre-deploy test-post-deploy docker-up docker-up-db docker-down docker-ps docker-status docker-logs smoke bootstrap

help:
	@echo "Hath0r ATC (control tower)"
	@echo "  make test            - Unit/contract tests"
	@echo "  make test-pre-deploy - Tests with coverage XML generation"
	@echo "  make test-post-deploy- Smoke/health checks"
	@echo "  make docker-up       - hath0r group: Hath0r-Sessions + Hath0r-Edge + Hath0r-phoenix + Hathor-MLFLOW + Hath0r-Cruise-Control"
	@echo "  make docker-up-db    - shared + Hath0r-Data"
	@echo "  make docker-down | docker-ps | docker-status | docker-logs"
	@echo "  make smoke           - edge + redis smoke test"
	@echo "  make bootstrap       - layout/identity checks"

test:
	python3 -m pytest -v

test-pre-deploy:
	python3 -m pytest -v --cov=. --cov-report=xml

test-post-deploy:
	@./deploy/docker/smoke-test.sh

docker-up:
	@$(MAKE) -C deploy/docker up

docker-up-db:
	@$(MAKE) -C deploy/docker up-db

docker-down:
	@$(MAKE) -C deploy/docker down

docker-ps:
	@$(MAKE) -C deploy/docker ps

docker-status:
	@$(MAKE) -C deploy/docker status

docker-logs:
	@$(MAKE) -C deploy/docker logs

smoke:
	@./deploy/docker/smoke-test.sh

bootstrap:
	@./bin/hath0r-bootstrap.sh

