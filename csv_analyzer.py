import csv

def analyze_csv(filepath):
    error = 0
    warning = 0

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            reader = csv.reader(file)

            for row in reader:
                row_text = " ".join(row).lower()

                if "error" in row_text:
                    error += 1
                if "warning" in row_text:
                    warning += 1

    except Exception as e:
        print("CSV Analyzer Error:", e)

    # ✅ MUST return integers
    return int(error), int(warning)