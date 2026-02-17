def count_by_level(logs):
    result = {}
    for log in logs:
        level = log["level"]
        result[level] = result.get(level, 0) + 1
    return result
