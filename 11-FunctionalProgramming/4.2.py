values = [48, 47, 54, 50, 42, 68, 39, 46]
too_high = list(filter(lambda v: v > 50, values))

print(f"Recorded values: {values}")
print(f"Speed too high: {too_high}")
