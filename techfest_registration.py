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
