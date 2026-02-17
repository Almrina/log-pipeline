from src.filter import filter_by_level

def test_filter_info():
    logs = [{"level": "INFO"}, {"level": "ERROR"}]
    result = filter_by_level(logs, "INFO")
    assert len(result) == 1

def test_filter_empty():
    logs = []
    result = filter_by_level(logs, "INFO")
    assert result == []