def analyze_log(filepath):
    error = 0
    warning = 0

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line = line.lower()
                if "error" in line:
                    error += 1
                if "warning" in line:
                    warning += 1

    except Exception as e:
        print("Log Analyzer Error:", e)

    # ✅ MUST return integers
    return int(error), int(warning)