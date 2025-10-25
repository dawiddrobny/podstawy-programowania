from random import randint

dice_roll = randint(1, 6)

print(f"Dice rolled: {dice_roll}")
print(f"Special number (1 or 6): {dice_roll == 1 or dice_roll == 6}")
