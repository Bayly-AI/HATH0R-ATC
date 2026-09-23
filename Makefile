# Hath0r ATC — OpenSource control tower operator entry
.PHONY: help docker-up docker-up-db docker-down docker-ps docker-status docker-logs smoke bootstrap

help:
	@echo "Hath0r ATC (control tower)"
	@echo "  make docker-up       - hath0r group: hath0r-redis + hath0r-nginx"
	@echo "  make docker-up-db    - shared + hath0r-postgres"
	@echo "  make docker-down | docker-ps | docker-status | docker-logs"
	@echo "  make smoke           - edge + redis smoke test"
	@echo "  make bootstrap       - layout/identity checks"

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
