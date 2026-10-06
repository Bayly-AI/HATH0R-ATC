#!/usr/bin/env bash
# Hath0r Docker group smoke test — NGINX edge + Redis (+ optional MCP)
set -u
PASS=0
FAIL=0

check() {
  local name="$1" ok="$2" detail="$3"
  if [[ "$ok" == "1" ]]; then
    printf 'PASS  %s — %s\n' "$name" "$detail"
    PASS=$((PASS + 1))
  else
    printf 'FAIL  %s — %s\n' "$name" "$detail"
    FAIL=$((FAIL + 1))
  fi
}

NGINX_PORT="${HATH0R_NGINX_HOST_PORT:-38000}"
LOOPBACK="127.0.0.1"

echo "=== Hath0r smoke test $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
echo

echo "--- container/group status ---"
docker ps -a --filter label=com.docker.compose.project=hath0r \
  --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' || true
echo

for c in hath0r-nginx hath0r-redis hath0r-phoenix; do
  st=$(docker inspect -f '{{.State.Status}} health={{if .State.Health}}{{.State.Health.Status}}{{else}}n/a{{end}}' "$c" 2>/dev/null || echo missing)
  echo "$c: $st"
  if [[ "$st" == missing ]]; then
    check "$c present" 0 "missing"
  elif [[ "$st" == running* ]] || [[ "$st" == *health* ]]; then
    check "$c present" 1 "$st"
  else
    check "$c present" 0 "$st"
  fi
done

# Optional members
for c in hath0r-postgres hath0r-mcp; do
  st=$(docker inspect -f '{{.State.Status}} health={{if .State.Health}}{{.State.Health.Status}}{{else}}n/a{{end}}' "$c" 2>/dev/null || echo missing)
  echo "$c: $st (optional)"
done
echo

echo "--- NGINX edge ---"
body=$(curl -fsS -m 5 "http://${LOOPBACK}:${NGINX_PORT}/healthz" 2>/dev/null || true)
if printf '%s' "$body" | grep -q 'ok'; then check "nginx /healthz" 1 "body=$(printf '%s' "$body" | tr '\n' ' ')"
else check "nginx /healthz" 0 "body=$body"; fi

body=$(curl -fsS -m 5 "http://${LOOPBACK}:${NGINX_PORT}/" 2>/dev/null || true)
if printf '%s' "$body" | grep -qi 'hath0r-nginx'; then check "nginx /" 1 "banner ok"
else check "nginx /" 0 "body=$body"; fi

# Phoenix via edge
code=$(curl -sS -m 8 -o /tmp/h0_phoenix.out -w '%{http_code}' "http://${LOOPBACK}:${NGINX_PORT}/phoenix/" 2>/dev/null || echo 000)
if [[ "$code" == "200" ]]; then
  check "nginx /phoenix/" 1 "http=$code (Arize Phoenix UI ok)"
else
  check "nginx /phoenix/" 0 "http=$code"
fi

# MCP via edge (optional — pass if MCP up, soft-fail note if not)
if docker inspect hath0r-mcp >/dev/null 2>&1; then
  code=$(curl -sS -m 8 -o /tmp/h0_mcp.out -w '%{http_code}' "http://${LOOPBACK}:${NGINX_PORT}/mcp/health" 2>/dev/null || echo 000)
  body=$(head -c 200 /tmp/h0_mcp.out 2>/dev/null | tr '\n' ' ')
  if [[ "$code" == "200" ]]; then
    check "nginx /mcp/health" 1 "http=$code body=$body"
  else
    check "nginx /mcp/health" 0 "http=$code body=$body"
  fi
else
  echo "SKIP  nginx /mcp/health — hath0r-mcp not running (standalone member)"
fi

echo
echo "--- Redis ---"
pong=$(docker exec hath0r-redis redis-cli ping 2>/dev/null || true)
[[ "$pong" == "PONG" ]] && check "redis-cli ping" 1 "$pong" || check "redis-cli ping" 0 "$pong"

docker exec hath0r-redis redis-cli DEL hath0r:smoke >/dev/null 2>&1 || true
setout=$(docker exec hath0r-redis redis-cli SET hath0r:smoke "ok-$(date +%s)" EX 60 2>/dev/null || true)
[[ "$setout" == "OK" ]] && check "redis SET hath0r:smoke" 1 "$setout" || check "redis SET hath0r:smoke" 0 "$setout"

getout=$(docker exec hath0r-redis redis-cli GET hath0r:smoke 2>/dev/null || true)
if printf '%s' "$getout" | grep -q '^ok-'; then check "redis GET hath0r:smoke" 1 "value=$getout"
else check "redis GET hath0r:smoke" 0 "value=$getout"; fi

# Reachability from edge on hath0r-net
if docker inspect hath0r-nginx >/dev/null 2>&1; then
  out=$(docker exec hath0r-nginx sh -c 'wget -qO- --timeout=3 http://127.0.0.1/healthz 2>/dev/null || true')
  if printf '%s' "$out" | grep -q ok; then check "nginx self healthz" 1 "$out"
  else check "nginx self healthz" 0 "$out"; fi

  for alias in hath0r-redis redis h0-redis; do
    ip=$(docker exec hath0r-nginx getent hosts "$alias" 2>/dev/null | awk '{print $1; exit}')
    if [[ -n "${ip:-}" ]]; then check "DNS alias $alias" 1 "resolves=$ip"
    else check "DNS alias $alias" 0 "unresolved"; fi
  done
fi

echo
echo "=== SUMMARY pass=$PASS fail=$FAIL ==="
[[ "$FAIL" -eq 0 ]]
