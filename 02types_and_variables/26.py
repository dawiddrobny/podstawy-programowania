import math

tree_circumference = int(input("Enter tree circumference in cm: "))
can_be_cut = tree_circumference / math.pi >= 50
print(f"Tree can be cut down: {can_be_cut}")
