# AGENTS.md — Site Subsystem (HATH0R-ATC)

> Hyper-context node for **HATH0R ATC Portal & Static Web Subsystem**.
> Parent Node: [`../AGENTS.md`](../AGENTS.md)

## Subsystem Identity & Role

| Field | Value |
|---|---|
| Subsystem | `site` |
| Scope | Static Landing Portal, Control Tower Dashboard UI |

## Operational Guidelines

1. **Lightweight & Portable**: Site assets must be lightweight and function without heavy Node build chains or remote dependencies.
2. **Local Serving**: Serve cleanly behind NGINX at port `38080` (or root path `/`).
3. **No External CDN Lock-In**: Avoid external third-party CDN scripts or fonts.

## Key Files & Direct Links

- [README.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/site/README.md): Site subsystem overview.
- [rules.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/site/rules.md): Static site design rules.
- [canonical.md](file:///Users/raybayly/Development/OpenSource/hath0r-atc/site/canonical.md): Site structure index.
