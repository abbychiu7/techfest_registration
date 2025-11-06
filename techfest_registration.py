# TechFest Registration System
# Author: April Abegail B. Chiu
# Section: APPDAET BTCS1

# ANSI escape codes for calm colors
HEADER = "\033[94m"  # soft blue
INFO = "\033[92m"  # soft green
WARNING = "\033[93m"  # soft yellow
ERROR = "\033[91m"  # soft red
RESET = "\033[0m"  # reset to default

# Welcome messages
print(f"{HEADER}\nWelcome to SMIT TechFest!{RESET}")
print(f"{INFO}Submitted by April Abegail B. Chiu of APPDAET BTCS1{RESET}")
print("-" * 50)

# Participant registration
try:
    num_participants = int(input("How many participants will register? "))
    if num_participants <= 0:
        print(f"{ERROR}Invalid number of participants.{RESET}")
        exit()
except ValueError:
    print(f"{ERROR}Invalid input. Please enter a number.{RESET}")
    exit()

participants = []

for i in range(num_participants):
    print(f"\nParticipant {i + 1}:")
    name = input("  Enter participant name: ").strip()
    track = input("  Enter chosen track: ").strip()
    participants.append({"name": name, "track": track})

# Display registered participants
print(f"\n{HEADER}Registered Participants:{RESET}")
for idx, p in enumerate(participants, 1):
    print(f"  {idx}. {p['name']} - {p['track']}")

# Track diversity report
unique_tracks = set(p['track'] for p in participants)
print(f"\n{INFO}Tracks offered in this event:{RESET}")
print("  " + ", ".join(unique_tracks))
if len(unique_tracks) < 2:
    print(f"{WARNING}Not enough variety in tracks.{RESET}")

# Duplicate name detection
seen_names = set()
duplicates = set()
for p in participants:
    if p['name'] in seen_names:
        duplicates.add(p['name'])
    else:
        seen_names.add(p['name'])

if duplicates:
    for name in duplicates:
        print(f"\n{WARNING}Duplicate name found: {name}{RESET}")
else:
    print(f"\n{INFO}No duplicate names.{RESET}")

# Track summary report
track_summary = {}
for p in participants:
    track_summary[p['track']] = track_summary.get(p['track'], 0) + 1

print(f"\n{HEADER}Participants per track:{RESET}")
for track, count in track_summary.items():
    print(f"  {track}: {count}")

print("\n" + "-" * 50)
print(f"{INFO}Thank you for using the TechFest Registration System!{RESET}")
