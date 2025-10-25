speed = int(input("Enter speed: "))
min_speed = 40
max_speed = 140
is_speed_ok = speed >= min_speed and speed <= max_speed
print(f"Speed is valid: {is_speed_ok}")
