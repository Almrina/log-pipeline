from src.parser import parse_log_line
from src.aggregator import count_by_level

def test_integration_file(tmp_path):
    file = tmp_path / "log.txt"
    file.write_text("INFO,Start\nERROR,Crash\nINFO,Run")

    lines = file.read_text().splitlines()
    logs = [parse_log_line(line) for line in lines]
    result = count_by_level(logs)

    assert result["INFO"] == 2
    assert result["ERROR"] == 1
