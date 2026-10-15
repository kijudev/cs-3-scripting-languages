from datetime import datetime

FORMAT = "%Y-%m-%d %H:%M:%S"

text = input(f"date ({FORMAT}): ") or "2023-10-15 14:30:00"

try:
    date = datetime.strptime(text, FORMAT)
except ValueError:
    print(f"'{text}' does not match format {FORMAT}")
else:
    print(f"{date=}")
    print(date.ctime())
