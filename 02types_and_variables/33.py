###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# User enters temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))
# Kelvin = Celsius + 273.15
kelvin = celsius + 273.15
# Fahrenheit = Celsius * 9/5 + 32
fahrenheit = celsius * 9 / 5 + 32
# Print the results
print(f"Temperature in Kelvin: {kelvin}")
print(f"Temperature in Fahrenheit: {fahrenheit}")
