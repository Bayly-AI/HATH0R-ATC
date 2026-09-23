#!/usr/bin/env bash
# Minimal post-init checks for HATH0R ATC control tower.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> HATHOR fileset bootstrap: HATH0R ATC (hath0r-atc)"
echo "    root: $ROOT"

# Resolve hath0r CLI (optional but preferred)
HATH0R_BIN=""
if command -v hath0r >/dev/null 2>&1 && hath0r --version >/dev/null 2>&1; then
  HATH0R_BIN="hath0r"
elif [[ -d "/Users/raybayly/Development/OpenSource/hathor-cli/src" ]]; then
  HATH0R_BIN="python3 -m hath0r_cli.cli"
  export PYTHONPATH="/Users/raybayly/Development/OpenSource/hathor-cli/src:${PYTHONPATH:-}"
fi

if [[ -n "$HATH0R_BIN" ]]; then
  echo "==> hath0r --version"
  $HATH0R_BIN --version || true
else
  echo "==> hath0r CLI not on PATH (optional for ATC infra bootstrap)"
fi

export HATH0R_GROUP_ROOT="${HATH0R_GROUP_ROOT:-/Users/raybayly/Development/OpenSource}"
echo "==> HATH0R_GROUP_ROOT=${HATH0R_GROUP_ROOT}"

echo "==> Verifying ATC identity + deploy layout"
test -f cfg/product.yaml
test -f cfg/suite.yaml
test -f cfg/control-tower.yaml
test -f cfg/knowledge-tower.yaml
test -f cfg/products.yaml
test -f deploy/docker/docker-compose.yml
test -f deploy/docker/smoke-test.sh
test -f deploy/docker/nginx/nginx.conf
test -f deploy/docker/nginx/conf.d/default.conf
test -f docs/runbook.md
test -f docs/deployment-local-docker.md
test -f docs/rules/cr-docker-hath0r-group-001.md
test -f AGENTS.md
test -f README.md
test -d .hath0r/knowledgebase

# Forbidden legacy roots
for bad in .ai .aegis .infraOS; do
  if [[ -e "$bad" ]]; then
    echo "FAIL: forbidden hidden root $bad present"
    exit 1
  fi
done

echo "bootstrap ok"
