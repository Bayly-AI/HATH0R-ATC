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


def test_docker_compose_mlflow() -> None:
    compose_path = Path(__file__).parent.parent / "deploy" / "docker" / "docker-compose.yml"
    assert compose_path.is_file()
    content = compose_path.read_text(encoding="utf-8")
    assert "Hathor-MLFLOW" in content
    assert "hath0r_mlflow_data" in content
    assert "35000" in content


def test_canonical_container_names() -> None:
    compose_path = Path(__file__).parent.parent / "deploy" / "docker" / "docker-compose.yml"
    assert compose_path.is_file()
    content = compose_path.read_text(encoding="utf-8")
    canonical_containers = [
        "Hath0r-phoenix",
        "Hath0r-Edge",
        "Hath0r-Data",
        "Hath0r-Sessions",
        "Hath0r-MCP",
    ]
    for name in canonical_containers:
        assert f"container_name: {name}" in content, f"Missing container_name: {name}"

