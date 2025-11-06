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
unique_tracks = set(p['track'] for p in participants)

print("\nTracks offered in this event:")
print(", ".join(unique_tracks))

if len(unique_tracks) < 2:
    print("Not enough variety in tracks.")

seen_names = set()
duplicates = set()

for p in participants:
    if p['name'] in seen_names:
        duplicates.add(p['name'])
    else:
        seen_names.add(p['name'])

if duplicates:
    for name in duplicates:
        print(f"\nDuplicate name found: {name}")
else:
    print("\nNo duplicate names.")
track_summary = {}
for p in participants:
    track_summary[p['track']] = track_summary.get(p['track'], 0) + 1

print("\nParticipants per track:")
for track, count in track_summary.items():
    print(f"{track}: {count}")
