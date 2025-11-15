def occurs(number, array):
    return number in array


arr = [15, 38, 7, 23, 14]
number = int(input("Number: "))
print("Array:", end=" ")
for num in arr:
    print(num, end=" ")
print()
if occurs(number, arr):
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
