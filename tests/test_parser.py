from src.parser import parse_log_line
import pytest

def test_parse_log_line():
    line = "INFO,Application started"
    result = parse_log_line(line)
    assert result["level"] == "INFO"
    assert result["message"] == "Application started"

def test_parse_invalid_line():
    with pytest.raises(IndexError):
        parse_log_line("INVALID")
