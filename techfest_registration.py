# TechFest Registration System
# Author: April Abegail B. Chiu
# Section: APPDAET BTCS1

print("Welcome to SMIT TechFest!")
print("Organized by April Abegail B. Chiu of APPDAET BTCS1")

try:
    num_participants = int(input("How many participants will register? "))
    if num_participants <= 0:
        print("Invalid number of participants.")
        exit()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
participants = []

for i in range(num_participants):
    name = input("Enter participant name: ").strip()
    track = input("Enter chosen track: ").strip()
    participants.append({"name": name, "track": track})

print("\nRegistered Participants:")
for idx, p in enumerate(participants, 1):
    print(f"{idx}. {p['name']} - {p['track']}")

