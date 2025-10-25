###
# A program that prints your height both in cm and in feet and inches.
#
cm = 174

# calculate the number of feet
feet = int(cm // 30.48)

inches = int((cm % 30.48) // 2.54)

print(f"I am {cm}cm tall, i.e. {feet} feet and {inches} inches")
