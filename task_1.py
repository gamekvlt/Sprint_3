time_string = "1h 45m,360s,25m,30m 120s,2h 60s"

parts = time_string.split(",")
total_minutes = 0

for part in parts:
    time_part = part.strip()
    pieces = time_part.split()

    for piece in pieces:
        if "h" in piece:
            hours = int(piece.replace("h", ""))
            total_minutes += hours * 60
        elif "m" in piece:
            minutes = int(piece.replace("m", ""))
            total_minutes += minutes
        elif "s" in piece:
            seconds = int(piece.replace("s", ""))
            total_minutes += seconds // 60

print(total_minutes)
