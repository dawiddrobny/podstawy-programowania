def f(detector):
    current = 0
    max_occupancy = 0
    for event in detector:
        if event == "+":
            current += 1
        elif event == "-":
            current -= 1
        max_occupancy = max(max_occupancy, current)
    return max_occupancy >= 3


print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
