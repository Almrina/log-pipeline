def parse_log_line(line: str):
    parts = line.strip().split(",")
    return {
        "level": parts[0],
        "message": parts[1]
    }
