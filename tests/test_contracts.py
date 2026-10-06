"""Basic contract and configuration tests for HATH0R-ATC."""
from pathlib import Path
import json


def test_contracts_directory_exists() -> None:
    contracts_dir = Path(__file__).parent.parent / "contracts"
    assert contracts_dir.is_dir()


def test_cfg_observability() -> None:
    otel_path = Path(__file__).parent.parent / "cfg" / "observability" / "otel.json"
    if otel_path.is_file():
        data = json.loads(otel_path.read_text(encoding="utf-8"))
        assert "resource" in data
