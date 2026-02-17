def filter_by_level(logs, level):
    return [log for log in logs if log["level"] == level]
