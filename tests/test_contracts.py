"""Basic contract and configuration tests for HATH0R-ATC."""
import json
from pathlib import Path


def test_contracts_directory_exists() -> None:
    contracts_dir = Path(__file__).parent.parent / "contracts"
    assert contracts_dir.is_dir()


def test_cfg_observability() -> None:
    otel_path = Path(__file__).parent.parent / "cfg" / "observability" / "otel.json"
    assert otel_path.is_file()
    data = json.loads(otel_path.read_text(encoding="utf-8"))
    assert "resource" in data
    assert data["exporters"]["otlp"]["default_endpoint"] == "http://localhost:38000/phoenix"
    assert "network_services" in data
    assert data["network_services"]["docker_network"] == "hath0r-net"
    assert data["network_services"]["phoenix"]["container"] == "Hath0r-phoenix"
    assert data["network_services"]["mlflow"]["container"] == "Hathor-MLFLOW"
    assert data["network_services"]["cruise_control"]["container"] == "Hath0r-Cruise-Control"

    openobs_path = Path(__file__).parent.parent / "cfg" / "observability" / "openobservation.json"
    assert openobs_path.is_file()
    openobs_data = json.loads(openobs_path.read_text(encoding="utf-8"))
    assert openobs_data["kind"] == "OpenObservationConfig"
    assert openobs_data["spool"]["never_block"] is True


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
        "Hath0r-Cruise-Control",
    ]
    for name in canonical_containers:
        assert f"container_name: {name}" in content, f"Missing container_name: {name}"


def test_docker_compose_cruise_control_and_nginx_route() -> None:
    compose_path = Path(__file__).parent.parent / "deploy" / "docker" / "docker-compose.yml"
    nginx_path = Path(__file__).parent.parent / "deploy" / "docker" / "nginx" / "conf.d" / "default.conf"
    compose_content = compose_path.read_text(encoding="utf-8")
    nginx_content = nginx_path.read_text(encoding="utf-8")

    assert "container_name: Hath0r-Cruise-Control" in compose_content
    assert "hath0r_cruise_data" in compose_content
    assert "38090" in compose_content
    assert "com.hath0r.component: cruise-control" in compose_content

    assert "location /cruise/ {" in nginx_content
    assert "proxy_pass http://Hath0r-Cruise-Control:8090/;" in nginx_content
    assert "location /api/decisions {" in nginx_content


