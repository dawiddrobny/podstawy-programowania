x = int(input("x = "))
y = int(input("y = "))

if x == 0 and y == 0:
    pos = "the origin of the coordinate system"
elif x == 0:
    pos = "the y-axis"
elif y == 0:
    pos = "the x-axis"
elif x > 0 and y > 0:
    pos = "the first quadrant of the coordinate system"
elif x < 0 and y > 0:
    pos = "the second quadrant of the coordinate system"
elif x < 0 and y < 0:
    pos = "the third quadrant of the coordinate system"
elif x > 0 and y < 0:
    pos = "the fourth quadrant of the coordinate system"

print(f"Point P({x},{y}) is in {pos}")
