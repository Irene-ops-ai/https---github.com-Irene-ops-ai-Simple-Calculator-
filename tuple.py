emergency_exits = (
    ("Main Lobby", 1, 12.5),
    ("ER Back", 1, 87.3),
    ("ICU Wing", 3, 45.0)
)

print("Exit near ICU:", emergency_exits[2][0])

emergency_exits[1] = ("Lab Zone", 2, 33.1)

try:
    emergency_exits[1] = ("Lab Zone", 2, 33.1)
except TypeError as e:
    print("Security Alert! ", e) 