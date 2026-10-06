# site/ — optional nested service stubs

Hath0r ATC keeps shared infrastructure under `deploy/docker/`.

Product application code does **not** live here by default. Framework work stays in sibling `../hath0r`. Standalone MCP stays in `../hath0r-mcp`.

Use this folder only for thin deploy stubs or future site-local helpers that must remain in the control-tower tree while still joining compose project `hath0r` / network `hath0r-net`.
