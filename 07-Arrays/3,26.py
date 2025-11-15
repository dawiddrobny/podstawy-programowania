import matplotlib.pyplot as plt
import math

x = []
y = []

for angle in range(0, 361):
    x.append(angle)
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y)
plt.title('y = sin(x) for x in degrees')
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
