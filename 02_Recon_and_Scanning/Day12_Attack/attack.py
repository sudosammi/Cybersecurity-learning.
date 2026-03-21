#    Day12: Dictionary attack Simulation

import time

print("---BRUTE FORCE TOOL V1.0---")

target_password = "secret123"

file_name = input("Enter password list filename: ")

try:
    file = open(file_name, "r")

    print("Running attack on target......")
    time.sleep(1)

    for word in file:
        guess = word.strip()
 
        print("Trying password: " + guess)

        if guess == target_password:

            print("----------------------------")
            print("PASSWORD CRACKED" + guess)
            print("----------------------------")
            break

        time.sleep(0.1)

    file.close()

except FileNotFoundError:
    print(" Error: File nahi mili! Naam sahi likho.")

print("Attack Finished.")
