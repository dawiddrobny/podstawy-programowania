print("SURVEY Are you interested in computer science? (y/n): ", end='')
cs = input().lower() == 'y'
print("Do you like playing computer games? (y/n): ", end='')
games = input().lower() == 'y'
print("Do you have an Instagram account? (y/n): ", end='')
insta = input().lower() == 'y'

print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if cs else 'No'}")
print(f"Playing computer games: {'Yes' if games else 'No'}")
print(f"Has an Instagram account: {'Yes' if insta else 'No'}")
