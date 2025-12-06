import json
import os

file_name = 'voting.json'

# Load existing votes or initialize
if os.path.exists(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        try:
            votes = json.load(f)
        except json.JSONDecodeError:
            votes = {}
else:
    votes = {}

print("Current Voting Data:")
print(votes)

# Vote for a person
person_name = input('Name of the person you are voting for: ')

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(votes, f, indent=4)

print(f"Vote recorded for {person_name}. Total votes: {votes[person_name]}")
