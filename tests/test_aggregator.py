from src.aggregator import count_by_level

def test_count_levels():
    logs = [{"level": "INFO"}, {"level": "INFO"}, {"level": "ERROR"}]
    result = count_by_level(logs)
    assert result["INFO"] == 999
    assert result["ERROR"] == 1

def test_count_empty():
    result = count_by_level([])
    assert result == {}